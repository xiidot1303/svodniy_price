from bot.bot import *

@is_start
def get_drug_name(update, context):
    msg = update.message.text
    # get drug_id from message
    try:
        drug_name, drug_id = split_text_and_text_id(msg)
    except:
        # delete message if not availabe drug_id in msg
        bot_delete_message(update, context)
        return
    
    # get drug obj by id
    drug = get_drug_by_pk(int(drug_id))
    # filter drugs that with the same title
    drugs = filter_drugs_by_title(drug.title)
    # get text to send
    drugs_info_text_list = drug_information_list(update, drugs)
    # find min and max prices
    max_price, min_price = get_max_and_min_price_of_drugs_query(drugs)
    # last text that max and min prices
    price_diff_text = max_and_min_string(update, max_price, min_price)
    # buttons for msg
    markup = select_drug_keyboard(update)
    # send messages
    bot_send_chat_action(update, context)
    remove_inline_keyboards_from_last_msg(update, context)
    [bot_send_message(update, context, text) for text in drugs_info_text_list]
    msg = bot_send_message(update, context, price_diff_text, markup)
    # set last message to user_data
    context.user_data['last_msg'] = msg
    return