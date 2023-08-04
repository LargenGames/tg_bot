import telebot as tg
import time


bot = tg.TeleBot('6612317897:AAG7VaFOIfkhSclQuMI5hq4tfboECQZe-DQ')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Я бот, который может отправить тебе сообщение через заданное время.')


@bot.message_handler(commands=['send'])
def send_delayed_message(message):
    chat_id = message.chat.id
    delay = message.text.split(' ', 1)[1]

    try:
        seconds = int(delay)

        if seconds > 0:
            time.sleep(seconds)
            bot.send_message(chat_id, 'Привет! Это сообщение отправлено через заданное тобой количество секунд.')
        else:
            bot.send_message(chat_id, 'Укажите положительное количество секунд.')

    except ValueError:
        bot.send_message(chat_id, 'Неверный фо.рмат. Пожалуйста, введите целое число секунд.')


bot.polling()