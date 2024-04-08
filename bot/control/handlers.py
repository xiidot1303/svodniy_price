from telegram import Bot, InputTextMessageContent
from telegram.ext import Dispatcher, ConversationHandler, PicklePersistence, BasePersistence
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    filters,
    CallbackQueryHandler,
    InlineQueryHandler,
    TypeHandler,
    BaseFilter
)

from bot.resources.strings import lang_dict
from bot.resources.conversationList import *
from bot.bot import (
    main, login, settings, search, drug
)
from bot.bot import main_menu


login_handler = ConversationHandler(
    entry_points=[CommandHandler("start", main.start)],
    states={
        SELECT_LANG: [MessageHandler(Filters.text(lang_dict["uz_ru"]), login.select_lang)],
        GET_NAME: [MessageHandler(Filters.text, login.get_name)],
        GET_CONTACT: [MessageHandler(Filters.all, login.get_contact)],
    },
    fallbacks=[],
    name="login",
    persistent=True,

)

settings_query = ConversationHandler(
    entry_points=[CallbackQueryHandler(main.settings, pattern="settings")],
    states={
        ALL_SETTINGS: [MessageHandler(Filters.text, settings.all_settings)],
        LANG_SETTINGS: [
            CallbackQueryHandler(settings.lang_settings),
            CommandHandler("start", settings.lang_settings),
        ],
        PHONE_SETTINGS: [MessageHandler(Filters.all, settings.phone_settings)],
        NAME_SETTINGS: [MessageHandler(Filters.text, settings.name_settings)],
    },
    fallbacks=[],
    name="settings",
    persistent=True,
  
)

# drug_handler = ConversationHandler(
#     entry_points=[MessageHandler(Filters.text(lang_dict["search drugs"]), main.search_drugs)],
#     states={
#         GET_DRUG_NAME: [
#             MessageHandler(Filters.text, drug.get_drug_name),
#             CallbackQueryHandler(drug.get_drug_name),
#         ],

#     },
#     fallbacks=[],
#     name='drug',
#     persistent=True
# )
drug_handler = MessageHandler(Filters.text, drug.get_drug_name)

about_handler = MessageHandler(Filters.text(lang_dict['about us']), main_menu)
partners_handler = MessageHandler(Filters.text(lang_dict['our partners']), main_menu)
site_handler = MessageHandler(Filters.text(lang_dict['our site']), main_menu)
settings_handler = MessageHandler(Filters.text(lang_dict["settings"]), main_menu)

about_handler_query = CallbackQueryHandler(main.about, pattern="about_us")
partners_query = CallbackQueryHandler(main.partners, pattern="our_partners")
site_query = CallbackQueryHandler(main.site, pattern="our_site")
back_query = CallbackQueryHandler(main.back_to_main_menu, pattern="main_menu")


search_handler = InlineQueryHandler(search.get_inline_query)

handlers = [
    search_handler,
    drug_handler,
    about_handler,
    partners_handler,
    site_handler,
    login_handler,
    settings_handler,

    about_handler_query,
    partners_query,
    site_query,
    settings_query,
    back_query
]