import csv
from datetime import datetime
import matplotlib.pyplot as plt

path_link = 'C:\\Users\\Notebook\\PycharmProjects\\practic_learn\\vacancies.csv' #любой путь до файла
with open(path_link, 'r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)
    kon_dict = {}
    prof = ['python', 'питон', 'пайтон']
    for row in csv_reader:
        for k in prof:
            if k.lower() in row[0].lower():  # Приведение к нижнему регистру для корректного поиска
                if row[1]:
                    date_object = datetime.strptime(row[-1], "%Y-%m-%dT%H:%M:%S%z")
                    year = date_object.year
                    skills = [skill.strip() for skill in row[1].split('\n')]  # Удаление лишних пробелов
                    if year not in kon_dict:
                        kon_dict[year] = {}
                    for skill in skills:
                        if skill in kon_dict[year]:
                            kon_dict[year][skill] += 1
                        else:
                            kon_dict[year][skill] = 1

    for year in kon_dict:
        kon_dict[year] = dict(sorted(kon_dict[year].items(), key=lambda x: x[1], reverse=True)[:20])

    # Построение диаграмм
    fig, axes = plt.subplots(3, 3, figsize=(15, 10))

    for i, (year, skills) in enumerate(kon_dict.items()):
        if i < 9:
            ax = axes[i // 3, i % 3]
            ax.barh(list(skills.keys()), list(skills.values()))
            ax.set_title(f"Год: {year}", fontsize=8)
            ax.set_xlabel("Количество упоминаний", fontsize=6)
            ax.set_ylabel("Навыки", fontsize=6)
            ax.tick_params(axis='x', labelsize=8)
            ax.tick_params(axis='y', labelsize=8)

    plt.tight_layout()
    plt.show()
