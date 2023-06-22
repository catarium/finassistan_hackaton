import time

from matplotlib import pyplot as plt
import numpy as np
import random

MONTHS = ['Янв', 'Фев', 'Март', 'Апр', 'Май', 'Июнь', 'Июль',
          'Авг', 'Сент', 'Окт', 'Нояб', 'Дек']


def mounth_graph_bars(categories: list, values: list):
    plt.bar(categories, values, edgecolor='black')
    plt.title('Расходы')
    plt.xlabel('Категории')
    plt.ylabel('Траты')
    path = f'bot/services/figures/{time.time()}.png'
    plt.savefig(path)
    return path


def year_graph_line(values: list):
    num = np.arange(1, 13)
    plt.plot(num, values, 'r')
    plt.scatter(num, values, color='red')
    plt.xlabel('Номера месяцев')
    plt.ylabel('Траты')
    plt.title('Расходы')
    plt.xticks(num)

    path = f'bot/services/figures/{time.time()}.png'
    plt.savefig(path)
    return path


def year_graph_bar(values: list):
    num = np.arange(1, 13)
    plt.bar(MONTHS, values, edgecolor='black')
    plt.title('Расходы')
    plt.xlabel('Месяца')
    plt.ylabel('Траты')
    plt.show()
    plt.title('Расходы')
    filename = f'{time.time()}.png'
    plt.savefig(f'figures/{filename}')
    return filename
