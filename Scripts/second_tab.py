"""Строит вкладку 'Понравившееся'."""
import tkinter as tk
from tkinter import ttk, Tk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import pandas as pd
import numpy as np
from pandas import ExcelWriter as ew
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import base_statistics
import out_pivot_table
import group_diagram


def error():
    """Автор: Мотявин Матвей 
       Цель: выдать сообщение об ошибке
       Вход: -
       Выход: окно с сообщением об ошибке """
    mb.showerror('Ошибка',
                 'Невозможно произвести анализ с данными параметрами.')


def secondtab(tab_2, liked_list, table_ind, new_ind, count_2):
    """Автор: Царегородцева Елизавета 
       Цель: построение и заполнение вкладки «Понравившееся»
       Вход: списки с данными и индексами об их наличии/отсутствии
       Выход: -"""
    def get_analysis():
        """Автор: Мотявин Матвей 
           Цель: строит окна с выбором параметров для анализа
           Вход: event
           Выход: вызов подходящей функции"""
        def base_stat():
            """Автор: Царегородцева Елизавета 
               Цель: проведение анализа
               Вход: список данных
               Выход: список с результатами анализа"""
            amount = 0
            for i in range(len(count_2)):
                if count_2[i] == 1:
                    amount += 1
            if amount != 0:
                if var.get() == 0:
                    error()
                elif var.get() == 3:
                    error()
                elif var.get() == 1:
                    output = []
                    count = 1
                    index = 0
                    for i in range(len(count_2)-1, -1, -1):
                        if count_2[i] == 1:
                            index = i
                    for i in range(index+1, len(liked_list)):
                        if (liked_list[index][3] == liked_list[i][3] and count_2[i] == 1):
                            count += 1
                    output.append({
                        'Значение': liked_list[index][3],
                        'Частота': count,
                        'Процент от общего числа': str(count/amount*100) + "%"
                        })
                    for i in range(index+1, len(liked_list)):
                        repeat = 0
                        for rep in range(len(output)):

                            if (liked_list[i][3] == output[rep]['Значение'] and count_2[i] == 1):
                                repeat += 1
                        if repeat == 0:
                            count = 0
                            for j in range(index+1, len(liked_list)):
                                if (liked_list[i][3] == liked_list[j][3] and count_2[i] == 1):
                                    count += 1
                            if count > 0:
                                output.append({
                                    'Значение': liked_list[i][3],
                                    'Частота': count,
                                    'Процент от общего числа': str(count/amount*100) + "%"
                                    })

                elif var.get() == 2:
                    output = []
                    count = 1
                    index = 0
                    for i in range(len(count_2)-1, -1, -1):
                        if count_2[i] == 1:
                            index = i
                    for i in range(index+1, len(liked_list)):
                        if (liked_list[index][2] == liked_list[i][2] and count_2[i] == 1):
                            count += 1
                    output.append({
                        'Значение': liked_list[index][2],
                        'Частота': count,
                        'Процент от общего числа': str(count/amount*100) + "%",
                        })
                    for i in range(index+1, len(liked_list)):
                        repeat = 0
                        for rep in range(len(output)):

                            if (liked_list[i][2] == output[rep]['Значение'] and count_2[i] == 1):
                                repeat += 1
                        if repeat == 0:
                            count = 0
                            for j in range(index+1, len(liked_list)):
                                if (liked_list[i][2] == liked_list[j][2] and count_2[i] == 1):
                                    count += 1
                            if count > 0:
                                output.append({
                                    'Значение': liked_list[i][2],
                                    'Частота': count,
                                    'Процент от общего числа': str(count/amount*100) + "%"
                                    })
                elif var.get() == 4:
                    dfcolumns = ['lm_link', 'lm_title', 'lm_region',
                                 'lm_city', 'lm_contacts_ad',
                                 'lm_contacts_tel', 'lm_schedule',
                                 'lm_rating', 'lm_price', 'lm_info']
                    liked = []
                    j = int(0)
                    for i in range(len(liked_list)):
                        liked.append(0)
                    for i in range(len(liked_list)):
                        if count_2[i] == 1:
                            liked[j] = dict(zip(dfcolumns, liked_list[i]))
                            j += 1
                    df = pd.DataFrame.from_dict(liked)
                    output = []
                    output.append({
                        'Переменная': 'Рейтинг',
                        'Максимум': df['lm_rating'].max(),
                        'Минимум': df['lm_rating'].min(),
                        'Среднее арифметическое': df['lm_rating'].mean(),
                        'Выборочная дисперсия': df['lm_rating'].std(0),
                        'Стандартное отклонение': df['lm_rating'].var(ddof=1),
                        })
                elif var.get() == 5:
                    dfcolumns = ['lm_link', 'lm_title', 'lm_region',
                                 'lm_city', 'lm_contacts_ad',
                                 'lm_contacts_tel', 'lm_schedule',
                                 'lm_rating', 'lm_price', 'lm_info']
                    liked = []
                    j = int(0)
                    for i in range(len(liked_list)):
                        liked.append(0)
                    for i in range(len(liked_list)):
                        if count_2[i] == 1:
                            liked[j] = dict(zip(dfcolumns, liked_list[i]))
                            j += 1
                    df = pd.DataFrame.from_dict(liked)
                    output = []
                    output.append({
                        'Переменная': 'Цена',
                        'Максимум': df['lm_price'].max(),
                        'Минимум': df['lm_price'].min(),
                        'Среднее арифметическое': df['lm_price'].mean(),
                        'Выборочная дисперсия': df['lm_price'].std(0),
                        'Стандартное отклонение': df['lm_price'].var(ddof=1),
                        })
                dialog1.destroy()
                if (var.get() == 1 or var.get() == 2):
                    base_statistics.base_text(output)
                if (var.get() == 4 or var.get() == 5):
                    base_statistics.base_num(output)
            else:
                mb.showerror('Ошибка', 'Список пуст.')
        def sv_table():
            """Автор: Царегородцева Елизавета 
               Цель: проведение анализа
               Вход: список данных
               Выход: обьект DataFrame"""
            amount = 0
            for i in range(len(count_2)):
                if count_2[i] == 1:
                    amount += 1
            if amount != 0:
                if entry_quality1.get() == 'Регион':
                    if entry_quality2.get() == 'Город':
                        if agreg.get() == 'Цена':
                            new_list = []
                            for i in range(len(count_2)):
                                if count_2[i] == 1:
                                    new_list.append({'Регион':
                                                     liked_list[i][2],
                                                     'Город': liked_list[i][3],
                                                     'Цена': liked_list[i][8]})
                            df = pd.DataFrame.from_dict(new_list)
                            data = pd.pivot_table(df, index=['Регион', 'Город'],
                                                  values=['Цена'],
                                                  aggfunc=np.sum)
                        else:
                            new_list = []
                            for i in range(len(count_2)):
                                if count_2[i] == 1:
                                    new_list.append({'Регион': liked_list[i][2],
                                                     'Город': liked_list[i][3],
                                                     'Количество достопримечательностей':
                                                         int(1)})
                            df = pd.DataFrame.from_dict(new_list)
                            data = pd.pivot_table(df, index=['Регион', 'Город'],
                                                  values=['Количество достопримечательностей'],
                                                  aggfunc=np.sum)
                        dialog2.destroy()
                        out_pivot_table.output(data)
                else:
                    error()
            else:
                mb.showerror('Ошибка', 'Список пуст.')

        def gr_diagram():
            """Автор: Царегородцева Елизавета 
               Цель: анализ возможности построения столбчатой диаграммы
               Вход: event
               Выход: вызов функции или окно с ошибкой"""
            amount = 0
            for i in range(len(count_2)):
                if count_2[i] == 1:
                    amount += 1
            if amount != 0:
                if entry_quality2.get() == 'Тип достопримечательности':
                    if entry_quality1.get() == 'Регион':
                        group_diagram.output(2, liked_list, count_2)
                        dialog3.destroy()
                    elif entry_quality1.get() == 'Город':
                        group_diagram.output(3, liked_list, count_2)
                        dialog3.destroy()
                    else:
                        error()
            else:
                mb.showerror('Ошибка', 'Список пуст.')
        choosen_analysis = combobox_2.get()
        if choosen_analysis == "Базовая статистика":
            dialog1 = tk.Toplevel()
            dialog1.title('Параметры базовой статистики')
            dialog1.geometry('300x300+400+300')
            dialog1.resizable(False, False)
            var = tk.IntVar()
            var.set(0)
            title = ttk.Radiobutton(dialog1, text='Название', variable=var, value=0)
            title.place(x=50, y=30)
            city = ttk.Radiobutton(dialog1, text='Город', variable=var, value=1)
            city.place(x=50, y=60)
            region = ttk.Radiobutton(dialog1, text='Регион', variable=var, value=2)
            region.place(x=50, y=90)
            link = ttk.Radiobutton(dialog1, text='Ссылка', variable=var, value=3)
            link.place(x=50, y=120)
            rating = ttk.Radiobutton(dialog1, text='Рейтинг', variable=var, value=4)
            rating.place(x=50, y=150)
            price = ttk.Radiobutton(dialog1, text='Цена', variable=var, value=5)
            price.place(x=50, y=180)
            btn_ok = tk.Button(dialog1, text='Начать анализ', command=base_stat)
            btn_ok.place(x=50, y=250)
            dialog1.mainloop()
        elif choosen_analysis == 'Сводная таблица':
            dialog2 = tk.Toplevel()
            dialog2.title('Параметры сводной таблицы')
            dialog2.geometry('400x220+400+300')
            dialog2.resizable(False, False)
            label_quality1 = tk.Label(dialog2, text='Качественный параметр 1')
            label_quality1.place(x=50, y=50)
            label_quality2 = tk.Label(dialog2, text='Качественный параметр 2')
            label_quality2.place(x=50, y=80)
            label_numerical = tk.Label(dialog2, text='Метод агрегации')
            label_numerical.place(x=50, y=110)
            entry_quality1 = ttk.Combobox(dialog2, values=['Название',
                                                           'Город',
                                                           'Регион',
                                                           'Телефон',
                                                           'Ссылка'])
            entry_quality1.current(0)
            entry_quality1.place(x=200, y=50)
            entry_quality2 = ttk.Combobox(dialog2, values=['Название',
                                                           'Город',
                                                           'Регион',
                                                           'Телефон',
                                                           'Ссылка'])
            entry_quality2.current(0)
            entry_quality2.place(x=200, y=80)
            agreg = ttk.Combobox(dialog2, values=['Цена', 'Количество достопримечательностей'])
            agreg.current(0)
            agreg.place(x=200, y=110)
            dialog2.btn_ok = tk.Button(dialog2, text='Начать анализ', command=sv_table)
            dialog2.btn_ok.place(x=200, y=170)
            dialog2.mainloop()
        elif choosen_analysis == 'Столбчатая диаграмма':
            dialog3 = tk.Toplevel()
            dialog3.title('Параметры столбчатой диаграммы')
            dialog3.geometry('400x220+400+300')
            dialog3.resizable(False, False)
            label_quality1 = tk.Label(dialog3, text='Качественный столбец 1')
            label_quality1.place(x=50, y=50)
            label_quality2 = tk.Label(dialog3, text='Качественный столбец 2')
            label_quality2.place(x=50, y=100)
            entry_quality1 = ttk.Combobox(dialog3, values=['Название',
                                                           'Город', 'Регион', 'Телефон', 'Ссылка'])
            entry_quality1.current(0)
            entry_quality1.place(x=200, y=50)
            entry_quality2 = ttk.Combobox(dialog3, values=['Название',
                                                           'Город',
                                                           'Регион',
                                                           'Тип достопримечательности',
                                                           'Адрес'])
            entry_quality2.current(0)
            entry_quality2.place(x=200, y=100)
            btn_cancel = ttk.Button(dialog3, text='Закрыть',
                                    command=dialog3.destroy)
            btn_cancel.place(x=300, y=170)
            btn_ok = ttk.Button(dialog3, text='Начать анализ',
                                command=gr_diagram)
            btn_ok.place(x=200, y=170)
            dialog3.mainloop()
        elif choosen_analysis == 'Гистограмма':
            dialog4 = Tk()
            dialog4.title('Параметры гистограммы')
            dialog4.geometry('400x220+400+300')
            dialog4.resizable(False, False)
            label_quality1 = tk.Label(dialog4, text='Качественный столбец')
            label_quality1.place(x=50, y=50)
            label_numerical = tk.Label(dialog4, text='Численный столбец')
            label_numerical.place(x=50, y=100)
            dialog4.entry_quality1 = ttk.Combobox(dialog4, values=[u'Название',
                                                                   u'Город',
                                                                   u'Регион'])
            dialog4.entry_quality1.current(0)
            dialog4.entry_quality1.place(x=200, y=50)
            dialog4.entry_numerical = ttk.Combobox(dialog4, values=[u'Цена',
                                                                    u'Рейтинг'])
            dialog4.entry_numerical.current(0)
            dialog4.entry_numerical.place(x=200, y=100)
            btn_cancel = ttk.Button(dialog4, text='Закрыть',
                                    command=dialog4.destroy)
            btn_cancel.place(x=300, y=170)
            dialog4.btn_ok = ttk.Button(dialog4, text='Начать анализ',
                                        command=histogramm)
            dialog4.btn_ok.place(x=200, y=170)
            dialog4.btn_ok.bind('<Button-1>',
                                lambda event:
                                histogramm(dialog4.entry_quality1.get(),
                                           dialog4.entry_numerical.get()))
            dialog4.grab_set()  # перехват всех событий, происходящих в приложении
            dialog4.focus_set()  # захват и удержание фокуса
            dialog4.mainloop()
        elif choosen_analysis == 'Диаграмма Бокса-Вискера':
            dialog5 = Tk()
            dialog5.title('Параметры Диаграммы Бокса-Вискера')
            dialog5.geometry('400x220+400+300')
            dialog5.resizable(False, False)
            label_quality1 = tk.Label(dialog5, text='Качественный столбец')
            label_quality1.place(x=50, y=50)
            label_numerical = tk.Label(dialog5, text='Численный столбец')
            label_numerical.place(x=50, y=100)
            dialog5.entry_quality1 = ttk.Combobox(dialog5, values=[u'Город',
                                                                   u'Регион'])
            dialog5.entry_quality1.current(0)
            dialog5.entry_quality1.place(x=200, y=50)
            dialog5.entry_numerical = ttk.Combobox(dialog5, values=[u'Цена',
                                                                    u'Рейтинг'])
            dialog5.entry_numerical.current(0)
            dialog5.entry_numerical.place(x=200, y=100)
            btn_cancel = ttk.Button(dialog5, text='Закрыть',
                                    command=dialog5.destroy)
            btn_cancel.place(x=300, y=170)
            dialog5.btn_ok = ttk.Button(dialog5, text='Начать анализ',
                                        command=boxgraph)
            dialog5.btn_ok.place(x=200, y=170)
            dialog5.btn_ok.bind('<Button-1>',
                                lambda event:
                                boxgraph(dialog5.entry_quality1.get(),
                                         dialog5.entry_numerical.get()))
            dialog5.grab_set()  # перехват всех событий, происходящих в приложении
            dialog5.focus_set()  # захват и удержание фокуса
            dialog5.mainloop()
        elif choosen_analysis == 'Диаграмма рассеивания':
            dialog6 = Tk()
            dialog6.title('Параметры диаграммы рассеивания')
            dialog6.geometry('400x220+400+300')
            dialog6.resizable(False, False)
            label_quality1 = tk.Label(dialog6, text='Качественный столбец')
            label_quality1.place(x=50, y=50)
            label_numerical1 = tk.Label(dialog6, text='Численный столбец 1')
            label_numerical1.place(x=50, y=80)
            label_numerical2 = tk.Label(dialog6, text='Численный столбец 2')
            label_numerical2.place(x=50, y=110)
            dialog6.entry_quality1 = ttk.Combobox(dialog6, values=[u'Название',
                                                                   u'Город',
                                                                   u'Регион'])
            dialog6.entry_quality1.current(0)
            dialog6.entry_quality1.place(x=200, y=50)
            dialog6.entry_numerical1 = ttk.Combobox(dialog6, values=[u'Цена',
                                                                     u'Рейтинг'])
            dialog6.entry_numerical1.current(0)
            dialog6.entry_numerical1.place(x=200, y=80)
            dialog6.entry_numerical2 = ttk.Combobox(dialog6, values=[u'Цена',
                                                                     u'Рейтинг'])
            dialog6.entry_numerical2.current(0)
            dialog6.entry_numerical2.place(x=200, y=110)
            btn_cancel = ttk.Button(dialog6, text='Закрыть',
                                    command=dialog6.destroy)
            btn_cancel.place(x=300, y=170)
            dialog6.btn_ok = ttk.Button(dialog6, text='Начать анализ',
                                        command=scatter)
            dialog6.btn_ok.place(x=200, y=170)
            dialog6.btn_ok.bind('<Button-1>', lambda event:
                                scatter(dialog6.entry_quality1.get(),
                                        dialog6.entry_numerical1.get(),
                                        dialog6.entry_numerical2.get()))
            dialog6.grab_set()  # перехват всех событий, происходящих в приложении
            dialog6.focus_set()  # захват и удержание фокуса
            dialog6.mainloop()

    def deleting():
        """Автор: Царегородцева Елизавета 
           Цель: удаление элемента из таблицы
           Вход: event
           Выход: измененные глобальные переменные"""
        try:
            item = tree.selection()[0]
            tree.delete(item)
            for i in range(len(new_ind)):
                if item == new_ind[i]:
                    count_2[i] -= 1
        except:
            mb.showerror('Ошибка', 'Вы ничего не выбрали!')

    def sort_column(tv, col, reverse):
        """Автор: Царегородцева Елизавета 
           Цель: сортировка качественных столбцов
           Вход: таблица и столбец для сортировки
           Выход: -"""
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)
        tv.heading(col, text=col, command=lambda _col=col:
                   sort_column(tv, _col, not reverse))

    def tree_sortf(tv, col, reverse):
        """Автор: Царегородцева Елизавета 
           Цель: сортировка количественных столбцов
           Вход: таблица и столбец для сортировки
           Выход: -"""
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(key=lambda rate: float(rate[0]), reverse=reverse)
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)
        tv.heading(col, command=lambda: tree_sortf(tv, col, not reverse))

    def creation():
        """Автор: Царегородцева Елизавета 
           Цель: заполнение шапки таблицы, размещение скроллбара
           Вход: -
           Выход: -"""
        tree['show'] = 'headings'
        tree.column("0", width=150, stretch=False, anchor='c')
        tree.column("1", width=150, stretch=False, anchor='c')
        tree.column("2", width=150, stretch=False, anchor='c')
        tree.column("3", width=140, stretch=False, anchor='c')
        tree.column("4", width=300, stretch=False, anchor='c')
        tree.heading("4", text="Ссылка")
        tree.place(x=30, y=220)
        scrll = ttk.Scrollbar(tab_2, orient="vertical",
                              command=tree.yview)
        scrll.place(x=922, y=220, height=430)
        tree.configure(yscrollcommand=scrll.set)
    
    def inserting():
        """Автор: Царегородцева Елизавета 
           Цель: заполнение таблицы данными (вкладка «Главное окно»)
           Вход: -
           Выход: - """
        if len(liked_list) > 0:
            for i in tree.get_children():
                tree.delete(i)
        for i in range(len(liked_list)):
            tree.insert('', 'end', values=(liked_list[i][1],
                                           liked_list[i][3],
                                           liked_list[i][2],
                                           liked_list[i][7],
                                           liked_list[i][0]))
        for i in range(len(new_ind)):
            if count_2[i] != 1:
                tree.delete(new_ind[i])
    
    def saving():
        """Автор: Царегородцева Елизавета 
           Цель: сохранение новой таблицы
           Вход: event
           Выход: excel файл"""
        if 1 not in count_2:
            mb.showerror('Ошибка', 'Вы ничего не добавили в список!')
        else:
            savefile = fd.asksaveasfilename(filetypes=(("Excel files", "*.xlsx"),
                                                       ("All files", "*.*")))
            if savefile:
                dfcolumns1 = ['lm_title', 'lm_region', 'lm_city']
                dfcolumns2 = ['lm_schedule', 'lm_rating', 'lm_price', 'lm_info']
                primary = []
                contacts = []
                info = []
                j = int(0)
                for i in range(len(liked_list)):
                    primary.append(0)
                    info.append(0)
                for i in range(len(liked_list)):
                    if count_2[i] == 1:
                        primary[j] = dict(zip(dfcolumns1, liked_list[i][1:4]))
                        contacts.append({'lm_link': liked_list[i][0],
                                         'lm_contacts_ad': liked_list[i][4],
                                         'lm_contacts_tel': liked_list[i][5]})
                        info[j] = dict(zip(dfcolumns2, liked_list[i][6:10]))
                        j += 1
                df1 = pd.DataFrame.from_dict(primary)
                df2 = pd.DataFrame.from_dict(contacts)
                df3 = pd.DataFrame.from_dict(info)
                wrt = ew(savefile + ".xlsx", engine='xlsxwriter')
                df1.to_excel(wrt, sheet_name="Основная таблица")
                df2.to_excel(wrt, sheet_name="Контакты")
                df3.to_excel(wrt, sheet_name="Дополнительная информация")
                wrt.save()
                primary.clear()
                contacts.clear()
                info.clear()
    
    def showing():
        """Автор: Царегородцева Елизавета 
           Цель: открытие окна для просмотра данных
           Вход: event
           Выход: -"""
        try:
            item = tree.selection()[0]
            for i in range(len(new_ind)):
                if item == new_ind[i]:
                    index = i
            showinfo = tk.Toplevel()
            showinfo.title("Просмотр информации")
            showinfo.geometry('500x600+450+140')
            showinfo.resizable(False, False)
            title = tk.Label(showinfo, text="Название:")
            city = tk.Label(showinfo, text="Город:")
            region = tk.Label(showinfo, text="Регион:")
            link = tk.Label(showinfo, text="Ссылка:")
            tel = tk.Label(showinfo, text="Телефон:")
            ad = tk.Label(showinfo, text="Адрес:")
            rating = tk.Label(showinfo, text="Рейтинг:")
            schedule = tk.Label(showinfo, text="Время работы:")
            price = tk.Label(showinfo, text="Цена:")
            info = tk.Label(showinfo, text="Описание:")
            title.grid(row=0, column=0, sticky="w")
            city.grid(row=1, column=0, sticky="w")
            region.grid(row=2, column=0, sticky="w")
            link.grid(row=3, column=0, sticky="w")
            tel.grid(row=4, column=0, sticky="w")
            ad.grid(row=5, column=0, sticky="w")
            rating.grid(row=6, column=0, sticky="w")
            schedule.grid(row=7, column=0, sticky="w")
            price.grid(row=8, column=0, sticky="w")
            info.grid(row=9, column=0, sticky="w")
            title_e = tk.Entry(showinfo, width=40)
            city_e = tk.Entry(showinfo, width=40)
            region_e = tk.Entry(showinfo, width=40)
            link_e = tk.Entry(showinfo, width=40)
            tel_e = tk.Entry(showinfo, width=40)
            ad_e = tk.Entry(showinfo, width=40)
            rating_e = tk.Entry(showinfo, width=40)
            schedule_e = tk.Entry(showinfo, width=40)
            price_e = tk.Entry(showinfo, width=40)
            info_e = tk.Text(showinfo, state='disabled', width=30,
                             height=20, wrap='word')
            title_e.grid(row=0, column=1, padx=5, pady=5)
            city_e.grid(row=1, column=1, padx=5, pady=5)
            region_e.grid(row=2, column=1, padx=5, pady=5)
            link_e.grid(row=3, column=1, padx=5, pady=5)
            tel_e.grid(row=4, column=1, padx=5, pady=5)
            ad_e.grid(row=5, column=1, padx=5, pady=5)
            rating_e.grid(row=6, column=1, padx=5, pady=5)
            schedule_e.grid(row=7, column=1, padx=5, pady=5)
            price_e.grid(row=8, column=1, padx=5, pady=5)
            info_e.grid(row=9, column=1, padx=5, pady=5)
            title_e.insert(0, liked_list[index][1])
            city_e.insert(0, liked_list[index][3])
            region_e.insert(0, liked_list[index][2])
            link_e.insert(0, liked_list[index][0])
            tel_e.insert(0, liked_list[index][5])
            ad_e.insert(0, liked_list[index][4])
            rating_e.insert(0, liked_list[index][7])
            schedule_e.insert(0, liked_list[index][6])
            price_e.insert(0, liked_list[index][8])
            title_e['state'] = 'disabled'
            city_e['state'] = 'disabled'
            region_e['state'] = 'disabled'
            rating_e['state'] = 'disabled'
            info_e.configure(state='normal')
            info_e.insert('end', liked_list[index][9])
            info_e.configure(state='disabled')
            link_e['state'] = 'disabled'
            showinfo.mainloop()
        except:
            mb.showerror('Ошибка', 'Вы ничего не выбрали!')

    analysis_group = tk.LabelFrame(tab_2, text='Выбор метода анализа')
    analysis_group.grid(column=0, row=0, pady=10, padx=10)
    combobox_2 = ttk.Combobox(analysis_group,
                              values=["Базовая статистика",
                                      "Сводная таблица",
                                      "Столбчатая диаграмма",
                                      "Гистограмма",
                                      "Диаграмма Бокса-Вискера",
                                      "Диаграмма рассеивания"])
    combobox_2.grid(column=0, row=1, pady=10, padx=10)
    combobox_2.current(0)
    button_method = ttk.Button(analysis_group, text="Выбрать",
                               command=get_analysis)
    button_method.grid(column=0, row=2, pady=10, padx=10)
    editing_group = tk.LabelFrame(tab_2, text='Редактирование таблицы')
    editing_group.grid(column=1, row=0, pady=10, padx=10)
    button_like = ttk.Button(editing_group, text="Удалить из понравившегося",
                             command=deleting)
    button_like.grid(column=1, row=1, pady=10, padx=10)
    save_group = tk.LabelFrame(tab_2, text='Экспорт данных')
    save_group.grid(column=2, row=0, pady=10, padx=10)
    button_save = ttk.Button(save_group, text="Сохранить изменения",
                             command=saving)
    button_save.grid(column=2, row=0, pady=10, padx=10)
    more_group = tk.LabelFrame(tab_2, text='Дополнительно')
    more_group.grid(column=3, row=0, pady=10, padx=10)
    button_show = ttk.Button(more_group, text="Просмотреть полностью",
                             command=showing)
    button_show.grid(column=3, row=1, pady=10, padx=10)

    columns = ("Название", "Город", "Регион", "Рейтинг", "Ссылка")
    tree = ttk.Treeview(tab_2, columns=columns, height=20)
    columns_sort = ("Название", "Город", "Регион")
    column = ("Рейтинг",)
    rate = []
    for i in range(len(liked_list)):
        rate.append(0)
        rate[i] = liked_list[i][7]
    for col in columns_sort:
        tree.heading(col, text=col, command=lambda _col=col:
                     sort_column(tree, _col, False))
    for col in column:
        tree.heading(col, text=col, command=lambda:
                     tree_sortf(tree, col, False))
    creation()
    inserting()

    def histogramm(chosen1, chosen2):
        """Автор: Мотявин Матвей 
           Цель: построение гистограммы
           Вход: названия столбцов
           Выход: -"""
        def save_plot():
            """Автор: Мотявин Матвей
               Цель: сохранение графического отчета
               Вход: название фигуры
               Выход: файл png"""
            name = fd.asksaveasfilename(filetypes=(("PNG", "*.png"), ("all files", "*.*")))
            fmt = name + ".png"
            figure1.savefig(fmt)
        df = pd.DataFrame(liked_list[:][:])
        if chosen1 == 'Название':
            L1Values = df.iloc[:, 1]
        elif chosen1 == 'Город':
            L1Values = df.iloc[:, 3]
        elif chosen1 == 'Регион':
            L1Values = df.iloc[:, 2]
        if chosen2 == 'Цена':
            L2Values = df.iloc[:, 8]
        if chosen2 == 'Рейтинг':
            L2Values = df.iloc[:, 7]
        predict = tk.Tk()
        predict.title('Гистограмма')
        canvas1 = tk.Canvas(predict, width=600, height=0)
        canvas1.pack()
        figure1 = plt.Figure(figsize=(9, 8), dpi=90)
        ax = figure1.add_subplot(111)
        ax.bar(L1Values, L2Values, color='orange')
        L1Values = ax.set_xticklabels(L1Values,
                                      fontsize=10,
                                      rotation=25,
                                      verticalalignment='center')
        hist1 = FigureCanvasTkAgg(figure1, predict)
        hist1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)
        ax.legend()
        ax.set_title(f"{chosen1} Vs. {chosen2}")
        SaveBut = ttk.Button(predict, text="Сохранить", width=20,
                             command=save_plot)
        SaveBut.place(y=20)
        predict.grab_set()
        predict.focus_set()
        predict.mainloop()
   
    def boxgraph(chosen1, chosen2):
        """Автор: Мотявин Матвей
        Цель: построение диаграммы Бокса-Вискера
        Вход: названия столбцов
        Выход: - """
        def check(list):
            """Автор: Мотявин Матвей
            Цель: проверить все ли данные в выбранном стоблце идентичны
            Вход: список
            Выход: список"""
            return all(i == list[0] for i in list)
        
        def save_plot():
            """Автор: Мотявин Матвей
               Цель: сохранение графического отчета
               Вход: название фигуры
               Выход: файл png"""
            name = fd.asksaveasfilename(filetypes=(("PNG", "*.png"),
                                                   ("all files", "*.*")))
            fmt = name+".png"
            figure1.savefig(fmt)
        df = pd.DataFrame(liked_list[:][:])
        if chosen1 == 'Город':
            L1Values = df.iloc[:, 3]
        elif chosen1 == 'Регион':
            L1Values = df.iloc[:, 2]
        if check(L1Values) == True:
            if chosen2 == 'Цена':
                L2Values = df.iloc[:, 8]
            elif chosen2 == 'Рейтинг':
                L2Values = df.iloc[:, 7]
            predict = tk.Tk()
            predict.title('Диаграмма Бокса-Вискера')
            canvas1 = tk.Canvas(predict, width=600, height=0)
            canvas1.pack()
            figure1 = plt.Figure(figsize=(8, 8), dpi=100)
            ax = figure1.add_subplot(111)
            ax.boxplot(L2Values,
                       patch_artist=True,
                       medianprops={'color': "#297083"},
                       boxprops={'color': "#539caf", 'facecolor': "#539caf"},
                       whiskerprops={'color': "#539caf"},
                       capprops={'color': "#539caf"})
            ax.set_xticklabels(L1Values)
            hist1 = FigureCanvasTkAgg(figure1, predict)
            hist1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)
            ax.legend()
            ax.set_xlabel(chosen1)
            ax.set_ylabel('ось ординат (YAxis)')
            ax.set_title('Layer1 Temperature Vs. Soil Temperature')
            SaveBut = ttk.Button(predict, text="Сохранить",
                                 width=20, command=save_plot)
            SaveBut.place(y=20)
            predict.grab_set()
            predict.focus_set()
            predict.mainloop()
        else:
            mb.showerror('Ошибка',
                         'Невозможно произвести анализ с данными параметрами. Проверьте чтобы все значения в выбранном вами качественном столбце были одинаковыми!')
    def scatter(chosen1, chosen2, chosen3):
        """Автор: Мотявин Матвей 
           Цель: построение диаграммы рассеивания
           Вход: названия столбцов
           Выход: -"""
        def save_plot():
            """Автор: Мотявин Матвей
               Цель: сохранение графического отчета
               Вход: название фигуры
               Выход: файл png"""
            name = fd.asksaveasfilename(filetypes=(("PNG", "*.png"),
                                                   ("all files", "*.*")))
            fmt = name+".png"
            figure1.savefig(fmt)
        df = pd.DataFrame(liked_list[:][:])
        if chosen1 == 'Название':
            L1Values = df.iloc[:, 1]
        elif chosen1 == 'Город':
            L1Values = df.iloc[:, 3]
        elif chosen1 == 'Регион':
            L1Values = df.iloc[:, 2]
        if chosen2 == 'Цена':
            L2Values = df.iloc[:, 8]
        elif chosen2 == 'Рейтинг':
            L2Values = df.iloc[:, 7]
        if chosen3 == 'Цена':
            L3Values = df.iloc[:, 8]
        elif chosen3 == 'Рейтинг':
            L3Values = df.iloc[:, 7]
        data = {'Name': L1Values,
                'Name1': L2Values,
                'Name2': L3Values}
        midwest = pd.DataFrame(data)
        categories = np.unique(midwest['Name'])
        colors = [plt.cm.tab10(i/float(len(categories)-1)) for i in range(len(categories))]
        predict = tk.Tk()
        predict.title('Диаграмма рассеивания')
        canvas1 = tk.Canvas(predict, width=600, height=0)
        canvas1.pack()
        figure1 = plt.Figure(figsize=(16, 10), dpi=80, facecolor='w',
                             edgecolor='k')
        ax = figure1.add_subplot(111)
        for i, Name in enumerate(categories):
            ax.scatter('Name1', 'Name2',
                       data=midwest.loc[midwest.Name == Name, : ],
                       s=20, c=colors[i], label=str(Name))
        hist1 = FigureCanvasTkAgg(figure1, predict)
        hist1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)
        ax.legend()
        ax.set_xlabel(chosen2)
        ax.set_ylabel(chosen3)
        ax.set_title(f"Диаграмма рассеивания")
        SaveBut = ttk.Button(predict, text="Сохранить", width=20,
                             command=save_plot)
        SaveBut.place(y=20)
        predict.grab_set()
        predict.focus_set()
        predict.mainloop()
