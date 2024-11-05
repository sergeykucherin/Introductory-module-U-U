
def send_email(message, recipient, sender = "university.help@gmail.com"):
    recipient = str(recipient)
    sender = str(sender)
    for i in range(len(recipient)):
        if str(recipient[i]) != "@" != ".com" != ".ru" != ".net" and str(sender[i]) != "@" != ".com" != ".ru" != ".net":
            result = 'Невозможно отправить письмо с адреса <sender> на адрес <recipient>'
            break
    for i in range(len(sender[i])):
        if str(sender[i]) != "university.help@gmail.com":
            result = 'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>.'
            break
    if sender == recipient:
        result = 'Нельзя отправить письмо самому себе!'
    elif sender == "university.help@gmail.com":
        result = 'Письмо успешно отправлено с адреса <sender> на адрес <recipient>.'
    # elif sender != "university.help@gmail.com":
    #     result = 'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>.'


    return result
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))

print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))


















    # send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
    # send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
    # send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
    # send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')