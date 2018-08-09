import os
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

line_bot_api = LineBotApi('')
handler = WebhookHandler('')


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
#########################################################
carapake = 'Bot ini dapat digunakan untuk mencari nama bangunan dari input kode ruangan yang kalian masukkan. Misal, kalian memasukkan input \"9127\", bot ini akan membalas dengan \"GKU Barat Lantai 2\". Ketik \"tutorial\" untuk lihat penggunaan.'

########################################################################################################
def balas(event, balasan):
	line_bot_api.reply_message(
		event.reply_token, 
		TextSendMessage(text=balasan))

########################################################################################################
ruang = {'9009' : 'LFM Lantai I', 
		 '9011' : 'Labtek VIII Lantai II',
		 '9012' : 'Labtek VII',
		 '9013' : 'Labtek VII',
		 '9014' : 'Labtek VII',
		 '9015' : 'Labtek VIII Lantai II',
		 '9016' : 'Oktagon Lantai I',
		 '9017' : 'Oktagon Lantai I',
		 '9018' : 'Oktagon Lantai I',
		 '9019' : 'Oktagon Lantai II',}
########################################################################################################
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	pesan = event.message.text
	if (pesan in ruang):
		balas(event, ruang[pesan])
	elif (pesan == 'tutorial'):
		balas(event, carapake)
	else:
		balas(event, 'Kode ruangan salah, masukkan kode ruangan yang benar!')
    

########################################################################################################

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
