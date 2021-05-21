from requests import get, utils
from decimal import Decimal
from datetime import date


def currency_rates(valute):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    parse = content.split('<')

    date_parse = parse[2][14:24]
    date_split = date_parse.split('.')
    year = int(date_split[2])
    month = int(date_split[1])
    day = int(date_split[0])
    d = date(year, month, day)

    value = None
    valute = valute.upper()
    for i in range(6, len(parse), 12):
        if parse[i][9:] == valute:
            value = parse[i+6][6:]
            value = Decimal(value.replace(",", "."))
            value = value.quantize(Decimal("1.00"))
            return f'{value}, {d}'
    if not value:
        return None


if __name__ == '__main__':
    print(currency_rates('usd'))
    print(currency_rates('ge'))
    print(currency_rates('EUR'))
