import os
from dotenv import load_dotenv
load_dotenv()
from linebot import LineBotApi
from linebot.models import *

from linebot.models import FlexSendMessage
from linebot.models.flex_message import (
    BubbleContainer, ImageComponent,BoxComponent
)
from linebot.models.actions import URIAction

line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))

# import pygsheets
# gc = pygsheets.authorize()
# db = gc.open_by_url("https://docs.google.com/spreadsheets/d/1RFCcgCFkhk6lhfF04-0EeeILHSP7mwwPVObYUxaAS-g/edit#gid=0")[0]
# df = db.get_as_df()

def preorder():
    message = TemplateSendMessage(
            alt_text='Buttons template',
            template = ButtonsTemplate( 
                thumbnail_image_url="https://photoos.mac89.com/EPS180507/180507_203/dZAn5ItFQT_small.jpg",
                title='choice',
                text='請問需不需要美乃滋？',
                actions=[
                    PostbackTemplateAction(
                        label='要',
                        text='要',
                        data='action=要美乃滋'
                    ),
                    PostbackTemplateAction(
                        label='不要',
                        text='不要',
                        data='action=不要美乃滋'
                    )
                ]
            )
            
        )

def deliver(event):
    try:
        message = TemplateSendMessage(
            alt_text = '美乃滋？',
            template = ButtonsTemplate( 
                thumbnail_image_url="https://photoos.mac89.com/EPS180507/180507_203/dZAn5ItFQT_small.jpg",
                title='同志需不需要美乃滋？',
                text='美乃滋加／不加',
                actions=[
                    PostbackTemplateAction(
                        label='要美乃滋',
                        text='要美乃滋',
                        data='action=要美乃滋'
                    ),
                    PostbackTemplateAction(
                        label='不要美乃滋',
                        text='不要美乃滋',
                        data='action=不要美乃滋'
                    ),
                    PostbackTemplateAction(
                        label='取消',
                        text='取消',
                        data='action=取消'
                    )
                ]
            )   
            )
        line_bot_api.reply_message(event.reply_token, message)

    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='不買'))

def send_back_grade(event):
    try:
        message = TextSendMessage(
            text='同志是哪個年級？',
            quick_reply=QuickReply(items=[
                QuickReplyButton(action=PostbackTemplateAction(label="老師", text="年級：老師", data='GRADE&老師')),
                QuickReplyButton(action=PostbackTemplateAction(label="七", text="年級：七", data='GRADE&七')),
                QuickReplyButton(action=PostbackTemplateAction(label="八", text="年級：八", data='GRADE&八')),
                QuickReplyButton(action=PostbackTemplateAction(label="九", text="年級：九", data='GRADE&九')),
                QuickReplyButton(action=PostbackTemplateAction(label="一", text="年級：一", data='GRADE&一')),
                QuickReplyButton(action=PostbackTemplateAction(label="二", text="年級：二", data='GRADE&二')),
                QuickReplyButton(action=PostbackTemplateAction(label="三", text="年級：三", data='GRADE&三'))
            ]))
        
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='抱歉，革命失敗，請再試一次'))

def send_back_class(event):
    try:
        message = TextSendMessage(
            text='同志是哪個班級？',
            quick_reply=QuickReply(items=[
                QuickReplyButton(action=PostbackTemplateAction(label="忠", text="班級：忠", data='CLASS&七')),
                QuickReplyButton(action=PostbackTemplateAction(label="孝", text="班級：孝", data='CLASS&八')),
                QuickReplyButton(action=PostbackTemplateAction(label="仁", text="班級：仁", data='CLASS&九')),
                QuickReplyButton(action=PostbackTemplateAction(label="愛", text="班級：愛", data='CLASS&一')),
                QuickReplyButton(action=PostbackTemplateAction(label="信", text="班級：信", data='CLASS&二')),
                QuickReplyButton(action=PostbackTemplateAction(label="義", text="班級：義", data='CLASS&三'))
            ]))
        
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='抱歉，革命失敗，請再試一次'))