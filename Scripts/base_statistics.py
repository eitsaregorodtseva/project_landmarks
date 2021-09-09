"""Вывод базовой статистики в окно и сохранение"""
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog as fd
import pandas as pd
def base_text(output):
    """Автор: Царегородцева Елизавета
       Цель: вывод отчета по базовой статистике для текстовых переменных в окно приложения
       Вход: список данных
       Выход: - """
    def saving():
        """Автор: Царегородцева Елизавета
        Цель: сохранение отчета по базовой статистике
        Вход: -
        Выход: файл xlsx"""
        savefile = fd.asksaveasfilename(filetypes=(("Excel files", "*.xlsx"),
                                                   ("All files", "*.*")))
        if savefile:
            df = pd.DataFrame.from_dict(output)
            df.to_excel(savefile + ".xlsx", index=False,
                        sheet_name="Базовая статистика")
            output.clear()
    base = tk.Toplevel()
    base.title('Базовая статистика')
    base.geometry('600x400+400+300')
    base.resizable(False, False)
    columns = ("Значение", "Частота", "Процент от общего числа")
    tree_base = ttk.Treeview(base, columns=columns, height=20)
    tree_base.heading("0", text="Значение")
    tree_base.heading("1", text="Частота")
    tree_base.heading("2", text="Процент от общего числа")
    tree_base['show'] = 'headings'
    tree_base.column("0", width=150, stretch=False, anchor='c')
    tree_base.column("1", width=150, stretch=False, anchor='c')
    tree_base.column("2", width=200, stretch=False, anchor='c')
    tree_base.place(x=0, y=40)
    scrll = tk.Scrollbar(base, orient="vertical",
                         command=tree_base.yview)
    scrll.place(x=502, y=40, height=360)
    tree_base.configure(yscrollcommand=scrll.set)
    i = int(0)
    for i in range(len(output)):
        tree_base.insert('', 'end', values=(output[i]["Значение"],
                                            output[i]["Частота"],
                                            output[i]["Процент от общего числа"]))
    button_save = tk.Button(base, text="Сохранить",
                            command=saving)
    button_save.grid(column=0, row=0, pady=10, padx=10)
    base.mainloop()


def base_num(output):
    """Автор: Царегородцева Елизавета
       Цель: вывод отчета по базовой статистике для числовых переменных в окно приложения
       Вход: список данных
       Выход: - """
    def saving():
        """Автор: Царегородцева Елизавета
        Цель: сохранение отчета по базовой статистике
        Вход: -
        Выход: файл xlsx"""
        savefile = fd.asksaveasfilename(filetypes=(("Excel files", "*.xlsx"),
                                                   ("All files", "*.*")))
        if savefile:
            df = pd.DataFrame.from_dict(output)
            df.to_excel(savefile + ".xlsx", index=False,
                        sheet_name="Базовая статистика")
            output.clear()
    base = tk.Toplevel()
    base.title('Базовая статистика')
    base.geometry('900x400+400+300')
    base.resizable(False, False)
    columns = ("Переменная", "Максимум", "Минимум", "Среднее арифметическое",
               "Выборочная дисперсия",
               "Стандартное отклонение")
    tree_base = ttk.Treeview(base, columns=columns, height=20)
    tree_base.heading("0", text="Переменная")
    tree_base.heading("1", text="Максимум")
    tree_base.heading("2", text="Минимум")
    tree_base.heading("3", text="Среднее арифметическое")
    tree_base.heading("4", text="Выборочная дисперсия")
    tree_base.heading("5", text="Стандартное отклонение")
    tree_base['show'] = 'headings'
    tree_base.column("0", width=100, stretch=False, anchor='c')
    tree_base.column("1", width=80, stretch=False, anchor='c')
    tree_base.column("2", width=80, stretch=False, anchor='c')
    tree_base.column("3", width=150, stretch=False, anchor='c')
    tree_base.column("4", width=150, stretch=False, anchor='c')
    tree_base.column("5", width=150, stretch=False, anchor='c')
    tree_base.place(x=0, y=40)
    i = int(0)
    for i in range(len(output)):
        tree_base.insert('', 'end', values=(output[i]["Переменная"],
                                            output[i]["Максимум"],
                                            output[i]["Минимум"],
                                            output[i]["Среднее арифметическое"],
                                            output[i]["Выборочная дисперсия"],
                                            output[i]["Стандартное отклонение"]))
    button_save = tk.Button(base, text="Сохранить",
                            command=saving)
    button_save.grid(column=0, row=0, pady=10, padx=10)
    base.mainloop()
    