
def is_valid_email(email):
    result = "@" in email and any(email.endswith(suffix) for suffix in (".ru", ".com", ".net"))
    return result
def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if not is_valid_email(sender) or not is_valid_email(recipient):
        result = 'Невозможно отправить письмо с адреса <sender> на адрес <recipient>'
        return result
    if sender == recipient:
        result = 'Нельзя отправить письмо самому себе!'
        return result
    if sender == "university.help@gmail.com":
        result = 'Письмо успешно отправлено с адреса <sender> на адрес <recipient>.'
        return result
    else:
        result = 'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>.'
        return result

print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru',sender='urban.teacher@mail.uk'))
print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',sender='urban.info@gmail.com'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru',sender='urban.teacher@mail.ru'))











