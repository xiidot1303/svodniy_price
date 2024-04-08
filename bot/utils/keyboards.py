from bot.services.language_service import get_word
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton
)

def _inline_footer_buttons(update, buttons, back=True, main_menu=True):
    new_buttons = []
    if back:
        new_buttons.append(
            InlineKeyboardButton(text=get_word('back', update), callback_data='back'),
        )
    if main_menu:
        new_buttons.append(
            InlineKeyboardButton(text=get_word('main menu', update), callback_data='main_menu'),
        )

    buttons.append(new_buttons)
    return buttons


def settings_keyboard(update):

    buttons = [
        [get_word("change lang", update)],
        [get_word("change name", update)],
        [get_word("change phone number", update)],
        [get_word("main menu", update)],
    ]

    return buttons

def select_drug_keyboard(update):
    buttons = [
        [
            InlineKeyboardButton(get_word('select drug', update), switch_inline_query_current_chat='')
        ],
        [
            InlineKeyboardButton(text=get_word('about us', update), callback_data='about_us'),
            InlineKeyboardButton(text=get_word('our partners', update), callback_data='our_partners'),
        ],
        [
            InlineKeyboardButton(text=get_word('our site', update), callback_data='our_site'),
            InlineKeyboardButton(text=get_word('settings', update), callback_data='settings'),
        ],

    ]
    buttons = _inline_footer_buttons(update, buttons, back=False, main_menu=False)
    return InlineKeyboardMarkup(buttons)

def inline_back_keyboard(update):
    i_button = InlineKeyboardButton(text=get_word('back', update), callback_data='main_menu')
    markup = InlineKeyboardMarkup([[i_button]])
    return markup