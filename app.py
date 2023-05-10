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
    
import db

tmp = {}

app = Flask(__name__)

line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))

handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))

# line_bot_api.push_message(os.getenv("MY_ID"), TextSendMessage(text='你可以開始了'))

def replyText(event, text):
    if text == "抱歉，革命失敗，請再試一次":
        tmp[id] = {}

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
    id = event.source.user_id
    if db.is_ok(id):
        message = TextSendMessage(text=event.message.text)
        # line_bot_api.reply_message(event.reply_token, message)
        if event.message.text == "我要預購":
            tmp[id] = {'type': 'preorder'}
            func.preorder()
        elif event.message.text == "我要外送":
            tmp[id] = {'type': 'deliver'}
            func.deliver(event)

        if event.message.text == '要美乃滋':
            try:
                tmp[id]['sauce'] = 1
                func.send_back_amount_mini(event)
            except:
                replyText(event, "抱歉，革命失敗，請再試一次")
        elif event.message.text == '不要美乃滋':
            try:
                tmp[id]['sauce'] = 0
                func.send_back_amount_mini(event)
            except:
                replyText(event, "抱歉，革命失敗，請再試一次")
        elif event.message.text.split('：')[0] == '數量（小）':
            try:
                amount_m = int(event.message.text.split('：')[1])
                tmp[id]['amount_m'] = amount_m
                func.send_back_amount_large(event)
            except:
                replyText(event, "抱歉，革命失敗，請再試一次")
        elif event.message.text.split('：')[0] == '數量（大）':
            try:
                amount_l = int(event.message.text.split('：')[1])
                tmp[id]['amount_l'] = amount_l
                func.send_back_grade(event)
            except:
                replyText(event, "抱歉，革命失敗，請再試一次")
        elif event.message.text.split('：')[0] == '年級':
            try:
                print("yee1")
                tmp[id]['grade'] = event.message.text.split('：')[1]
                print("yee2")
                if tmp[id]['grade'] != "老師" and tmp[id]['grade'] != "家長":
                    func.send_back_class(event)
                else:
                    tmp[id]['class'] = ""
                    tmp[id]['number'] = ""
                    func.send_back_name(event)
                print("yee3")
            except:
                replyText(event, "抱歉，革命失敗，請再試一次")
                print("好亮")
        elif event.message.text.split('：')[0] == '班級' or event.message.text.split(':')[0] == '班級':
            try:
                if event.message.text.split('：')[0] == "班級":
                    _class = event.message.text.split('：')[1]
                else:
                    _class = event.message.text.split(':')[1]
                
                if not _class.isalpha() or len(_class) != 1:
                    replyText(event, "同志，請輸入班級啊！（範例：「班級：忠」）")
                else:
                    tmp[id]['class'] = event.message.text.split('：')[1]
                    func.send_back_number(event)
            except:
                replyText(event, "抱歉，革命失敗，請再試一次")
        elif event.message.text.split('：')[0] == "座號" or event.message.text.split(':')[0] == "座號":
            if event.message.text.split('：')[0] == "座號":
                number = event.message.text.split('：')[1]
            else:
                number = event.message.text.split(':')[1]
            try:
                if number.isdigit():
                    tmp[id]['number'] = number
                    func.send_back_name(event)
                else:
                    replyText(event, "同志，請輸入數字啊！（範例：「座號：1」）")
            except:
                replyText(event, "抱歉，革命失敗，請再試一次")
        elif event.message.text.split('：')[0] == "姓名" or event.message.text.split(':')[0] == "姓名":
            if event.message.text.split('：')[0] == "姓名":
                name = event.message.text.split('：')[1]
            else:
                name = event.message.text.split(':')[1]

            try:
                if name.isalpha():
                    tmp[id]['name'] = name

                    if tmp[id]['type'] == 'deliver':
                        func.send_back_pos(event)

                else:
                    replyText(event, "同志，請輸入名字啊！（範例：「姓名：弗拉迪米爾·列寧」）")
            except:
                replyText(event, "抱歉，革命失敗，請再試一次")
        elif event.message.text.split('：')[0] == "位置" or event.message.text.split(':')[0] == "位置":
            if event.message.text.split('：')[0] == "位置":
                location = event.message.text.split('：')[1]
            else:
                location = event.message.text.split(':')[1]
            
            try:
                if location.isalpha():
                    tmp[id]['pos'] = location
                    func.send_back_note(event)
                else:
                    replyText(event, "同志，請輸入明確的位置啊！（範例：「位置：校門口」）")
            except:
                replyText(event, "抱歉，革命失敗，請再試一次")
        elif event.message.text.split('：')[0] == "備註" or event.message.text.split('：')[0] == "備注" or event.message.text.split(':')[0] == "備註" or event.message.text.split(':')[0] == "備注":
            if event.message.text.split('：')[0] == "備註" or event.message.text.split('：')[0] == "備注":
                note = event.message.text.split('：')[1]
            else:
                note = event.message.text.split(':')[1]
            try:
                tmp[id]['note'] = note
                total = func.send_back_confirm(event, tmp[id]['amount_m'], tmp[id]['amount_l'])
                if total != -1:
                    tmp[id]['total'] = total
            except:
                replyText(event, "抱歉，革命失敗，請再試一次")

        elif event.message.text == '送出':
            if db.append(id, tmp):
                replyText(event, "革命成功——已接到訂單")
            else:
                replyText(event, "抱歉，革命失敗，請再試一次")

        elif event.message.text == '取消':
            tmp.pop(id, -1)
            replyText(event, "革命未成，永不忘初衷！")
            
        else:
            replyText(event, "抱歉同志，沒辦法理解您的指令。難道你是反革命分子？")
    else:
        replyText(event, "抱歉，無法處理您的訂單，這可能是因為訂單數出過上限。歡迎同志親自到訪參與革命！")



# main
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
