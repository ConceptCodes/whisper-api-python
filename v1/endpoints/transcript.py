import uuid
import os
import datetime
from sqlmodel import select
from fastapi import APIRouter

from core.schemas.response import ApiResponseModel
from core.schemas.transcript import (
    GetStatusResponse,
    TranscriptCreateRequest,
)
from core.models.uploads import Uploads
from core.util.response import send_success_response, send_error_response
from core.config import app_config

from lib.db import db_client
from lib.s3 import s3_client
from lib.kafka import kafka_client

router = APIRouter()


@router.get("/transcript/{transcript_id}/status",
            tags=["transcript"],
            summary="get a transcript by id",
            description="get a transcript by id",
            )
async def get_status(transcript_id: int) -> ApiResponseModel:
    try:
        session = db_client.get_session()
        statement = select(Uploads).where(Uploads.id == transcript_id)
        transcript = session.exec(statement)
        if transcript:
            data = GetStatusResponse(
                status=transcript.status, updated_at=transcript.updatedAt)
            return send_success_response("Transcript Status retrieved successfully", data)
        else:
            return send_error_response("Transcript not found", 404)
    except Exception as e:
        return send_error_response(str(e), 500)


@router.get("/transcript/{transcript_id}/download",
            tags=["transcript"],
            summary="download a transcript by id",
            description="download a transcript by id",
            )
# TODO: modify to return the file
async def download(transcript_id: int) -> ApiResponseModel:
    try:
        session = db_client.get_session()
        statement = select(Uploads).where(Uploads.id == transcript_id)
        transcript = session.exec(statement)
        if transcript:
            s3_client.download_file(transcript.file_id)
            file = os.path.join(app_config.ASSET_DIR, f"{transcript.file_id}.txt")
            return file
        else:
            return send_error_response("Transcript not found", 404)
    except Exception as e:
        return send_error_response(str(e), 500)


@router.post("/transcript",
             tags=["transcript"],
             summary="create a transcript",
             description="create a transcript",
             )
async def create(req: TranscriptCreateRequest) -> ApiResponseModel:
    try:
        session = db_client.get_session()
        file_id = uuid.uuid4()
        upload = Uploads(file_id=file_id, status="pending",
                             created=datetime.datetime.now(datetime.UTC),
                             updated=datetime.datetime.now(datetime.UTC),
                             )
        session.add(upload)
        session.commit()

        s3_client.upload_file(req.file_path, f"{file_id}_mp3")
        kafka_client.send_message(app_config.KAFKA_TOPIC, {
            "file_id": file_id,
        })
        return send_success_response("Transcript created successfully")
    except Exception as e:
        return send_error_response(str(e), 500)
