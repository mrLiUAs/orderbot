import os
from flask import Flask, request, abort, render_template
from urllib.parse import parse_qsl
from dotenv import load_dotenv
load_dotenv()
import func

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

# Google Sheet
import pygsheets
gc = pygsheets.authorize(service_account_env_var="SERVICE_FILE")
db_d = gc.open_by_url(os.getenv("DB_URL"))[0]

def is_here(id):
    df = db_d.get_as_df()
    return id in df['id'].values

def where(id):
    df = db_d.get_as_df()
    return df[df['id'] == id].index[0]

def append_d(id):
    try:
        db_d.append_table(values=[id, tmp_d[id]['sauce'], tmp_d[id]['grade'], tmp_d[id]['class']])
        tmp_d.pop(id, -1)
        return True
    except:
        return False
    


tmp_d = {}
tmp_t = {}

app = Flask(__name__)

line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))

handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))

# line_bot_api.push_message(os.getenv("MY_ID"), TextSendMessage(text='你可以開始了'))

def replyText(event, text):
    msg = TextSendMessage(text=text)
    line_bot_api.reply_message(event.reply_token, msg)

# @app.route("/")
# def index():
#   return render_template(r'index.html')

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
    message = TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token, message)
    if event.message.text == "我要預購":
        tmp_d[event.source.user_id] = {}
        func.preorder()
    elif event.message.text == "我要外送":
        tmp_d[event.source.user_id] = {}
        func.deliver(event)

    if event.message.text == '要美乃滋':
        try:
            tmp_d[event.source.user_id]['sauce'] = 1
            func.send_back_grade(event)
        except:
            replyText(event, "抱歉，革命失敗，請再試一次")

        func.send_back_class(event)

    elif event.message.text == '不要美乃滋':
        try:
            tmp_d[event.source.user_id]['sauce'] = 0
            func.send_back_grade(event)
        except:
            replyText(event, "抱歉，革命失敗，請再試一次")

        func.send_back_class(event)

    elif event.message.text.split('：')[0] == '年級':
        try:
            tmp_d[event.source.user_id]['grade'] = event.message.text.split('：')[1]
            func.send_back_class(event)
        except:
            replyText(event, "抱歉，革命失敗，請再試一次")
    elif event.message.text.split('：')[0] == '班級':
        try:
            tmp_d[event.source.user_id]['class'] = event.message.text.split('：')[1]
            if append_d(event.source.user_id):
                replyText(event, "革命成功——已接到訂單")
            else:
                replyText(event, "抱歉，革命失敗，請再試一次")
        except:
            replyText(event, "抱歉，革命失敗，請再試一次")
    elif event.message.text == '取消':
        db_d.pop(event.source.user_id, -1)
        replyText(event, "革命未成，永不忘初衷！")
        


# main
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
