from bot.services.language_service import get_word
from app.services.excel_service import get_last_excel as _get_last_excel

def select_drug_string(update):
    text = get_word('send drug name text', update)
    return text

def drug_information_list(update, drugs):
    # create template info text
    info_text = "<b>{index}. {title}</b>\n<i>{title_en_text}:</i> {title_en}\n<i>{provider_text}:</i> {provider}\n<i>{manufacturer_text}:</i> {manufacturer}\n"
    info_text += "<i>{price_text}:</i> {price}\n<i>{term_text}:</i> {term}\n<i>{address_text}:</i> {address}\n<i>{phone_text}:</i> {phone}"
    # create line text
    line_text = "🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹"
    # create text
    date_published_excel = _get_last_excel().published.strftime('%d-%m-%Y')
    result_text = f"{get_word('date published prices', update)}: {date_published_excel}"
    results = []
    n = 1
    for drug in drugs:
        text = info_text.format(
            index = n,
            title = drug.title,
            title_en_text = get_word('mnn', update),
            title_en = drug.title_en,
            provider_text = get_word('provider', update),
            provider = drug.provider.name if drug.provider else '',
            manufacturer_text = get_word('manufacturer', update),
            manufacturer = drug.manufacturer,
            address_text = get_word('address', update),
            address = drug.provider.address if drug.provider else '',
            price_text = get_word('price', update),
            price = drug.price,
            term_text = get_word('term', update),
            term = drug.term,
            phone_text = get_word('phone', update),
            phone = drug.provider.phone if drug.provider else '',
        )
        # add text to result
        result_text += f"\n\n{text}\n\n{line_text}"
        # send msg if result text contain 6 drug info
        if n % 6 == 0:
            results.append(result_text)
            result_text = ""
            
        n +=1
    # add result_text to result if not empty
    results.append(result_text) if result_text else None

    return results

def max_and_min_string(update, max, min):
    text = "{}: {} {}.\n{}: {} {}.".format(
        get_word('max price', update), max, get_word('sum', update),
        get_word('min price', update), min, get_word('sum', update)
    )
    return text
