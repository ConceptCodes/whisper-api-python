import uuid
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
            return send_success_response("Here is a message", data)
        else:
            return send_error_response("Transcript not found", 404)
    except Exception as e:
        return send_error_response(str(e), 500)


@router.get("/transcript/{transcript_id}/download",
            tags=["transcript"],
            summary="download a transcript by id",
            description="download a transcript by id",
            )
async def download(transcript_id: int) -> ApiResponseModel:
    try:
        session = db_client.get_session()
        statement = select(Uploads).where(Uploads.id == transcript_id)
        transcript = session.exec(statement)
        if transcript:
            file = s3_client.download_file(transcript.transcript_file_id)
            return send_success_response(file)
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
        audio_file_id = uuid.uuid4()
        transcript = Uploads(audio_file_id=audio_file_id, status="pending",
                             created=datetime.datetime.utcnow(),
                             updated=datetime.datetime.utcnow(),
                             )
        session.add(transcript)
        session.commit()
        kafka_client.send_message(app_config.KAFKA_TOPIC, {
            "file_name": req.file_name,
            "audio_file_id": audio_file_id,
        })
        return send_success_response("Transcript created successfully")
    except Exception as e:
        return send_error_response(str(e), 500)
