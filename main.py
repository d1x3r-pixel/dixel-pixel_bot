from turtle import pos
from urllib.request import urlopen
from setuptools import Command
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
import telegram
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
)
from cred import TOKEN
from menu import main_menu_keyboard,posle_menu_keyboard
from key_buttons import tele_button, buttons
from pars import*

def start(update: Update, context: CallbackContext):
    # context.bot.send_sticker(
    #      chat_id=update.effective_chat.id,
    #      sticker='CAACAgIAAxkBAAEFNoRixrPefDYKBB1bL-B7hqAsFt1_CwACs3cBAAFji0YMTTkAAU5m1y2uKQQ'
     update.message.reply_text(
        'Здравствуйте, {username} вас приветствует цветочный магазин LoveFlowers:)'.format(
            username=update.effective_user.first_name
            if update.effective_user.first_name is not None
            else update.effective_user
        ),
        reply_markup=main_menu_keyboard()
    )
def ha_menu(update: Update, context: CallbackContext):
    update.message.reply_text(facta[0]),


def resie_curse_menu(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='''
🟢1. Выберите тип заказа:
     "Самовывоз " или "Доставка".
🟢2. Укажите ваш номер телефона.    
🟢3. Укажите имя заказчика. 
🟢!!! В БЛИЖАЙШЕЕ ВРЕМЯ ВАМ ПОЗВОНИТ АДМИНИСТРАТОР:) !!!'''

    ),
def haha_menu(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(facts)),


    

def rese_menu(update: Update, context: CallbackContext):
    update.message.reply_text(
        '🟢Книга жалоб и предложений - Здесь вы можете оставить свой честный отзыв и свои пожелания нашему салону :)'
    ),
COURSE5_RAGEX = r'(?=(' + (tele_button[5]) + r'))'
COURSE4_RAGEX = r'(?=(' + (tele_button[4]) + r'))'
COURSE3_RAGEX = r'(?=(' + (tele_button[2]) + r'))'
COURSE2_RAGEX = r'(?=(' + (tele_button[3]) + r'))'
COURSE1_RAGEX = r'(?=(' + (tele_button[0]) + r'))'
COURSE_RAGEX = r'(?=(' + (tele_button[1]) + r'))'
CNOPKI = r'(?=(' + (buttons[0]) + r'))'
CNOPKI1 = r'(?=(' + (buttons[1]) + r'))'
LESSON_RAGEX = r'(?=(' + (buttons[2]) + r'))'




def prochee_inline_menu( update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton('Реквизиты', callback_data='rek'),
            InlineKeyboardButton('Соц.сети', callback_data='xet'),
            InlineKeyboardButton('🌷За 1 Цветок ',callback_data='chena'),
        ]
    ]


    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        '🟢Выберете опцию',
        reply_markup=reply_markup
    )



def butto(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == 'rek':
         context.bot.send_message(
            update.effective_chat.id,
            text = '''
💳Оплата по карте💳:
                    1️⃣Visa: 4215 8901 1616 7039
                    2️⃣Mbank: +996 559 576 000
                    3️⃣Элсом: +996 559 576 000




📲Заказ по номеру телефона📲:
                             🟢 +996 700 777 123
            '''
         )
        

    if query.data == 'xet':
        context.bot.send_message(
            update.effective_chat.id,
            text = '''
Instagram:'https://tinyurl.com/mr2z45mk'    
Whatsapp:'https://tinyurl.com/ykhdd55n'
                '''

    )

    if query.data == 'chena':
        context.bot.send_message(
            update.effective_chat.id,
            text = '''   
🌷Роза голландская (70см) 1шт 250 сом.
🌷Хризантема Bacardi 1шт 150 сом.
🌷Лилия 1шт 350 сом.
                '''

    )



def menu(update: Update, context: CallbackContext):
    update.message.reply_text(  
        "🟢Главное меню",
        reply_markup=main_menu_keyboard()
    )  


def resive_curse_menu(update:Update, context: CallbackContext):
    update.message.reply_text(
        '🟢Выберите филиал который вам более удобен',
        reply_markup=posle_menu_keyboard()
    ), 




def button(update:Update, context: CallbackContext):
        update.message.reply_text(
        'tinyurl.com/yc77y7hf',
        reply_markup=posle_menu_keyboard()
    ),


def buttons(update:Update, context: CallbackContext):
    update.message.reply_text(
        'https://tinyurl.com/2ws3696z', 
        reply_markup=posle_menu_keyboard()
    ),





def zap(update: Update, context: CallbackContext):
    a = update.message.text
    print(a[:6])
    print(a)

    if a[:6] == 'Доставкой' or 'Самовывоз' or 'Надом':
        context.bot.send_message(
            chat_id='@asdasdasdqweqweq',
            text=a

        ),





updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot-data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSE_RAGEX),
    resie_curse_menu
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSE2_RAGEX),
    rese_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSE4_RAGEX),
    prochee_inline_menu
))


updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSE5_RAGEX),
    ha_menu
))





updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSE1_RAGEX),
    resive_curse_menu
))


updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(CNOPKI),
    button
))


updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LESSON_RAGEX),
    menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSE3_RAGEX),
    haha_menu
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(CNOPKI1),
    buttons
))




updater.dispatcher.add_handler(MessageHandler(
    Filters.text,
    zap
))

updater.dispatcher.add_handler(CallbackQueryHandler(butto))
updater.start_polling(),
updater.idle(),
