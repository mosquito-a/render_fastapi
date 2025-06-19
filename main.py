# main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/index", response_class=HTMLResponse)
def index():
    html_content = """
    <html>
        <head>
            <title>私の素晴らしいページ</title>
        </head>
        <body>
            <h1>ようこそ、私の最初のウェブページへ！</h1>
            <p>これはカスタムコンテンツです。</p>
            <ul>
                <li>アイテム1</li>
                <li>アイテム2</li>
            </ul>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/receive_message")
async def receive_message(message: str):
    return {"server_response": f"メッセージを受け取りました！: '{message}'。ありがとうございます！"}
