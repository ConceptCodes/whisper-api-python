from fastapi import APIRouter
from sqlmodel import select

from core.schemas.response import ApiResponseModel
from core.schemas.transcript import Transcripts
from core.util.response import send_success_response, send_error_response
from lib.db import db

router = APIRouter()


@router.get("/transcript/{transcript_id}",
            tags=["transcript"],
            summary="get a transcript by id",
            description="get a transcript by id",
        )
async def get_transcript_by_id(transcript_id: int) -> ApiResponseModel:
    try:
        session = db.get_session()
        statement = select(Transcripts).where(Transcripts.id == transcript_id)
        transcript = session.exec(statement)
        if transcript:
            return send_success_response(transcript)
        else:
            return send_error_response("Transcript not found", 404)
    except Exception as e:
        return send_error_response(str(e), 500)
