import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO, 
                    format="%(asctime)s %(levelname)s %(message)s")  # Запись логов информационного уровня в файл

def greet_user(update, context):
    user = update.message.chat.first_name
    print("update", update)
    print("Вызван /start")
    update.message.reply_text(f'Привет, {user}! Ты вызвал(а) команду /start.\nНапиши что-нибудь, а я повторю.')

def talk_to_me(update, context):
    user_text = update.message.text  # Фиксирование сообщения пользователя 
    user = update.message.chat.first_name
    print(user_text)
    update.message.reply_text(f'Твое сообщение:\n{user_text}')  # Дублирование user_text ботом
    

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
