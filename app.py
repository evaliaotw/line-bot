
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('GyUSRM7NRIOC4Z1psTDcj2Dn7hQqfHIl7JMBjKoa3YxbjOOlxIUcY6/XW5N6WKasW7rh33BczBnNlbGDW0TbU5/Z7ACK6knc/OG/lDbEK7E49p9NuicJkHl65ORGipG5W6+gMbL7yvOsLJ/FMf+4MgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a8a2734d923e7e49ca3fe509bfab80ed')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '很抱歉,您說什麼?'

    if msg == 'hi':
        r = 'hi'
    elif msg == '你吃飯了嗎?'
        r = '還沒!'
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()