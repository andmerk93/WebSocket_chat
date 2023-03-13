from datetime import datetime
import json

from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse


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
    global count
    count = 0
    await websocket.accept()
    while True:
        time = datetime.now().strftime("%H:%M:%S")
        json_data = await websocket.receive_text()
        data = json.loads(json_data)
        nickname = data['nick']
        text = data['text']
#        nickname, text = [*data.items()][0]
        count += 1
#        export_data = {'message': f"{(count):03} [{time}] {nickname}: {text}"}
        export_data = {
            'count': f"{(count):03}",
            'time': time,
            'nickname': nickname,
            'text': text,
        }
        json_data = json.dumps(export_data)
        await websocket.send_text(json_data)
