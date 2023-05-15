import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO, 
                    format="%(asctime)s %(levelname)s %(message)s")  # Запись логов информационного уровня в файл

def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def talk_to_me(update, context):
    user_text = update.message.text  # Фиксирование сообщения пользователя 
    print(user_text)
    update.message.reply_text(user_text)  # Дублирование user_text ботом

def main():
    mybot = Updater(settings.API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))  # Назначение функции на команду /start
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))  # Назначение функции на текстовые сообщения

    logging.info("Бот стартовал")
    mybot.start_polling()  # Проверка ботом обновлений
    mybot.idle()  # Постоянная работа бота

if __name__ == "__main__":
    main()
