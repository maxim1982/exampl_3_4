#2) Дано: Вы собираетесь отправиться в путешествие и начинаете разрабатывать маршрут и выписывать цены на перелеты.
#   Даны цены на билеты в местных валютах. Файл currencies.txt
#  (Формат данных в файле: “<откуда куда>: <стоимость билета> <код валюты>”)
#  Вопрос: Посчитайте сколько вы потратите на путешествие денег в рублях. Точность: без копеек, округлить в большую сторону.

import osa


def amount_travel(source):
    data = list()
    with open(source) as file:
        for line in file:
            data += [list(line.split())]

    url = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'
    client = osa.client.Client(url)

    res = 0
    for city, amount, currency in data:
        # проверка :
        #convert = client.service.ConvertToNum(fromCurrency=currency, toCurrency='RUB', amount=amount, rounding=True)
        #print('add ', city, amount, currency, '=>', convert, 'RUB')

        res += client.service.ConvertToNum(fromCurrency=currency, toCurrency='RUB', amount=amount, rounding=False)
    return res


print('Total = ', round(amount_travel('currencies.txt')), 'RUB')

