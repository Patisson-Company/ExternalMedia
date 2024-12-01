from io import BytesIO

from db.base import get_session
from db.models import File
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

router = APIRouter()

@router.get('/{id}')
async def get_route(id: str) -> StreamingResponse:
    async with get_session() as session:
        file = await session.get(File, id)
    if not file: raise HTTPException(status_code=404, detail="File not found")
    return StreamingResponse(
        BytesIO(file.data),  # type: ignore
        media_type=file.mime_type  # type: ignore
    )
    