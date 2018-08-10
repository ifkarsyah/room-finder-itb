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

line_bot_api = LineBotApi('YOUR-CHANNEL-ACCESS-TOKEN')
handler = WebhookHandler('YOUR-CHANNEL-SECRET')


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
		 '9019' : 'Oktagon Lantai II',
         '9020' : 'Oktagon Lantai II',
         '9021' : 'Oktagon Lantai II',
         '9025' : 'Oktagon Lantai II',
         '9026' : 'Oktagon Lantai II',
         '9027' : 'Oktagon Lantai II',
         '9022' : 'TVST Lantai I',
         '9023' : 'TVST Lantai I',
         '9024' : 'TVST Lantai I',
         'TVST - A': 'TVST Lantai II',
         'TVST - B': 'TVST Lantai II',
         'TVST - C': 'TVST Lantai II',
         '9103': 'GKU Barat Lantai I',
         '9104': 'GKU Barat Lantai I',
         '9107': 'GKU Barat Lantai I',
         '9108': 'GKU Barat Lantai I',
         '9114': 'GKU Barat Lantai II',
         '9115': 'GKU Barat Lantai II',
         '9116': 'GKU Barat Lantai II',
         '9121': 'GKU Barat Lantai II',
         '9122': 'GKU Barat Lantai II',
         '9124': 'GKU Barat Lantai II',
         '9125': 'GKU Barat Lantai II',
         '9126': 'GKU Barat Lantai II',
         '9127': 'GKU Barat Lantai II',
         '9128': 'GKU Barat Lantai II',
         '9131': 'GKU Barat Lantai III',
         '9132': 'GKU Barat Lantai III',
         '9133': 'GKU Barat Lantai III',
         '9134': 'GKU Barat Lantai III',
         '9135': 'GKU Barat Lantai III',
         '9136': 'GKU Barat Lantai III',
         '9137': 'GKU Barat Lantai III',
         '9138': 'GKU Barat Lantai III',
         '9213': 'GKU Timur Lantai II',
         '9214': 'GKU Timur Lantai II',
         '9221': 'GKU Timur Lantai III',
         '9222': 'GKU Timur Lantai III',
         '9223': 'GKU Timur Lantai III',
         '9224': 'GKU Timur Lantai III',
         '9231': 'GKU Timur Lantai IV',
         '9232': 'GKU Timur Lantai IV',
         '9233': 'GKU Timur Lantai IV',
         '9234': 'GKU Timur Lantai IV',
         '9301': 'Labtek V',
         '9302': 'Labtek V',
         '9303': 'Labtek V',
         '9304': 'Labtek V',
         '9305': 'Labtek V',
         '9306': 'Labtek V',
         '9315': 'Labtek V',
         '9307': 'Labtek VI',
         '9308': 'Labtek VI',
         '9309': 'Labtek VI',
         '9311': 'Labtek VI',
         '9312': 'Labtek VI',
         '9313': 'Labtek VI',
         '9314': 'Labtek VI',
         '9401': 'Labtek I Lantai II',
         '9402': 'Labtek I Lantai II',
         '9404': 'Labtek I Lantai II',
         '9405': 'Labtek I Lantai II',
         'BSC - A': 'Basic Science A Lantai IV',
         }
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
