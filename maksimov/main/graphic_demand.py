import matplotlib.pyplot as plt
import numpy as np

def first_image():
    y = '''41304.95041859815
    42967.521860967
    44939.20745186862
    41317.917545727556
    44449.49173313904
    48411.221444544295
    44811.747280172036
    44657.89845349863
    46448.5237968961
    47462.016938049615
    49086.256507791935
    48552.181058720926
    51448.03159887236
    55292.04929364529
    59512.9022537924
    64688.60810199752
    69035.2938600372
    71944.75619362858
    82364.2603586067
    90637.58953238466
    552428.0880064967'''
    y = list(map(float, y.split('\n')))  # Преобразуем строки в числа
    x = [2003 + i for i in range(21)]

    plt.bar(x, y, label='Уровень зарплат', color='black')  # Параметр label позволяет задать название величины для легенды
    plt.xlabel('Год')
    plt.ylabel('Уровень зарплат, руб.')
    plt.title('Уровень зарплат по годам')
    plt.legend()

    # Изменяем масштаб надписей оси x и уменьшаем шрифт
    plt.xticks(x, [f'{year}' for year in x], fontsize=6)  # Устанавливаем метки для оси x с меньшим шрифтом

    # Устанавливаем деления по оси y
    y_ticks = np.arange(0, max(y) + 100000, 50000)  # Создаем массив делений от 0 до максимального значения y с шагом 50000
    plt.yticks(y_ticks, fontsize=8)  # Устанавливаем метки для оси y с меньшим шрифтом

    # Сохраняем график в файл
    plt.savefig('uroven_zarplat_po_godam.png', format='png', dpi=300)  # Сохранение в формате PNG с разрешением 300 dpi

    plt.show()


def second_image():
    y = '''1983
    7833
    16022
    33321
    53562
    75070
    52889
    93494
    142458
    173897
    234019
    259571
    284763
    332460
    391464
    517670
    535956
    611885
    943151
    887542
    683702'''
    y = list(map(float, y.split('\n')))  # Преобразуем строки в числа
    x = [2003 + i for i in range(21)]

    plt.bar(x, y, label='Количество вакансий', color='black')  # Параметр label позволяет задать название величины для легенды
    plt.xlabel('Год')
    plt.ylabel('Количество вакансий')
    plt.title('Количество вакансий по годам')
    plt.legend()

    # Изменяем масштаб надписей оси x и уменьшаем шрифт
    plt.xticks(x, [f'{year}' for year in x], fontsize=6)  # Устанавливаем метки для оси x с меньшим шрифтом

    # # Устанавливаем деления по оси y
    y_ticks = np.arange(0, max(y) + 10000,
                        40000)  # Создаем массив делений от 0 до максимального значения y с шагом 50000
    plt.yticks(y_ticks, fontsize=8)  # Устанавливаем метки для оси y с меньшим шрифтом

    # Сохраняем график в файл
    plt.savefig('dinamica_colichestvo_vacancy_po_godam.png', format='png', dpi=300)  # Сохранение в формате PNG с разрешением 300 dpi

    plt.show()


def third_image():
    y = '''25223.026
        55093.99375000001
        49306.66343750001
        55972.13555555556
        54831.61673076923
        59740.84104265402
        66139.17851010102
        67863.71625895755
        72063.39756321291
        92168.64332317776
        112052.65955925119
        100596.68826548533
        115901.59692804824
        125104.25094197413
        125356.6002400626
        159894.2306369242
        183722.74957635996
        190159.91774707573'''
    y = list(map(float, y.split('\n')))  # Преобразуем строки в числа
    x = [2006 + i for i in range(18)]
    plt.bar(x, y, label='Зарплата для Python',
            color='black')  # Параметр label позволяет задать название величины для легенды
    plt.xlabel('Год')
    plt.ylabel('Зарплата, руб.')
    plt.title('Динамика уровня зарплат по годам для Python')
    plt.legend()

    # Изменяем масштаб надписей оси x и уменьшаем шрифт
    plt.xticks(x, [f'{year}' for year in x], fontsize=6)  # Устанавливаем метки для оси x с меньшим шрифтом

    # # Устанавливаем деления по оси y
    y_ticks = np.arange(0, max(y) + 10000,
                        15000)  # Создаем массив делений от 0 до максимального значения y с шагом 50000
    plt.yticks(y_ticks, fontsize=8)  # Устанавливаем метки для оси y с меньшим шрифтом

    # Сохраняем график в файл
    plt.savefig('dinamica_urovnia_zarplat_po_python.png', format='png',
                dpi=300)  # Сохранение в формате PNG с разрешением 300 dpi

    plt.show()



def four_image():
    y = '''5
        10
        38
        60
        169
        389
        714
        1188
        4263
        4146
        3045
        3560
        4863
        5748
        7706
        13044
        11720
        10401'''
    y = list(map(float, y.split('\n')))  # Преобразуем строки в числа
    x = [2006 + i for i in range(18)]

    plt.bar(x, y, label='Количество вакансий Python',
            color='black')  # Параметр label позволяет задать название величины для легенды
    plt.xlabel('Год')
    plt.ylabel('Количество вакансий Python')
    plt.title('Динамика уровня зарплат по годам для Python')
    plt.legend()

    # Изменяем масштаб надписей оси x и уменьшаем шрифт
    plt.xticks(x, [f'{year}' for year in x], fontsize=6)  # Устанавливаем метки для оси x с меньшим шрифтом

    # # Устанавливаем деления по оси y
    y_ticks = np.arange(0, max(y) + 2000,
                        2000)  # Создаем массив делений от 0 до максимального значения y с шагом 50000
    plt.yticks(y_ticks, fontsize=8)  # Устанавливаем метки для оси y с меньшим шрифтом

    # Сохраняем график в файл
    plt.savefig('dinamica_kolichestva_vakacy_dlya_python.png', format='png',
                dpi=300)  # Сохранение в формате PNG с разрешением 300 dpi

    plt.show()
four_image()