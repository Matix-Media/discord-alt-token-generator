from random_username.generate import generate_username
import random
import string


def generate_password(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))


def generate_email(mail=None, min=5, max=20):
    extensions = ['com', 'net', 'org', 'gov']
    domains = ['gmail', 'yahoo', 'comcast', 'verizon',
               'charter', 'hotmail', 'outlook', 'frontier', 'web']

    winext = extensions[random.randint(0, len(extensions)-1)]
    windom = domains[random.randint(0, len(domains)-1)]

    acclen = random.randint(min, max)

    if mail == None:
        winacc = ''.join(random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase)
                         for _ in range(acclen))
    else:
        winacc = mail

    finale = winacc + "@" + windom + "." + winext
    return finale


class DiscordAccount():
    token = None
    email = None
    username = None
    password = None

    def __init__(self):
        pass

    def generate_random_credentials(self):
        self.username = generate_username(1)[0]
        self.email = generate_email()
        self.password = generate_password(10)
