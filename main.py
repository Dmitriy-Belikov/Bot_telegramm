import telebot
import random
from telebot import types

bot = telebot.TeleBot('')
# Загружаем список интересных фактов
f = open('compliment.txt', 'r', encoding='UTF-8')
compliment = f.read().split('\n')
f.close()


# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    # Добавляем две кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Песня")
    item2 = types.KeyboardButton("Комплимент")
    markup.add(item1)
    markup.add(item2)
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Песня', callback_data='Песня'); #кнопка «Да»
    keyboard.add(key_yes); #добавляем кнопку в клавиатуру
    key_no= types.InlineKeyboardButton(text='Комплимент', callback_data='Комплимент');
    keyboard.add(key_no);

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему песню
    if message.text.strip().lower() == 'песня':
        answer = open('music/Bon Jovi Bed Of Roses.mp3', 'rb')
        #answer = random.choice(music)
    # Если юзер прислал 2, выдаем комплимент
    elif message.text.strip().lower() == 'комплимент':
        answer = random.choice(compliment)
    else:
        answer = 'Я не понял'
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)


# Запускаем бота
bot.polling(none_stop=True, interval=0)
