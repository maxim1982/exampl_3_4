#3) Дано: Длина пути в милях, название пути. Файл travel.txt
#  (Формат: “<название пути>: <длина в пути> <мера расстояния>”)
#  Вопрос: Посчитать суммарное расстояние пути в километрах? Точность: .01 .

# библиотеку suds не использовал тк устанавливается на компьютер с ошибкой.
import osa


def distance_travel(source):
    data = list()
    with open(source) as file:
        for line in file:
            data += [list(line.split())]

    url = 'http://www.webservicex.net/length.asmx?WSDL'
    client = osa.client.Client(url)

    res = 0
    for city, distance, name_dist in data:
        # проверка :
        #test = client.service.ChangeLengthUnit(LengthValue=distance, fromLengthUnit='Miles', toLengthUnit='Kilometers' )
        #print('add ', city, distance, name_dist, '=>', test, 'Kilometers')
        res += client.service.ChangeLengthUnit(LengthValue=distance, fromLengthUnit='Miles', toLengthUnit='Kilometers')
    return res


print('Total =  ', round(distance_travel('travel.txt'), 2), ' Kilometers')
