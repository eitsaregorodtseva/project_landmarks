"""Вывод сводной таблицы в окно"""
import tkinter as tk


def output(data):
    """Автор: Царегородцева Елизавета
       Цель: построение графика и вывод таблицы в окно приложения
       Вход: обьект DataFrame
       Выход: окно приложения с таблицей"""
    table = tk.Toplevel()
    table.title('Сводная таблица')
    table.geometry('1000x600+400+300')
    table.resizable(False, False)
    text = tk.Text(table, state='normal', width=120,
                   height=50, wrap='word')
    text.grid(row=1, column=0, padx=5, pady=5)
    text.insert('end', data)
    table.mainloop()
    