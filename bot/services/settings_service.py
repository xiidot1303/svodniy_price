from bot.models import Settings

def is_registration_active():
    try:
        setting = Settings.objects.filter()[0]
        return setting.registration
    except:
        return False