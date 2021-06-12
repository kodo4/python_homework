import re
RE_EMAIL_VALID = re.compile(r'[^.]+([a-z0-9-!#$%*_.])[^.]@[a-z]{0,61}\.[a-z]', re.IGNORECASE)
RE_EMAIL_PARSED = re.compile(r'([a-z0-9-!#$%*_.]+)\@([a-z.]+)')
my_dict = {}


def email_parse(email_address):
    if RE_EMAIL_VALID.match(email_address):
        my_dict['username'] = RE_EMAIL_PARSED.match(email_address)[1]
        my_dict['domain'] = RE_EMAIL_PARSED.match(email_address)[2]
        return my_dict
    else:
        raise ValueError(f'wrong email {email_address}')


email_address = input("Enter email for checked: ")
email_parse(email_address)
print(my_dict)
