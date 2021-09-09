"""Построение и сохранение столбчатой диаграммы"""
import tkinter as tk
from tkinter import filedialog as fd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def output(index, liked_list, count_2):
    """Автор: Царегородцева Елизавета
       Цель: построение графика и вывод графика в окно приложения
       Вход: индекс столбца для анализа, список данных, список, указывающий на наличие/отсутствие элемента
       Выход: окно приложения с графиком"""
    def saving():
        """Автор: Царегородцева Елизавета
           Цель: сохранение графического отчета
           Вход: -
           Выход: файл png"""
        savefile = fd.asksaveasfilename(filetypes=(("PNG Files", "*.png"),
                                                   ("All files", "*.*")))
        if savefile:
            fig.savefig(savefile + ".png")
    data_names = []
    data_values1 = []
    data_values2 = []
    for i in range(len(liked_list)):
        count = 0
        if count_2[i] == 1:
            if len(data_names) > 0:
                if liked_list[i][index] in data_names:
                    count = 1
            else:
                data_names.append(liked_list[i][index])
                count = 1
        if count == 0:
            data_names.append(liked_list[i][index])
    for i in range(len(data_names)):
        index1 = 0
        index2 = 0
        for j in range(len(liked_list)):
            if (liked_list[j][index] == data_names[i]) and (count_2[j] == 1):
                if 'кремль' in liked_list[j][1]:
                    index1 += 1
                elif 'Кремль' in liked_list[j][1]:
                    index1 += 1
                else:
                    index2 += 1
        data_values1.append(index1)
        data_values2.append(index2)
    dpi = 90
    fig = plt.figure(dpi=dpi, figsize=(512/dpi, 500/dpi))
    mpl.rcParams.update({'font.size': 10})
    ax = plt.axes()
    ax.yaxis.grid(True, zorder=1)
    xs = range(len(data_names))
    plt.bar([x + 0.05 for x in xs], data_values1,
            width=0.2, color='red', alpha=0.7, label='Кремль',
            zorder=2)
    plt.bar([x + 0.3 for x in xs], data_values2,
            width=0.2, color='blue', alpha=0.7, label='Остальное',
            zorder=2)
    plt.xticks(xs, data_names)
    data_names = ax.set_xticklabels(data_names,
                                    fontsize=10,
                                    rotation=25,
                                    verticalalignment='center')
    plt.legend(loc='upper right')
    diag = tk.Toplevel()
    diag.title('Столбчатая диаграмма')
    diag.geometry('500x800')
    diag.resizable(False, False)
    FigureCanvasTkAgg(fig, diag).get_tk_widget().pack(side=tk.LEFT,
                                                      fill=tk.BOTH)
    button_save = tk.Button(diag, text="Сохранить", width=20,
                            command=saving)
    button_save.place(y=20)
    diag.mainloop()
    