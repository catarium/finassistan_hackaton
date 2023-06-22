from matplotlib import pyplot as plt
import numpy as np
import time


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


def year_graph_line(values_up: list, values_down: list):
    num = np.arange(1, 13)
    plt.plot(num, values_up, 'r-^')
    plt.plot(num, values_down, 'b-o')
    plt.xlabel('Номера месяцев')
    plt.ylabel('Траты')
    plt.title('Расходы')
    plt.xticks(num)
    plt.legend(['Доходы', 'Расходы'])
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


def year_graph_bars(value_up: list, value_down: list):
    plt.bar(MONTHS, value_up, edgecolor='black', color='blue')
    plt.bar(MONTHS, value_down, edgecolor='black', color='orange')
    plt.title('Расходы')
    plt.xlabel('Категории')
    plt.ylabel('Траты')
    path = f'bot/services/figures/{time.time()}.png'
    plt.savefig(path)
    return path
