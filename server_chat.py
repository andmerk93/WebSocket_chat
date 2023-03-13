from datetime import datetime
from json import dumps, loads
from typing import List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(
        self, 
        time: str,
        nickname: str,
        message: str, 
        websocket: WebSocket
    ):
        for connection in self.active_connections:
            if connection == websocket:
                nickname = 'You'
            export_data = {
                'count': f"{(10):03}",
                'time': time,
                'nickname': nickname,
                'text': message,
            }
            json_data = dumps(export_data)
            await connection.send_text(json_data
#                f"[{time}] {nickname}: {message}"
            )


manager = ConnectionManager()
app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


@app.get("/")
async def get():
    return FileResponse('index.html')


@app.get("/client.js")
async def get():
    return FileResponse('client.js')


@app.get('/favicon.ico')
def get():
    return None


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            time = datetime.now().strftime("%H:%M:%S")
            json_data = await websocket.receive_text()
            data = loads(json_data)
            nickname = data['nick']
            message = data['text']
            #nickname, message = [*data.items()][0]
            await manager.broadcast(time, nickname, message, websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(time, nickname, 'left the chat', websocket)

