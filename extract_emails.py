import json
import re
from collections import defaultdict

# Регулярное выражение для поиска email-адресов
EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

def find_emails(text):
    """
    Принимает строку, возвращает список email-адресов.
    """
    if not text:
        return []
    return re.findall(EMAIL_REGEX, text)

# Словарь для хранения email по ИНН
emails_by_inn = defaultdict(set)

# Загрузка сообщений
with open('1000_efrsb_messages.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for msg in data:
    inn = msg.get('publisher_inn')
    text = msg.get('msg_text', '')
    emails = find_emails(text)
    if inn and emails:
        emails_by_inn[inn].update(emails)

# Преобразуем set в list для сериализации
emails_by_inn = {k: list(v) for k, v in emails_by_inn.items()}

# Сохраняем результат
with open('emails.json', 'w', encoding='utf-8') as f:
    json.dump(emails_by_inn, f, ensure_ascii=False, indent=2)

print('Готово! Email-адреса сохранены в emails.json') 