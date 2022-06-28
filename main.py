import telebot
from telebot import types
import time
x = int(time.time())

BOT_TOKEN = place_your_token_here
bot = telebot.TeleBot('TOKEN')

# Функция рандом
def random(a=6364136223846793005, c=1442695040888963407, m=2 ** 64):
    global x
    x = (a * x + c) % m
    return x

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, любишь котиков?')

@bot.message_handler(commands=['developer'])
def developer(message):
    bot.send_message(message.chat.id, 'По вопросам и пожеланиям к боту пишите сюда --> @duratk')

# Функция, которая выдает рандомные картинки
@bot.message_handler(commands=['kot'])
def commands(message):
    num_rand = random() % 10 + 1
    if num_rand == 1:
        photo = open('nya.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption='Ну, кто из вас лучше всех чешет за ушком?')
    elif num_rand == 2:
        photo = open('hah.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption='Сегодня мы очень плохие! Мяу~')
    elif num_rand == 3:
        photo = open('sleep.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption='*зевает* Опять надо спасать друзей, да?')
    elif num_rand == 4:
        photo = open('kysb.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption='Вкусно пахнешь! Ты с рыбалки?')
    elif num_rand == 5:
        photo = open('hi.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption='Я люблю обнимашки. Только никому не говори!')
    elif num_rand == 6:
        photo = open('strawberry.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption='Я буду на тебе греться.')
    elif num_rand == 7:
        photo = open('glasses.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption='Кошки – прекрасные компаньоны! Спросите мою хозяйку...которая пропала при загадочных обстоятельствах.')
    elif num_rand == 8:
        photo = open('player.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption='Только не урони меня...только не урони меня!')
    elif num_rand == 9:
        photo = open('bow.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption='Не волнуйся, я тебя ни за что не брошу!')
    else:
        photo = open('went.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption='Умелая охотница неслышно подкрадывается к добыче.')

@bot.message_handler(commands=['commands'])
def command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kot = types.KeyboardButton('/kot')
    markup.add(kot)
    bot.send_message(message.chat.id, 'На кнопках предсдставлены все команды, которые на данный момент имеются<3', reply_markup=markup)

@bot.message_handler(commands=['help'])
def helper(message):
    markup = types.ReplyKeyboardMarkup()
    developer = types.KeyboardButton("/developer")
    command = types.KeyboardButton('/commands')
    markup.add(developer, command)
    bot.send_message(message.chat.id, 'Этот бот создан для понятия настроения каждому сюда входящему. Нектороые фразы я взяла из лиги легенд - персонаж "Юми".', reply_markup=markup)

@bot.message_handler()
def get_user_text(message):
    txt = message.text.lower()
    if txt.find('да') != -1:
        bot.send_message(message.chat.id, 'Замечательно! Я думаю мы с тобой поладим.')
    elif txt.find('нет') != -1:
        photo = open('bye.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю!')



bot.infinity_polling(none_stop=True)
