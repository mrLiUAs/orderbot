import os
# from dotenv import load_dotenv
# load_dotenv()
from linebot import LineBotApi
from linebot.models import *

from linebot.models import FlexSendMessage
from linebot.models.flex_message import (
    BubbleContainer, ImageComponent,BoxComponent
)
from linebot.models.actions import URIAction

import db

line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))

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
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='抱歉，革命失敗，請再試一次'))

def send_back_amount_mini(event):
    try:
        message = TextSendMessage(
            text='同志要幾份MINI堡？',
            quick_reply=QuickReply(items=[
                QuickReplyButton(action=PostbackTemplateAction(label="0", text="數量（小）：0", data='NUM&0')),
                QuickReplyButton(action=PostbackTemplateAction(label="1", text="數量（小）：1", data='NUM&1')),
                QuickReplyButton(action=PostbackTemplateAction(label="2", text="數量（小）：2", data='NUM&2')),
                QuickReplyButton(action=PostbackTemplateAction(label="3", text="數量（小）：3", data='NUM&3')),
                QuickReplyButton(action=PostbackTemplateAction(label="4", text="數量（小）：4", data='NUM&4')),
                QuickReplyButton(action=PostbackTemplateAction(label="5", text="數量（小）：5", data='NUM&5')),
                QuickReplyButton(action=PostbackTemplateAction(label="6", text="數量（小）：6", data='NUM&6')),
                QuickReplyButton(action=PostbackTemplateAction(label="7", text="數量（小）：7", data='NUM&7')),
                QuickReplyButton(action=PostbackTemplateAction(label="8", text="數量（小）：8", data='NUM&8')),
                QuickReplyButton(action=PostbackTemplateAction(label="9", text="數量（小）：9", data='NUM&9')),
                QuickReplyButton(action=PostbackTemplateAction(label="10", text="數量（小）：10", data='NUM&10'))
            ])
        )

        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='抱歉，革命失敗，請再試一次'))

def send_back_amount_large(event):
    try:
        message = TextSendMessage(
            text='同志要幾份LARGE堡？',
            quick_reply=QuickReply(items=[
                QuickReplyButton(action=PostbackTemplateAction(label="0", text="數量（大）：0", data='NUM&0')),
                QuickReplyButton(action=PostbackTemplateAction(label="1", text="數量（大）：1", data='NUM&1')),
                QuickReplyButton(action=PostbackTemplateAction(label="2", text="數量（大）：2", data='NUM&2')),
                QuickReplyButton(action=PostbackTemplateAction(label="3", text="數量（大）：3", data='NUM&3')),
                QuickReplyButton(action=PostbackTemplateAction(label="4", text="數量（大）：4", data='NUM&4')),
                QuickReplyButton(action=PostbackTemplateAction(label="5", text="數量（大）：5", data='NUM&5')),
                QuickReplyButton(action=PostbackTemplateAction(label="6", text="數量（大）：6", data='NUM&6')),
                QuickReplyButton(action=PostbackTemplateAction(label="7", text="數量（大）：7", data='NUM&7')),
                QuickReplyButton(action=PostbackTemplateAction(label="8", text="數量（大）：8", data='NUM&8')),
                QuickReplyButton(action=PostbackTemplateAction(label="9", text="數量（大）：9", data='NUM&9')),
                QuickReplyButton(action=PostbackTemplateAction(label="10", text="數量（大）：10", data='NUM&10'))
            ])
        )

        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='抱歉，革命失敗，請再試一次'))


def send_back_grade(event):
    try:
        message = TextSendMessage(
            text='同志是哪個年級？',
            quick_reply=QuickReply(items=[
                QuickReplyButton(action=PostbackTemplateAction(label="家長", text="年級：家長", data='GRADE&家長')),
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
        print("我要進來了小夫")
        # message = TextSendMessage(
        #     text='同志是哪個班級？',
            # quick_reply=QuickReply(items=[
            #     QuickReplyButton(action=PostbackTemplateAction(label="忠", text="班級：忠", data='NUM&1')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="孝", text="班級：孝", data='NUM&2')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="仁", text="班級：仁", data='NUM&3')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="愛", text="班級：愛", data='NUM&4')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="信", text="班級：信", data='NUM&5')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="義", text="班級：義", data='NUM&6')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="和", text="班級：和", data='NUM&7')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="平", text="班級：平", data='NUM&8')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="智", text="班級：智", data='NUM&9')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="勇", text="班級：勇", data='NUM&10')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="誠", text="班級：誠", data='NUM&11')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="正", text="班級：正", data='NUM&12')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="勤", text="班級：勤", data='NUM&13')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="齊", text="班級：齊", data='NUM&14'))
            # ])
            # quick_reply=QuickReply(items=[
            #     QuickReplyButton(action=PostbackTemplateAction(label="1", text="數量（大）：1", data='NUM&1')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="2", text="數量（大）：2", data='NUM&2')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="3", text="數量（大）：3", data='NUM&3')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="哈", text="數量（大）：4", data='NUM&4')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="5", text="數量（大）：5", data='NUM&5')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="6", text="數量（大）：6", data='NUM&6')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="7", text="數量（大）：7", data='NUM&7')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="8", text="數量（大）：8", data='NUM&8')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="9", text="數量（大）：9", data='NUM&9')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="10", text="數量（大）：10", data='NUM&10')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="10", text="數量（大）：10", data='NUM&10')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="10", text="數量（大）：10", data='NUM&10')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="10", text="數量（大）：10", data='NUM&10')),
            #     QuickReplyButton(action=PostbackTemplateAction(label="10", text="數量（大）：10", data='NUM&10'))
            # ]))
        message = TextMessage(
            text="同志是哪個班級？（範例：「班級：忠」）",
        )
        
        line_bot_api.reply_message(event.reply_token, message)
        print("send_back_class")
    except:
        message = TextSendMessage(text='抱歉，革命失敗，請再試一次')
        line_bot_api.reply_message(event.reply_token, message)
        print("笑爛")

def send_back_number(event):
    try:
        message = TextSendMessage(text='同志的座號是？（範例：「座號：1」）')
        line_bot_api.reply_message(event.reply_token, message)
    except:
        message = TextSendMessage(text='抱歉，革命失敗，請再試一次')
        line_bot_api.reply_message(event.reply_token, message)

def send_back_name(event):
    try:
        message = TextSendMessage(text='同志的名字是？（範例：「姓名：弗拉迪米爾·列寧」）')
        line_bot_api.reply_message(event.reply_token, message)
    except:
        message = TextSendMessage(text='抱歉，革命失敗，請再試一次')
        line_bot_api.reply_message(event.reply_token, message)

def send_back_pos(event):
    try:
        message = TextSendMessage(text='同志要送去哪裡？（範例：「位置：校門口」）')
        line_bot_api.reply_message(event.reply_token, message)
    except:
        message = TextSendMessage(text='抱歉，革命失敗，請再試一次')
        line_bot_api.reply_message(event.reply_token, message)

def send_back_note(event):
    try:
        message = TextSendMessage(text='同志有什麼話要說？（範例：「備註：找一位有帶紅色帽子的」、「備註：無」）')
        line_bot_api.reply_message(event.reply_token, message)
    except:
        message = TextSendMessage(text='抱歉，革命失敗，請再試一次')
        line_bot_api.reply_message(event.reply_token, message)

def send_back_confirm(event, amount_m, amount_l) -> int:
    '''
    send back sum: int, -1 for error
    '''
    try:
        bought = []
        sum = 0
        # TODO amount_l
        for name, value in db.how_much_m(amount_m).items():
        # for name, value in {'「我」的': {'amount': 3, 'price': 120}}:
            bought.append(TextComponent(text = name + ' × ' + str(value['amount']) + '＝' + '$' + str(value["price"]) + '\n'))
            sum += value["price"]
        for name, value in db.how_much_l(amount_l).items():
        # for name, value in {'「我」的': {'amount': 3, 'price': 120}}:
            bought.append(TextComponent(text = name + ' × ' + str(value['amount']) + '＝' + '$' + str(value["price"]) + '\n'))
            sum += value["price"]
        print("check(send_back_confirm)")
        #TODO
        bought.append(TextComponent(text = '總價：' + str(sum) + '\n'))
        bought.append(TextComponent(
                        text = "※由於園遊券最小面額為$5\n　應付價格可能與總價有出入",
                        color="#C8BCC3",
                        size="xs",
                        margin='xs'
                        ))
        if sum % 5 != 0:
            sum =(sum//5 + 1) * 5

        bought.append(TextComponent(text = '應付價格：' + str(sum) + '\n', weight='bold'))

        bubble = BubbleContainer(
            direction='ltr',
            header = BoxComponent(
                layout='vertical',
                #background_color='#DBD3D8',
                contents=bought
                ),
            footer=BoxComponent(
                layout='vertical',
                spacing='xs',
                contents=[
                    BoxComponent(
                        layout='horizontal',
                        spacing='xs',
                        contents=[
                            ButtonComponent(
                                style='secondary',
                                color="#E8F1E4",
                                action=PostbackTemplateAction(
                                    label='取消',
                                    text='取消',
                                    data='H'
                                )
                                )
                            # ButtonComponent(
                            #     style='secondary',
                            #     color="#C4DABB",
                            #     action=PostbackTemplateAction(
                            #         label='繼續購物',
                            #         text='繼續購物',
                            #         data='G'
                            #     )
                            #     )
                            
                            ]
                        
                        ),
                    ButtonComponent(
                        style='secondary',
                        color="#F6DCCB",
                        action=PostbackTemplateAction(
                            label='送出',
                            text='送出',
                            data='F'
                        )
                        
                        )
                    
                    ]
                )
            
            )
        
        message = FlexSendMessage(alt_text="確認訂單",contents=bubble)
        line_bot_api.reply_message(event.reply_token,message)
        return sum
    except:
        message = TextSendMessage(text='抱歉，革命失敗，請再試一次(from send_back_confirm)')
        #TODO
        line_bot_api.reply_message(event.reply_token, message)
        return -1
