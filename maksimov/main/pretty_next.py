from prettytable import PrettyTable

# Данные
def first_table2():
    y = '''Айет  2827558.4344
        Бар  1245705.5
        Шахрисабз  674928.44
        Шри-Ланка  500389.76611111115
        Хива  455874.1208333333
        Шотландия  419206.1722727273
        Жолква  409405.14999999997
        Добромиль  409405.14999999997
        Моршин  409405.14999999997
        Винники  409405.14999999997
        Золочев  409405.14999999997
        Дубляны  409405.14999999997
        Глиняны  409405.14999999997
        Жидачов  409405.14999999997
        Виноградное  402733.5
        Япония  392769.2037050363
        Бельгия  390010.59810344817
        Германия  386274.3360772408
        Мальта  354148.2835714286
        ЮАР  349530.4596666667
        Египет  334580.9492857143
        Алжир  333624.88877931033
        Калинковичи  332217.1610220455
        Текели  316027.53116666665
        Албания  312466.75573529414
        Финляндия  307175.32678819436
        Афганистан  306467.21937500004
        Швеция  296587.66029139794
        Липовец  296279.6
        Андорра  295783.85722222226
        Великобритания  289012.69109797303
        Ирландия  283398.26199425285
        Красноград  282080.0
        Старобельск  279840.715
        Австрия  277770.4026593221
        Бангладеш  276944.2928947369
        Дания  276720.49842857145
        Черногория  276130.10247499996
        Канада  275527.3005670103
        Словения  270134.8225'''

    data = y.replace('\n', ' ').split()
    years = data[::2]
    profits = list(map(float, data[1::2]))
    profits = list(map(lambda x: f'{float(x):.2f}', profits))

    # Создание таблицы
    table = PrettyTable()
    table.field_names = ["Город или страна", "Средняя з/п, руб."]

    # Заполнение таблицы данными
    for year, profit in zip(years, profits):
        table.add_row([year, profit])

    # Вывод таблицы
    return table


def second_table2():
    y = '''Москва  14.393454178873128
        Санкт-Петербург  5.295408981175838
        Новосибирск  1.2650820059399512
        Екатеринбург  1.2142822853778918
        Минск  1.212055751153692
        Казань  1.0938441539738424
        Нижний-Новгород  1.076837222346445
        Краснодар  0.8997724829425371
        Алматы  0.8854973982710725
        Ростов-на-Дону  0.8385033142198792
        Воронеж  0.7370302012786939
        Самара  0.6979316286608328
        Пермь  0.6030275812321798
        Уфа  0.5646080225975854
        Челябинск  0.5524331439673872
        Красноярск  0.5304204580912569
        Киев  0.45981879485440047
        Тула  0.41661455629120664
        Ярославль  0.4096507152070077
        Омск  0.4019762780938088
        Саратов  0.38440086964321135
        Волгоград  0.38034257676647854
        Томск  0.3788266385712788
        Тюмень  0.35250300345254926
        Нур-Султан  0.34241253984075065'''

    data = y.replace('\n', ' ').split()
    years = data[::2]
    profits = list(map(float, data[1::2]))
    profits = list(map(lambda x: f'{float(x):.4f}', profits))

    # Создание таблицы
    table = PrettyTable()
    table.field_names = ["Город или страна", "Доля вакансий, %"]

    # Заполнение таблицы данными
    for year, profit in zip(years, profits):
        table.add_row([year, profit])

    # Вывод таблицы
    return table

def third_table2():
    y = '''Королевство-Саудовская-Аравия  1029147.8999999999
    Кутаиси  818452.4774999999
    Ровно  578841.33
    Швейцария  490512.165
    Словения  423774.93
    Япония  409773.47250000003
    ОАЭ  352529.38
    Бельгия  347745.95
    Дзержинск  342158.35
    Батуми  341600.4115357144
    Ирландия  337750.35
    Донецк  334316.69999999995
    Финляндия  332289.75562500005
    Турция  322646.4523076923
    Швеция  310904.140625
    Армения  306411.84558823536
    Канада  301848.8333333333
    Тбилиси  297658.9875
    Сербия  293407.1311111111
    Кипр  285388.8505813954'''

    data = y.replace('\n', ' ').split()
    years = data[::2]
    profits = list(map(float, data[1::2]))
    profits = list(map(lambda x: f'{float(x):.2f}', profits))

    # Создание таблицы
    table = PrettyTable()
    table.field_names = ["Город или страна", "Уровень з/п для Python, руб."]

    # Заполнение таблицы данными
    for year, profit in zip(years, profits):
        table.add_row([year, profit])

    # Вывод таблицы
    return table


def four_table2():
    y = '''Москва  0.14685651265997887
    Санкт-Петербург  0.05806359108072497
    Екатеринбург  0.014717233311731213
    Новосибирск  0.013722398871131357
    Казань  0.011274790326798376
    Минск  0.008732435645265409
    Нижний-Новгород  0.00859031643946543
    Краснодар  0.0067269757411990315
    Алматы  0.00650590142106573
    Киев  0.006395364260999079
    Ростов-на-Дону  0.006000588689332469
    Уфа  0.0045636056084660094
    Красноярск  0.004437277425532694
    Томск  0.004326740265466044
    Тюмень  0.004326740265466044
    Челябинск  0.0041372479910660705
    Омск  0.0034898160535328307
    Самара  0.0034582340077995025
    Воронеж  0.0034424429849328375
    Волгоград  0.003189786619066207'''

    data = y.replace('\n', ' ').split()
    years = data[::2]
    profits = list(map(float, data[1::2]))
    profits = list(map(lambda x: f'{float(x * 100):.4f}', profits))

    # Создание таблицы
    table = PrettyTable()
    table.field_names = ["Город или страна", "Доля вакансий для Python, %"]

    # Заполнение таблицы данными
    for year, profit in zip(years, profits):
        table.add_row([year, profit])

    # Вывод таблицы
    return table

