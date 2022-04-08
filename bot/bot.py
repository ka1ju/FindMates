import telebot

token = '5233800397:AAFgdr9-7tk4HkTcsFzUCspJ-erxRaw22E8'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")


bot.infinity_polling()
