import re


def check_email(email):
    rex = re.compile(r"^[a-zA-Z0-9_\.\+\-]+\@[\w\-]+\.[a-zа-я]{2,4}$")
    if not email:
        raise ValueError({'email': 'Это обязательное поле.'})
    if not rex.match(email):
        raise ValueError({'email': 'Недействительный адрес.'})
