
import os
from flask import Flask, request, abort
from dotenv import load_dotenv
load_dotenv()

from linebot import (
  LineBotApi, WebhookHandler
)
from linebot.exceptions import (
  InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))

handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))

line_bot_api.push_message(os.getenv('MY_ID'), TextSendMessage(text='你可以開始了'))

# /callback Post Request
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
      abort(400)

  return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  print('hehe')
  message = TextSendMessage(text=event.message.text)
  line_bot_api.reply_message(event.reply_token, message)

# main
if __name__ == "__main__":
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)