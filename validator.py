import re
from datetime import datetime

def is_date(value):
    try:
        datetime.strptime(value, "%d.%m.%Y")
        return True
    except ValueError:
        pass
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_phone(value):
    return bool(re.match(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', value))

def is_email(value):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value))

def get_type(value):
    if is_date(value):
        return "date"
    if is_phone(value):
        return "phone"
    if is_email(value):
        return "email"
    return "text"
