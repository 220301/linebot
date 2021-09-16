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

line_bot_api = LineBotApi('iG/aMf7s4WYCXhWAbJzpoSPQ5bdSvhzN49TqHMOgooFth/XwsZ2DZVk3SkRWgrYpDCKZT8k3r7cWfcr7FoMfUEV9WbGATAaL7M0VXkPwDiiGUuB8BaU7lN6dQYM+OS9cjJz0cg8cSEGPrZR8IVTSFAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('83396750185dc1029f875099f28d3c72')
#line_bot_api.reply_message(reply_token, TextSendMessage(text='Hello World!'))

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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
