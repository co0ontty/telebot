import telebot

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['help'])
def send_help(message):
        bot.reply_to(message, "help - 获取帮助\nstart - 开启复读机")

@bot.message_handler(commands=['start'])
def send_start(message):
        bot.reply_to(message, "开启复读机")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)


bot.polling()