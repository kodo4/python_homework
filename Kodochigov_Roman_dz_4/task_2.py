from requests import get, utils
from decimal import Decimal


def currency_rates(valute):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    parse = content.split('<')

    value = None
    valute = valute.upper()
    for i in range(6, len(parse), 12):
        if parse[i][9:] == valute:
            value = parse[i+6][6:]
            value = Decimal(value.replace(",", "."))
            value = value.quantize(Decimal("1.00"))
            return f'{valute} - {value} рублей'
    if not value:
        return None


print(currency_rates('usd'))
print(currency_rates('ge'))
print(currency_rates('EUR'))
