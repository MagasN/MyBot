import logging
import ephem
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime

logging.basicConfig(filename='bot.log', level=logging.INFO, 
                    format="%(asctime)s %(levelname)s %(message)s")  # Запись логов информационного уровня в файл

def greet_user(update, context):
    user_name = update.message.chat.first_name
    #print("update", update)
    print("Вызван /start")
    update.message.reply_text(f"Привет, {user_name}!"
                              f" Ты вызвал(а) команду /start.\nНапиши что-нибудь, а я повторю.\n"
                              f"Или введи /planet <Название планеты>.")

def talk_to_me(update, context):
    user_text = update.message.text  # Фиксирование сообщения пользователя 
    print(user_text)
    update.message.reply_text(f'Твое сообщение:\n{user_text}')  # Дублирование user_text ботом 

def planet_stars(update, context):
    print("Вызван /planet")
    update.message.reply_text("Введи, например, /planet Venus и я скажу в каком созвездии сегодня находится планета.")

    message_user = update.message.text.split()[1].lower()
    dt_now = datetime.now()
    dt_format = dt_now.strftime('%Y/%m/%d')
    
    if message_user =='venus':
        update.message.reply_text(f'Venus: {(ephem.constellation(ephem.Venus(dt_format))[1])}')
    elif message_user == 'mars':
        update.message.reply_text(f'Mars: {(ephem.constellation(ephem.Mars(dt_format))[1])}')
    elif message_user == 'mercury':
         update.message.reply_text(f'Mercury: {(ephem.constellation(ephem.Mercury(dt_format))[1])}')
    elif message_user == 'jupiter':
        update.message.reply_text(f'Jupiter: {(ephem.constellation(ephem.Jupiter(dt_format))[1])}')
    elif message_user == 'saturn':
         update.message.reply_text(f'Saturn: {(ephem.constellation(ephem.Saturn(dt_format))[1])}')
    elif message_user == 'uranus':
         update.message.reply_text(f'Uranus: {(ephem.constellation(ephem.Uranus(dt_format))[1])}')
    elif message_user == 'neptune':
         update.message.reply_text(f'Eptune: {(ephem.constellation(ephem.Neptune(dt_format))[1])}')
    elif message_user == 'pluto':
         update.message.reply_text(f'Pluto: {(ephem.constellation(ephem.Pluto(dt_format))[1])}')
    else:
        update.message.reply_text("Укажи планету солнечной системы на английском.")

def main():
    mybot = Updater(settings.API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))  # Назначение функции на команду /start
    dp.add_handler(CommandHandler("planet", planet_stars))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))  # Назначение функции на текстовые сообщения

    logging.info("Бот стартовал")
    mybot.start_polling()  # Проверка ботом обновлений
    mybot.idle()  # Постоянная работа бота



if __name__ == "__main__":
    main() 
