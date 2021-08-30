import config
import random
import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
from telebot import types

bot = telebot.TeleBot("1865998813:AAGyN1Yvcdtpsr9OujQdFfkt-ebKrrS88eo")

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲Бросить кубик🎲")
    item2 = types.KeyboardButton("😊Как дела?😊")
    item3 = types.KeyboardButton("😂Анекдоты🤡")
    item4 = types.KeyboardButton("🌦Какая сейчас погода?☀️")
    item5 = types.KeyboardButton("❓FAQ❓")
 
    markup.add(item1, item2, item3, item4, item5)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, давай дружить? Если тебе будет одиноко, то скорее пиши мне 😊".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲Бросить кубик🎲':
            bot.send_message(message.chat.id, str(random.randint(1,6)))
      
           
        if message.text == '😊Как дела?😊':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'Все прекрасно, а как твои дела?😊', reply_markup=markup)
        #else:
         #   bot.send_message(message.chat.id, 'Пока могу поговорить только про твои дела 😢')
        if message.text == '🌦Какая сейчас погода?☀️':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item3 = types.InlineKeyboardButton("Страна", callback_data='country')
            item4 = types.InlineKeyboardButton("Город", callback_data='city')
 
            markup.add(item3, item4) 

            bot.send_message(message.chat.id, 'Где интересует?', reply_markup=markup)
           
        if message.text == '😂Анекдоты🤡':
            anekdoti = ['Врач говорит больному:\n – Вам нельзя пить, курить, увлекаться случайным сексом, играть в карты…\nБольной:\n – Доктор, скажите честно: тут уже была моя Софочка? ', 'Что будет, если Чак Нориса полить медом? Чак-чак Норис', 'На берегу стояли трое: он, она и у него']
            bot.send_message(message.chat.id, random.choice(anekdoti))
        elif message.text == '❓FAQ❓':
            faq = ["Привет, дружище! Я Telegram бот - Falcons. Что на данный момент я умею?\n Я смогу бросить кубик 🎲, где выпадет число от 1 до 6, смогу рассказать тебе анекдоты 🤡 и поговорить про твои дела 😊.\n В скором времени я буду постоянно развиваться и радовать тебя своими новыми функциями.\n\n Последнее обновление 0.3: \n\n \t\t\t\t\t\t\tДобавлено ❓FAQ❓ \n \t\t\t\t\t\t\tОптимизирован код"]
            bot.send_message(message.chat.id, faq)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и славно. Хорошего тебе дня 😊')   
            if call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает. Главное не расстраивайся😢')
            if call.data == 'country':
                bot.send_message(call.message.chat.id, 'Какая страна тебя интересует?')
            elif call.data == 'city':
                bot.send_message(call.message.chat.id, 'Какой город тебя интересует?')
 
            # remove inline buttons
            #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
               # reply_markup=None)
              # https://gruzdevv.ru/stati/boty-v-telegramme/
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="Улыбнись 😊")
 
    except Exception as e:
        print(repr(e))

# RUN
bot.polling(none_stop=True)