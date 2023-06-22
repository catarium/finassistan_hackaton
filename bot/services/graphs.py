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
    plt.savefig('saved_figure.png')

def year_graph_line(values: list):
    num = np.arange(1, 13)
    plt.plot(num, values, 'r')
    plt.scatter(num, values, color='red')
    plt.xlabel('Номера месяцев')
    plt.ylabel('Траты')
    plt.title('Расходы')
    plt.show()
    plt.savefig('saved_figure.png')

def year_graph_bar(values: list):
    num = np.arange(1, 13)
    plt.bar(MONTHS, values, edgecolor='black')
    plt.title('Расходы')
    plt.xlabel('Месяца')
    plt.ylabel('Траты')
    plt.show()
    plt.title('Расходы')
    plt.savefig('saved_figure.png')


center = ['Еда', 'Транспор', 'Налоги', 'Развлечение', 'Прочее', 'f']
value = [random.randint(100, 1000) for x in range(12)]
year_graph_line(value)