duration = int(input("Enter seconds: "))

# if duration >= 60 and duration < 3600:
#     minutes = duration // 60
#     seconds = duration % 60
#     print(f'{minutes} мин {seconds} сек')
# elif duration >= 3600 and duration < 86400:
#     hours = duration // 60 // 60
#     minutes = duration // 60 % 60
#     seconds = duration % 60
#     print(f'{hours} ч {minutes} мин {seconds} сек')
# elif duration >= 86400:
#     days = duration // 60 // 60 // 24
#     hours = duration // 60 // 60 % 24
#     minutes = duration // 60 % 60
#     seconds = duration % 60
#     if days > 30:
#         months = days // 30
#         days %= 30
#         if months >= 12:
#             years = months // 12
#             months %= 12
#             print(f'{years} г {months} мес {days} д {hours} ч {minutes} мин {seconds} сек')
#         else:
#             print(f'{months} мес {days} д {hours} ч {minutes} мин {seconds} сек')
#     else:
#         print(f'{days} д {hours} ч {minutes} мин {seconds} сек')
#
# else:
#     seconds = duration % 60
#     print(f'{seconds} сек')

if duration >= 60:
    minutes = duration // 60
    seconds = duration % 60
    if minutes >= 60:
        hours = minutes // 60
        minutes %= 60
        if hours >= 24:
            days = hours // 24
            hours %= 24
            if days >= 30:
                months = days // 30
                days %= 30
                if months >= 12:
                    years = months // 12
                    months %= 12
                    print(f'{years} г {months} мес {days} д {hours} ч {minutes} мин {seconds} сек')
                else:
                    print(f'{months} мес {days} д {hours} ч {minutes} мин {seconds} сек')
            else:
                print(f'{days} д {hours} ч {minutes} мин {seconds} сек')
        else:
            print(f'{hours} ч {minutes} мин {seconds} сек')
    else:
        print(f'{minutes} мин {seconds} сек')
else:
    seconds = duration % 60
    print(f'{seconds} сек')