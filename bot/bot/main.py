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
                keyboard=[["UZ πΊπΏ", "RU π·πΊ"]], resize_keyboard=True, one_time_keyboard=True
            ),
        )
        return SELECT_LANG


def settings(update, context):
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
    info = get_info()
    user_lang = get_user_by_update(update).lang
    if user_lang == 'uz' and info:
        text = info.about_uz
    elif user_lang == 'ru' and info:
        text = info.about_ru
    else:
        text = 'π§Ύ'
    update_message_reply_text(update, text)
    

def partners(update, context):
    info = get_info()
    if info:
        file = get_info().partners
        bot_send_document(update, context, file)
    else:
        text = 'π€'
        update_message_reply_text(update, text)

def site(update, context):
    text = get_info().site if get_info() else 'π'
    update_message_reply_text(update, text, disable_web_page_preview=False)
    