from core.models.uploads import Uploads
from lib.kafka import kafka_client
from lib.s3 import s3_client
from lib.db import db_client
from lib.logger import logger
from core.config import app_config
from sqlmodel import select
import whisper
import json
import os


def on_message(message):
    logger.info(f"Received message: {message}")
    data = json.loads(message)

    file_id = data["file_id"]

    if not file_id:
        logger.error("Audio file id is missing")
        return

    s3_client.download_file(file_id, "mp3")

    session = db_client.get_session()
    
    statement = select(Uploads).where(
        Uploads.audio_file_id == file_id)
    upload = session.exec(statement)

    if not upload:
        logger.error(
            f"Transcript not found for audio file id: {file_id}")
        return

    upload.status = "processing"
    session.update(upload)
    session.commit()

    file_path_mp3 = os.path.join(app_config.ASSET_DIR, f"{file_id}.mp3")
    file_path_txt = os.path.join(app_config.ASSET_DIR, f"{file_id}.txt")

    model = whisper.load_model("base")
    result = model.transcribe(file_path_mp3)

    with open(file_path_txt, "w") as file:
        file.write(result)

    s3_client.upload_file(file_path_txt, f"{file_id}_txt")

    upload.status = "completed"
    session.update(upload)
    session.commit()

    os.remove(f"{file_id}.txt")
