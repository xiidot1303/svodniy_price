from django.db.models import Q
from bot.bot import *
from transliterate import translit

def get_inline_query(update, context):
    chat_id=update.inline_query.from_user.id
    text = update.inline_query.query
    text = text.capitalize()
    text_ru = translit(text, 'ru')
    text_en = translit(text, 'ru', reversed=True)
    # text_en = regexing_en(text_en)
    # text_ru = regexing_ru(text_ru)
    # replace "-" with space
    new_text = text.replace('-', ' ')
    # split words and add regexing in 2 lang
    words = []
    for word in new_text.split():
        words.append(
            [
                regexing_en(translit(word, 'ru', reversed=True)),
                regexing_ru(translit(word, 'ru')),
            ]
        )
    # search from database
    drugs = filter_drugs_by_title_regex(words, text_en, text_ru, text)
    # create inline query
    article = [
        inlinequeryresultarticle(
            obj.title,
            obj.title_en,
            title_id=obj.pk
            ) 
            for obj in drugs
    ]
    if not article:
        article = [
            inlinequeryresultarticle(get_word('not found', chat_id=update.inline_query.from_user.id))
        ]
    
    update_inline_query_answer(update, article)


def regexing_en(text):
    list_couples = [
        'ao', 'xh', 'ie', 'qk', 'cs', 'jy', 'kc'
    ]

    for i in list_couples:
        text = text.replace(i[0], f'({i[0]}|{i[1]})')
        text = text.replace(i[1], f'({i[0]}|{i[1]})')
        text = text.replace(f'{i[0]}|({i[0]}|{i[1]})', f'{i[0]}|{i[1]}')

    return text

def regexing_ru(text):
    list_couples = [
        'ао', 'её', 'ыи', 'юу', 'щш', 'сц', ['л', 'ль'], ['н', 'нь'], 
        ['ш', 'шь'], ['д', 'дь'], ['м', 'мь'], ['т', 'ть'], ['б', 'бь'],
    ]

    for i in list_couples:
        text = text.replace(i[0], f'({i[0]}|{i[1]})')
        text = text.replace(i[1], f'({i[0]}|{i[1]})')
        text = text.replace(f'{i[0]}|({i[0]}|{i[1]})', f'{i[0]}|{i[1]}')

    return text