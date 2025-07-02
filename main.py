from telebot import TeleBot, types

bot = TeleBot("8013845194:AAHOo7ZxpUNRyMhKiHB_FAV6nGBl3YtO1SA")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🎁 Открыть подарок")
    markup.add(btn1)
    bot.send_message(
        message.chat.id,
        "Привет! Бот работает 24/7. Жми кнопку ниже, чтобы открыть подарок 🎁",
        reply_markup=markup
    )

@bot.message_handler(func=lambda msg: msg.text == "🎁 Открыть подарок")
def open_gift(message):
    bot.send_message(message.chat.id, "Вы открыли подарок! 🎉")

bot.polling()
