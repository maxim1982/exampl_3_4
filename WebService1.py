#1) Дано: Семь значений температур по Фаренгейту. Файл temps.txt.
#   Вопрос: Какая средняя арифм. температура по Цельсию на неделю?
import osa


def average_temp(source):
    with open(source) as file:
        text = file.read()
    str_data = text.replace('  ', '').replace('\n', '').replace('F', '').split()

    url = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
    client = osa.client.Client(url)

    res = 0
    for tmp in str_data:
        res += client.service.ConvertTemp(Temperature=tmp, FromUnit='degreeFahrenheit', ToUnit='degreeCelsius', )
    return res


print('Average temperature =  %.2f  Celsius' % average_temp('temps.txt'))

