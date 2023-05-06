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

def deliver():
    message = TemplateSendMessage(
        alt_text='美乃滋？',
        template = ButtonsTemplate( 
            thumbnail_image_url="https://photoos.mac89.com/EPS180507/180507_203/dZAn5ItFQT_small.jpg",
            title='choice',
            text='請問需不需要美乃滋？',
            actions=[
                PostbackTemplateAction(
                    label='要',
                    text='要',
                    data='action=要'
                ),
                PostbackTemplateAction(
                    label='不要',
                    text='不要',
                    data='action=不要'
                )
            ]
        )
            
        )

def send_back_class(event):
    try:
        message = TextSendMessage(
            text='同志是哪個班級？',
            quick_reply=QuickReply(items=[
                QuickReplyButton(action=PostbackTemplateAction(label="7", text="七", data='CLASS&' + num + '&4')),
                QuickReplyButton(action=PostbackTemplateAction(label="8", text="八", data='CLASS&' + num + '&5')),
                QuickReplyButton(action=PostbackTemplateAction(label="9", text="九", data='CLASS&' + num + '&6')),
                QuickReplyButton(action=PostbackTemplateAction(label="1", text="一", data='CLASS&' + num + '&1')),
                QuickReplyButton(action=PostbackTemplateAction(label="2", text="二", data='CLASS&' + num + '&2')),
                QuickReplyButton(action=PostbackTemplateAction(label="3", text="三", data='CLASS&' + num + '&3')),
                
            ]))
        
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='不買'))