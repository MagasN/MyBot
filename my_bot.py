import logging
import settings
from datetime import datetime
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(filename='bot.log', level=logging.INFO, 
                    format="%(asctime)s %(levelname)s %(message)s")  # Запись логов информационного уровня в файл

def greet_user(update, context):
    user_name = update.message.chat.first_name
    #print("update", update)
    print("Вызван /start")
    
    message_to_user = (f"Привет, {user_name}! "
                      f"Ты вызвал(а) команду /start.\nНапиши что-нибудь, а я повторю.\n"
                      f"Или введи /planet <Название планеты на английском>.")
    
    update.message.reply_text(message_to_user)

def talk_to_me(update, context):
    user_text = update.message.text  # Фиксирование сообщения пользователя 
    print(user_text)
    update.message.reply_text(f'Твое сообщение:\n{user_text}')  # Дублирование user_text ботом 

def planet_stars(update, context):
    print("Вызван /planet")

    planets = [name_planet[2] for name_planet in ephem._libastro.builtin_planets()]  # Список планет
    
    try:       
        planet_user = update.message.text.split()[1].capitalize()
            
        if hasattr(ephem, planet_user):
            name_planet = getattr(ephem, planet_user)(datetime.now())  # 
            update.message.reply_text(f'{planet_user} в созвездии {ephem.constellation(name_planet)[1]}')
        else:
            update.message.reply_text("К сожалению, я не знаю такой планеты. Попробуй еще раз.")
    
    except IndexError:
        update.message.reply_text("Введи, например, /planet Venus, а я скажу в каком созвездии сегодня находится планета.")

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
