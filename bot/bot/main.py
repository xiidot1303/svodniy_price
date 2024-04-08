from bot.bot import *

def start(update, context):
    if is_group(update):
        return 

    if is_registered(update.message.chat.id):
        # some functions
        main_menu(update, context)
    else:
        hello_text = lang_dict['hello']
        update.message.reply_text(
            hello_text,
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[["UZ 🇺🇿", "RU 🇷🇺"]], resize_keyboard=True, one_time_keyboard=True
            ),
        )
        return SELECT_LANG


def settings(update, context):
    update = update.callback_query
    bot_edit_message_reply_markup(update, context)
    make_button_settings(update, context)
    return ALL_SETTINGS

def search_drugs(update, context):
    # get text fot message
    text = select_drug_string(update)
    # get message buttons
    markup = select_drug_keyboard(update)
    # send message
    deleted_msg = bot_send_message(update, context, text, reply_keyboard_remove())
    bot_delete_message(update, context, deleted_msg.message_id)
    msg = update_message_reply_text(update, text, markup)
    # save last message to user_data
    context.user_data['last_msg'] = msg
    return GET_DRUG_NAME

def about(update, context):
    update = update.callback_query
    info = get_info()
    markup = select_drug_keyboard(update)
    user_lang = get_user_by_update(update).lang
    if user_lang == 'uz' and info:
        text = info.about_uz
    elif user_lang == 'ru' and info:
        text = info.about_ru
    else:
        text = '🧾'
    bot_edit_message_text(update, context, text)
    bot_edit_message_reply_markup(update, context, reply_markup = inline_back_keyboard(update))
    # update_message_reply_text(update, text, reply_markup=markup)
    

def partners(update, context):
    update = update.callback_query
    
    info = get_info()
    # markup = select_drug_keyboard(update)
    markup = None
    bot_delete_message(update, context)
    if info:
        file = get_info().partners
        bot_send_document(update, context, file, reply_markup=markup)
    else:
        text = '🤝'
        update_message_reply_text(update, text, reply_markup=markup)
    bot_send_message(update, context, get_word('our partners', update), reply_markup=inline_back_keyboard(update))

def site(update, context):
    update = update.callback_query

    text = get_info().site if get_info() else '🌐'
    markup = select_drug_keyboard(update)
    # update_message_reply_text(update, text, reply_markup=markup, disable_web_page_preview=False)
    bot_edit_message_text(update, context, text)
    bot_edit_message_reply_markup(update, context, reply_markup = inline_back_keyboard(update))

def back_to_main_menu(update, context):
    update = update.callback_query
    text = select_drug_string(update)
    # get message buttons
    markup = select_drug_keyboard(update)
    # send message
    bot_edit_message_text(update, context, text)
    bot_edit_message_reply_markup(update, context, reply_markup=markup)
