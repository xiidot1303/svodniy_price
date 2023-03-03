from datetime import datetime, date, timedelta

def get_user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def datetime_now():
    now = datetime.now()
    return now

def time_now():
    now = datetime.now()
    return now.time()

def today():
    today = date.today()
    return today

def fix_format_date_in_excel(value):
    try:
        n = int(value)
        result = (date(1899, 12, 30) + timedelta(days=n)).strftime("%d.%m.%Y")
    except:
        result = value
    return result