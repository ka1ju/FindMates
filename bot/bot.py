import telebot
from aiogram import types

token = '5233800397:AAFgdr9-7tk4HkTcsFzUCspJ-erxRaw22E8'
bot = telebot.TeleBot(token)

k = 0

messages = \
    ['On this screen u can see the main navigation buttons of my app\n\n'
     'News button redirects u to the news page, where u can read news, posted by admins of my web-site.\n'
     'Find mates button redirects u to the page, where u can see another registered users.\n'
     'Profile redirects u to the page, where u can login to ur profile, and view it after logging in.',

     'On this screen u can see news page. \n\n'
     'How was sad before here u can read news, what are posted by our admins.'
     'https://find-mates.herokuapp.com/news',

     'Here u can see page, where u can find teammates. \n\n'
     'Every user have discord and steam profile link, so u can use in to contact with them, '
     'if u think that they correspond to ur criteria.'
     'https://find-mates.herokuapp.com/find_mates',

     'This is the login form.\n\n'
     "U can login on our site after register. U can register on the register form, "
     "what you'll see,on the next screenshot"
     "https://find-mates.herokuapp.com/login",

     'Here is it - register form.\n\n'
     'In it u need provide information about u. After it u need to click confirm button. Now u are registered.'
     'https://find-mates.herokuapp.com/login',

     'After register u may return to the login form, and log into your account. '
     'After it you will see your profile.\n\n'
     'Now, here u can check your information out and logout.'
     'https://find-mates.herokuapp.com/login']


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_btn = types.KeyboardButton(text="/🏎️")
    keyboard.add(start_btn)
    bot.send_message(message.chat.id, '👋')
    bot.send_message(message.chat.id,
                     "Hello. I'm FindMates telegram-bot.\n "
                     "\n "
                     "I'm here to help u in using our WEB-site and now i'll "
                     "give u screenshots with explanation, how to use it.", reply_markup=[keyboard])


@bot.message_handler(commands=["🏎️"])
def next_image(message):
    global k
    """file = open('img/00.png', 'rb')
    bot.send_photo(message.chat.id, photo=file, caption=messages[k])"""
    bot.send_message(message.chat.id, messages[k])
    k += 1
    k %= 6


bot.infinity_polling()
