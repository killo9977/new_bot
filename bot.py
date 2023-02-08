import telebot
from telebot import TeleBot
from telebot import types
import os
from dotenv import load_dotenv
import datetime

import asyncio

load_dotenv()
#bot API
API = os.getenv('API_KEY')
#admin tg-ID
Admin_telegram_ID = os.getenv('Admin_telegram_ID')
userID = ""

bot = telebot.TeleBot(API)

# messages
start_message = """
〰️〰️〰️〰️〰️〰️〰️〰️〰️
⚜️Dear Friend

Please select one of these buttons👇🏻
ከተዘረዘሩት ቁልፎች አንዱን ይጫኑ👇

ለጥያቄ እና ተጨማሪ መረጃ ፡ https://t.me/itshenok1
ይህን Link ይጠቀሙ

〰️〰️〰️〰️〰️〰️〰️〰️〰️
"""

billing_info ="""
💳 Billing 🔰🔰🔰🔰🔰🔰🔰

Payment amount: 100.00+ birr
100 ብር እና ከዛም በላይ
____________________

ከታች በተዘረዘሩት የሂሳብ ቁጥሮች 100 ብር እና ከዛም በላይ በማስገባት አገልግሎቱን በመደገፍ የልቤ ጌታ የተሰኘውን የዘማሪት ህሊና ዳዊትን ሙሉ አልበም ማግኘት ይችላሉ!

ገቢ ካደረጉ በኋላ Screenshot ወይም ፎቶ ይላኩ 
ንግድ ባንክ፡ 1000353787164
ብርሀን ባንክ፡ 100078733905
ዳሽን ባንክ፡ 5044102309011
አዋሽ ባንክ፡ 01347521716200253

ጌታ ዘመናችሁን ይባርክ!

ለጥያቄ https://t.me/itshenok1
〰️〰️〰️〰️〰️〰️〰️〰️  
 
🔴 Please After payment, send your receipt image by clicking on submit receipt button

.
"""


verified_message = """
🎖 Dear Customer
ጥያቄዎ በትክክል ተስተናግዷል!
The payment has been confirmed successfully
📆Your membership is valid until  30/12/2043 
Click to enter the channel👇🏽
"""


bot_info = """
〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️
*********** INFO ************
〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️

ከታች በተዘረዘሩት የሂሳብ ቁጥሮች 100 ብር እና ከዛም በላይ በማስገባት አገልግሎቱን በመደገፍ የልቤ ጌታ የተሰኘውን የዘማሪት ህሊና ዳዊትን ሙሉ አልበም ማግኘት ይችላሉ!

ገቢ ካደረጉ በኋላ Screenshot ወይም ፎቶ ይላኩ 
ንግድ ባንክ፡ 1000353787164
ብርሀን ባንክ፡ 100078733905
ዳሽን ባንክ፡ 5044102309011
አዋሽ ባንክ፡ 01347521716200253

ጌታ ዘመናችሁን ይባርክ!

ጌታ ዘመናችሁን ይባርክ!
〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️
〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️

"""
bot_help = """
〰️〰️〰️〰️〰️〰️〰️〰️〰️
>>>>>>>   🆘HELP🆘  <<<<<<<
〰️〰️〰️〰️〰️〰️〰️〰️〰️

Available Commands

/start 

/Help

/Buy_Albums

/Info

/GetAccountNumber

/submit_receipt

/back
〰️〰️〰️〰️〰️〰️〰️〰️〰️
〰️〰️〰️〰️〰️〰️〰️〰️〰️
〰️〰️〰️〰️〰️〰️〰️〰️〰️
"""


print("Bot Started...")
try:
  def accept():
    bot.send_message(Admin_telegram_ID, "Enter User id and channel link")
    @bot.message_handler(content_types=['text'])
    def smtc(message):
      idlink = message.text.split(" ")
      try:
        link_btn = types.InlineKeyboardButton('🔗Channel link',  url=idlink[1])
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(link_btn)
        bot.send_message(idlink[0], text=verified_message, reply_markup=keyboard)
        bot.reply_to(message, "link successfuly sent to user ID: {}".format(idlink[0]))
      except:
        accept()
  
  # /start
  @bot.message_handler(commands=['start', 'start▶️','back', 'back⬅️'])
  def start(message):
    markup = types.ReplyKeyboardMarkup()
    start_btn = types.KeyboardButton('/start▶️')
    buyAlbum_btn = types.KeyboardButton('/Buy_Albums💰')
    info_btn = types.KeyboardButton('/Info📝')
    help_btn = types.KeyboardButton('/Help🆘')
    markup.row(start_btn)
    markup.row(info_btn, help_btn)
    markup.row(buyAlbum_btn)
    bot.send_message(message.chat.id, start_message, reply_markup=markup)
    # buy albums
  @bot.message_handler(commands=['Buy_Albums','Buy_Albums💰'])
  def info(message):
    markup = types.ReplyKeyboardMarkup()
    bank_btn = types.KeyboardButton('/GetAccountNumber💳')
    buy_btn = types.KeyboardButton('/submit_receipt📃')
    back_btn = types.KeyboardButton('/back⬅️')
    markup.row(bank_btn)
    markup.row(buy_btn)
    markup.row(back_btn)
    
    bot.send_message(message.chat.id, "Payment Options", reply_markup=markup)
    @bot.message_handler(commands=['GetAccountNumber', 'GetAccountNumber💳'])
    def info(message):
      bot.reply_to(message, billing_info)
    # submit_receipt
    @bot.message_handler(commands=['submit_receipt','submit_receipt📃'])
    def sendDataToAdmin(message):
      username = message.from_user.first_name
      buyAlbum_message = """
⚜️Dear {},

📍Send payment screenshot:
  """.format(username)

      bot.send_message(message.chat.id, buyAlbum_message)
      @bot.message_handler(content_types=['photo'])
      def photo(message):
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        with open("image.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_photo(chat_id=Admin_telegram_ID, photo=open('image.jpg', 'rb'))
        bot.reply_to(message, "receipt recieved..")
        accept_btn = types.InlineKeyboardButton('✅Accept', callback_data='accept')
        decline_btn = types.InlineKeyboardButton('❌Decline', callback_data='decline')
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(accept_btn)
        keyboard.add(decline_btn)

        user = message.from_user.first_name
        date = datetime.datetime.now()
        cid = message.chat.id
        paymentInformation = """
  📬 New Request recieved
  #Request_Buy_Full_Album
  📝 Request title: 💰 buy album
  📅 Request date: {}
  📎 Request information
  〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️

  📌 Username: {}
  📌 Chat ID: {}
  〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️
  🚧 End request information
            
        """.format(date,user,cid)
        bot.send_message(Admin_telegram_ID, text=paymentInformation, reply_markup=keyboard)
        bot.send_message(message.chat.id, "Please wait for admin's response...")

  # info
  @bot.message_handler(commands=['Info', 'Info📝'])
  def info(message):
    bot.send_message(message.chat.id, bot_info)
    
  # help
  @bot.message_handler(commands=['Help🆘', 'Help'])
  def info(message):
    bot.send_message(message.chat.id, bot_help)


 # accept
  @bot.callback_query_handler(lambda query: query.data == "accept")
  def process_callback(query):
    accept()
  @bot.callback_query_handler(lambda query: query.data == "decline")
  def process_callback(query):
    bot.send_message(Admin_telegram_ID, "Declined")
  bot.polling()
except Exception as e:
  print(e)

