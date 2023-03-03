from bot.utils.bot_functions import *
from yandex_geocoder import Client

def get_callback_query_data(update):
    data = update.data
    *args, result = str(data).split('_')
    return result

def get_location_coordinates(l):
    return l['latitude'], l['longitude']

def split_text_and_text_id(msg):
    return msg.split('<>?')

def get_last_msg(context):
    return context.user_data['last_msg']

def remove_inline_keyboards_from_last_msg(update, context):
    try:
        last_msg = get_last_msg(context)
        msg = bot_edit_message_text(update, context, last_msg.text, last_msg.message_id)
        return msg
    except:
        return None

def get_address_by_coordinates(lat, lon):
    try:
        client = Client('4d16304f-12ba-4134-ac9b-f0da5028a1f4')
        location = client.address(lon, lat)
        return location
    except:
        return ""

def is_group(update):
    if update.message.chat.type == 'group' or update.message.chat.type == 'supergroup':
        return True
    return False

def save_and_get_photo(update, context):
    bot = context.bot
    photo_id = bot.getFile(update.message.photo[-1].file_id)
    *args, file_name = str(photo_id.file_path).split('/')
    d_photo = photo_id.download('files/photos/{}'.format(file_name))
    return str(d_photo).replace('files/', '')

