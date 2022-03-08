import os 
import telebot
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)



@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    user_id = message.from_user.id
    username = message.from_user.username
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Apple',callback_data='apple')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Samsung',callback_data='samsung')
    )    
        
    
    bot.send_message(message.chat.id,'Выберите бренд',reply_markup=keyboard)




   


@bot.callback_query_handler(func=lambda call: True)
def char_message(message):
    id = message.id
    if 'apple' == message.data:
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('iPhone11',callback_data='iPhone 11'),
            telebot.types.InlineKeyboardButton('iPhone11Pro',callback_data='iPhone 11pro'),
            telebot.types.InlineKeyboardButton('iPhone11ProMax',callback_data='iPhone 11ProMax')
            )
        keyboard.row(
            telebot.types.InlineKeyboardButton('iPhone12',callback_data='iPhone 12'),
            telebot.types.InlineKeyboardButton('iPhone12Pro',callback_data='iPhone 12Pro'),
            telebot.types.InlineKeyboardButton('iPhone12ProMax',callback_data='iPhone 12ProMax'),
            )
        keyboard.row(
            telebot.types.InlineKeyboardButton('iPhone13',callback_data='iPhone13'),
            telebot.types.InlineKeyboardButton('iPhone13Pro',callback_data='iPhone 13Pro'),
            telebot.types.InlineKeyboardButton('iPhone13ProMax',callback_data='iPhone 13ProMax')
            )
        
        keyboard.row(
            telebot.types.InlineKeyboardButton('iphone12mini',callback_data='iPhone 12mini'),
            telebot.types.InlineKeyboardButton('iPhone 13mini',callback_data='iPhone 13mini')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад',callback_data='to_brand_list')
            ) 
    

        bot.edit_message_text(text='Выберите телефон', chat_id=message.message.chat.id, message_id=message.message.id)
        bot.edit_message_reply_markup(chat_id=message.message.chat.id, message_id=message.message.id, reply_markup=keyboard)
    
    if 'samsung' == message.data:
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Galaxy A',callback_data='GalaxyA')
        )

        keyboard.row(
            telebot.types.InlineKeyboardButton('Galaxy M',callback_data='GalaxyM')
        )
        
        keyboard.row(
            telebot.types.InlineKeyboardButton('Galaxy S',callback_data='GalaxyS')
        )
        
        
        
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад',callback_data='to_brand_list')
            ) 

        bot.edit_message_text(text='Выберите телефон', chat_id=message.message.chat.id, message_id=message.message.id)
        bot.edit_message_reply_markup(chat_id=message.message.chat.id, message_id=message.message.id, reply_markup=keyboard)        

    #Тут apple
    elif 'iPhone 11' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://i.ibb.co/SJTp64t/iphn11.png',caption='Характеристики 11',reply_markup=keyboard)

    elif 'iPhone 11pro' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/1M3wAz1FxFMCGw',caption='Характеристики 11Pro',reply_markup=keyboard)

    elif 'iPhone 11ProMax' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/ZVRq6-425T4k-w',caption='Характеристики 11ProMax',reply_markup=keyboard)


    elif 'iPhone 12' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://i.ibb.co/7bBfdM3/iphone12.png',caption='Характеристики 12',reply_markup=keyboard)
    
    elif 'iPhone 12Pro' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://i.ibb.co/cgnjHzq/iphone12pro.png',caption='Характеристики 12 Pro',reply_markup=keyboard)

    elif 'iPhone 12ProMax' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://i.ibb.co/YpT136p/iphone12promax.png',caption='Характеристики 12 ProMax',reply_markup=keyboard)

    elif 'iPhone13' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://i.ibb.co/CVJKm71/iphone13.png',caption='Характеристики 13',reply_markup=keyboard)

    elif 'iPhone 13Pro' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://i.ibb.co/RcJNLWq/iphone13prozagruzispliz.png',caption='Характеристики 13Pro',reply_markup=keyboard)

    elif 'iPhone 13ProMax' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/v8-q-6LSjM_KTA',caption='Характеристики 13ProMax',reply_markup=keyboard)
    
    
    elif 'iPhone 12mini' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/VzPPSQQESvpoPQ',caption='Характеристики 12 mini',reply_markup=keyboard)
    
    elif 'iPhone 13mini' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/7T-Kzh7IeRiHQg',caption='Характеристики 13 mini',reply_markup=keyboard)
    
    #конец Apple

#Тут самсунги
    elif 'GalaxyA' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('GalaxyA03Core',callback_data='GalaxyA03Core')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('GalaxyA02',callback_data='GalaxyA02'),
            telebot.types.InlineKeyboardButton('GalaxyA02s',callback_data='GalaxyA02s'),
            telebot.types.InlineKeyboardButton('GalaxyA03s',callback_data='GalaxyA03s')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('GalaxyA12',callback_data='GalaxyA12'),
            telebot.types.InlineKeyboardButton('GalaxyA22',callback_data='GalaxyA22'),
            telebot.types.InlineKeyboardButton('GalaxyA22s',callback_data='GalaxyA22s')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('GalaxyA32',callback_data='GalaxyA32'),
            telebot.types.InlineKeyboardButton('GalaxyA52',callback_data='GalaxyA52'),
            telebot.types.InlineKeyboardButton('GalaxyA72',callback_data='GalaxyA72')
            
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )
    
        bot.edit_message_text(text='Выберите телефон', chat_id=message.message.chat.id, message_id=message.message.id)
        bot.edit_message_reply_markup(chat_id=message.message.chat.id, message_id=message.message.id, reply_markup=keyboard)

    elif 'GalaxyM' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('GalaxyM12',callback_data='GalaxyM12')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('GalaxyM22',callback_data='GalaxyM22')
            )
        keyboard.row(
            telebot.types.InlineKeyboardButton('GalaxyM32',callback_data='GalaxyM32')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('GalaxyM52',callback_data='GalaxyM52')
        )

        bot.edit_message_text(text='Выберите телефон', chat_id=message.message.chat.id, message_id=message.message.id)
        bot.edit_message_reply_markup(chat_id=message.message.chat.id, message_id=message.message.id, reply_markup=keyboard)


    elif 'GalaxyS' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('GalaxyS20FE',callback_data='GalaxyS20FE')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('GalaxyS21',callback_data='GalaxyS21')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('GalaxyS21+',callback_data='GalaxyS21+')
            )
        keyboard.row(
            telebot.types.InlineKeyboardButton('GalaxyS21Ultra',callback_data='GalaxyS21ultra')
        )
        # keyboard.row(
        #     telebot.types.InlineKeyboardButton('GalaxyM52',callback_data='GalaxyM52')
        # )

        bot.edit_message_text(text='Выберите телефон', chat_id=message.message.chat.id, message_id=message.message.id)
        bot.edit_message_reply_markup(chat_id=message.message.chat.id, message_id=message.message.id, reply_markup=keyboard)



    elif 'GalaxyA02' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/AxKTcXEgvJwoqA',caption='Характеристики Galaxy A02',reply_markup=keyboard)

    elif 'GalaxyA03Core' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/zkJq104MXfI7Tg',caption='Характеристики Galaxy A03Core',reply_markup=keyboard)    

    elif 'GalaxyA02s' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/G7oOcjcsvrOFLg',caption='Характеристики Galaxy A02s',reply_markup=keyboard)

    elif 'GalaxyA03s' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/Z9DU1SjFW5WpXw',caption='Характеристики Galaxy A03s',reply_markup=keyboard)

    elif 'GalaxyA12' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/DJ8EOT3yGoz6_g',caption='Характеристики Galaxy A12',reply_markup=keyboard)
    
    elif 'GalaxyA22' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/822SQ8TjCVzR3w',caption='Характеристики Galaxy A22',reply_markup=keyboard)
    
    elif 'GalaxyA22s' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/l8dMDgmD4N0m9A',caption='Характеристики Galaxy A22s',reply_markup=keyboard)

    elif 'GalaxyA32' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/d/U9CbL1w7sYndPQ',caption='Характеристики Galaxy A32',reply_markup=keyboard)

    elif 'GalaxyA52' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        # bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/d/qPMxzL4z8OvpRg',caption='Характеристики Galaxy A52',reply_markup=keyboard)

    elif 'GalaxyA72' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/TkxhuqOyfB6Nxg',caption='Характеристики Galaxy A72',reply_markup=keyboard)

    elif 'GalaxyM12' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/QjKefLEiS4OP3Q',caption='Характеристики Galaxy M12',reply_markup=keyboard)

    elif 'GalaxyM22' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/d/Cytl3VLlwo9pMA',caption='Характеристики Galaxy M22',reply_markup=keyboard)

    elif 'GalaxyM32' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/Ds0vGlXeY9AOnw',caption='Характеристики Galaxy M32',reply_markup=keyboard)    

    elif 'GalaxyM52' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/B0CZqdYC9QV6jw',caption='Характеристики Galaxy M52',reply_markup=keyboard)

    elif 'GalaxyS20FE' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/kXJE-sKaWHJWdA',caption='Характеристики Galaxy S20FE',reply_markup=keyboard)

    elif 'GalaxyS21' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/d/acHyi0VsesfNJg',caption='Характеристики Galaxy S21',reply_markup=keyboard)

    elif 'GalaxyS21+' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/DDiNiV1G4wPz_w',caption='Характеристики Galaxy S21+',reply_markup=keyboard)


    elif 'GalaxyS21ultra' == message.data:
        keyboard=telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Посмотреть другой телефон',callback_data='to_new_request')
        )

        bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.id)
        bot.send_photo(message.message.chat.id,photo='https://disk.yandex.ru/i/ILAgE7U9NKb96w',caption='Характеристики Galaxy S21+',reply_markup=keyboard)

    

    elif 'to_brand_list' == message.data:
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
        telebot.types.InlineKeyboardButton('Apple',callback_data='apple')
    )
        keyboard.row(
        telebot.types.InlineKeyboardButton('Samsung',callback_data='samsung')
    )    
        # keyboard.row( 
        # telebot.types.InlineKeyboardButton('Xiaomi',callback_data='xiaomi'),
        # telebot.types.InlineKeyboardButton('Huawei',callback_data='huawei'),
        # telebot.types.InlineKeyboardButton('Honor',callback_data='honor')
        # )
        bot.edit_message_text(chat_id=message.message.chat.id, text='Выберите бренд', message_id=message.message.id)
        bot.edit_message_reply_markup(chat_id=message.message.chat.id, message_id=message.message.id, reply_markup=keyboard)
    
    elif 'to_new_request' == message.data:
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
        telebot.types.InlineKeyboardButton('Apple',callback_data='apple')
    )
        keyboard.row(
        telebot.types.InlineKeyboardButton('Samsung',callback_data='samsung')
    )    
        # keyboard.row( 
        # telebot.types.InlineKeyboardButton('Xiaomi',callback_data='xiaomi'),
        # telebot.types.InlineKeyboardButton('Huawei',callback_data='huawei'),
        # telebot.types.InlineKeyboardButton('Honor',callback_data='honor')
        # )
        bot.send_message(chat_id=message.message.chat.id, text='Выберите бренд', reply_markup=keyboard)
        bot.edit_message_reply_markup(chat_id=message.message.chat.id, message_id=message.message.id, reply_markup=None)





@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    server.run(host='0.0.0.0',port=int(os.environ.get('PORT',5000)))

