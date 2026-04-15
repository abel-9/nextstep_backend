from fastapi import APIRouter
from src.core.oauth import TOKEN

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    responses={404: {"description": "Not found"}},
)


@router.websocket("/chat")
async def websocket_endpoint(websocket, token: TOKEN):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
