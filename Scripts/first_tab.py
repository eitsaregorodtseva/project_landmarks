"""Строит вкладку 'Главное окно'."""
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as mb
import pandas as pd
import numpy as np
import base_statistics
import out_pivot_table
import second_tab


def error():
    """Автор: Мотявин Матвей 
       Цель: выдать сообщение об ошибке
       Вход: -
       Выход: окно с сообщением об ошибке """
    mb.showinfo('Ошибка',
                'Невозможно произвести анализ с данными параметрами.')


def firsttab(tab_1, tab_2, landmarks, cities, liked_list, table_ind, new_ind, count_1, count_2):
    """Автор: Царегородцева Елизавета 
       Цель: построение и заполнение вкладки «Главное окно»
       Вход: списки с данными и индексами об их наличии/отсутствии
       Выход: -"""
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

    def inserting():
        """Автор: Царегородцева Елизавета 
           Цель: заполнение таблицы данными (вкладка «Главное окно»)
           Вход: -
           Выход: - """
        for i in tree.get_children():
            tree.delete(i)
        for i in range(len(landmarks)):
            if count_1[i] == 0:
                tree.insert('', 'end', values=(landmarks[i][1],
                                               landmarks[i][3],
                                               landmarks[i][2],
                                               landmarks[i][7],
                                               landmarks[i][0]))

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
        scrll = ttk.Scrollbar(tab_1, orient="vertical",
                              command=tree.yview)
        scrll.place(x=922, y=220, height=430)
        tree.configure(yscrollcommand=scrll.set)

    def table():
        """Автор: Царегородцева Елизавета 
           Цель: вызов функций inserting, creation и функций сортировки
           Вход: -
           Выход: -"""
        creation()
        inserting()
        columns_sort = ("Название", "Город", "Регион")
        column = ("Рейтинг",)
        for col in columns_sort:
            tree.heading(col, text=col, command=lambda _col=col:
                         sort_column(tree, _col, False))
        for col in column:
            tree.heading(col, text=col, command=lambda:
                         tree_sortf(tree, col, False))

    def get_city():
        """Автор: Царегородцева Елизавета 
           Цель: перезаполнение таблицы в соответствие с выбранным городом
           Вход: event
           Выход: -"""
        choosen_city = combobox_1.get()
        for i in tree.get_children():
            tree.delete(i)
        for i in range(len(landmarks)):
            if landmarks[i][3] == choosen_city:
                tree.insert('', 'end', values=(landmarks[i][1],
                                               landmarks[i][3],
                                               landmarks[i][2],
                                               landmarks[i][7],
                                               landmarks[i][0]))

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
            for i in range(len(count_1)):
                if count_1[i] == 0:
                    amount += 1
            if amount == 1:
                mb.showinfo('Ошибка', 'Таблица пуста.')
            else:
                if var.get() == 0:
                    error()
                elif var.get() == 3:
                    error()
                elif var.get() == 1:
                    output = []
                    count = 1
                    index = 0
                    for i in range(len(count_1)-1, -1, -1):
                        if count_1[i] == 0:
                            index = i
                    for i in range(index+1, len(landmarks)):
                        if (landmarks[index][3] == landmarks[i][3] and count_1[i] == 0):
                            count += 1
                    output.append({
                        'Значение': landmarks[index][3],
                        'Частота': count,
                        'Процент от общего числа':
                            str(count/amount*100) + "%",
                            })
                    for i in range(index+1, len(landmarks)):
                        repeat = 0
                        for rep in range(len(output)):
                            if (landmarks[i][3] == output[rep]['Значение'] and count_1[i] == 0):
                                repeat += 1
                        if repeat == 0:
                            count = 0
                            for j in range(index+1, len(landmarks)):
                                if (landmarks[i][3] == landmarks[j][3] and count_1[i] == 0):
                                    count += 1
                            if count > 0:
                                output.append({
                                    'Значение': landmarks[i][3],
                                    'Частота': count,
                                    'Процент от общего числа':
                                        str(count/amount*100) + "%"})
                elif var.get() == 2:
                    output = []
                    count = 1
                    index = 0
                    for i in range(len(count_1)-1, -1, -1):
                        if count_1[i] == 0:
                            index = i
                    for i in range(index+1, len(landmarks)):
                        if (landmarks[index][2] == landmarks[i][2] and count_1[i] == 0):
                            count += 1
                    output.append({
                        'Значение': landmarks[index][2],
                        'Частота': count,
                        'Процент от общего числа': str(count) + "%",
                        })
                    for i in range(index+1, len(landmarks)):
                        repeat = 0
                        for rep in range(len(output)):

                            if (landmarks[i][2] == output[rep]['Значение'] and count_1[i] == 0):
                                repeat += 1
                        if repeat == 0:
                            count = 0
                            for j in range(index+1, len(landmarks)):
                                if (landmarks[i][2] == landmarks[j][2] and count_1[i] == 0):
                                    count += 1
                            if count > 0:
                                output.append({
                                    'Значение': landmarks[i][2],
                                    'Частота': count,
                                    'Процент от общего числа': str(count/amount*100) + "%"
                                    })
                elif var.get() == 4:
                    dfcolumns = ['lm_link', 'lm_title', 'lm_region',
                                 'lm_city', 'lm_contacts_ad',
                                 'lm_contacts_tel', 'lm_schedule',
                                 'lm_rating', 'lm_price', 'lm_info']
                    land = []
                    output = []
                    j = int(0)
                    for i in range(len(landmarks)):
                        land.append(0)
                    for i in range(len(landmarks)):
                        if count_1[i] == 0:
                            land[j] = dict(zip(dfcolumns, landmarks[i]))
                            j += 1
                    df = pd.DataFrame.from_dict(land)
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
                    land = []
                    output = []
                    j = int(0)
                    for i in range(len(landmarks)):
                        land.append(0)
                    for i in range(len(landmarks)):
                        if count_1[i] == 0:
                            land[j] = dict(zip(dfcolumns, landmarks[i]))
                            j += 1
                    df = pd.DataFrame.from_dict(land)
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

        def sv_table():
            """Автор: Царегородцева Елизавета 
               Цель: проведение анализа
               Вход: список данных
               Выход: обьект DataFrame"""
            amount = 0
            for i in range(len(count_1)):
                if count_1[i] == 0:
                    amount += 1
            if amount == 1:
                mb.showinfo('Ошибка', 'Таблица пуста.')
            else:
                if entry_quality1.get() == 'Регион':
                    if entry_quality2.get() == 'Город':
                        if agreg.get() == 'Цена':
                            new_list = []
                            for i in range(len(count_1)):
                                if count_1[i] == 0:
                                    new_list.append({'Регион': landmarks[i][2],
                                                     'Город': landmarks[i][3],
                                                     'Цена': landmarks[i][8]})
                            df = pd.DataFrame.from_dict(new_list)
                            data = pd.pivot_table(df, index=['Регион', 'Город'],
                                                  values=['Цена'],
                                                  aggfunc=np.sum)
                        else:
                            new_list = []
                            for i in range(len(count_1)):
                                if count_1[i] == 0:
                                    new_list.append({'Регион': landmarks[i][2],
                                                     'Город': landmarks[i][3],
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
            entry_quality1 = ttk.Combobox(dialog2, values=['Название', 'Город',
                                                           'Регион', 'Телефон',
                                                           'Ссылка'])
            entry_quality1.current(0)
            entry_quality1.place(x=200, y=50)
            entry_quality2 = ttk.Combobox(dialog2, values=['Название', 'Город',
                                                           'Регион', 'Телефон',
                                                           'Ссылка'])
            entry_quality2.current(0)
            entry_quality2.place(x=200, y=80)
            agreg = ttk.Combobox(dialog2, values=['Цена',
                                                  'Количество достопримечательностей'])
            agreg.current(0)
            agreg.place(x=200, y=110)
            dialog2.btn_ok = tk.Button(dialog2, text='Начать анализ',
                                       command=sv_table)
            dialog2.btn_ok.place(x=200, y=170)
            dialog2.mainloop()
        else:
            mb.showinfo('Ошибка',
                        'Эта функция возможна только в разделе "Понравившееся".')

    def liked():
        """Автор: Царегородцева Елизавета 
           Цель: добавление данных в «Понравившееся»
           Вход: event
           Выход: измененные глобальные переменные"""
        try:
            item = tree.selection()[0]
            k = int(0)
            for i in range(table_ind.size):
                if item == table_ind[i]:
                    index = i
            if (len(liked_list) == 0 and 1 not in count_2):
                liked_list.append(landmarks[index])
                new_ind.append(str(table_ind[0]))
                k = 1
                count_2[0] = 1
            else:
                rep = -1
                for j in range(len(liked_list)):
                    if landmarks[index][1] == liked_list[j][1]:
                        rep = j
                if rep > -1:
                    if count_2[rep] == 1:
                        mb.showerror("Ошибка",
                                     "Этот элемент уже добавлен в список.")
                        k = 1
                    else:
                        count_2[rep] = 1
                        k = 1
            if k == 0:
                liked_list.append(landmarks[index])
                new_ind.append(str(table_ind[len(liked_list)-1]))
                count_2[len(liked_list)-1] = 1
            second_tab.secondtab(tab_2, liked_list, table_ind, new_ind,
                                 count_2)
        except:
            mb.showerror('Ошибка', 'Вы ничего не выбрали!')

    def deleting():
        """Автор: Царегородцева Елизавета 
           Цель: удаление элемента из таблицы
           Вход: event
           Выход: измененные глобальные переменные"""
        try:
            item = tree.selection()[0]
            tree.delete(item)
            for i in range(len(table_ind)-1):
                if item == table_ind[i]:
                    count_1[i] -= 1
        except:
            mb.showerror('Ошибка', 'Вы ничего не выбрали!')

    def new_item():
        """Автор: Царегородцева Елизавета 
           Цель: добавление нового элемента в тублицу
           Вход: event
           Выход: -"""
        def save_changes():
            """Автор: Царегородцева Елизавета 
               Цель: сохранение изменений
               Вход: event
               Выход: измененные глобальные переменные"""
            index = len(landmarks)
            count_1.append(0)
            count_2.append(0)
            new = []
            new.append(link_e.get())
            new.append(title_e.get())
            new.append(region_e.get())
            new.append(city_e.get())
            new.append(ad_e.get())
            new.append(tel_e.get())
            new.append(schedule_e.get())
            if rating_e.get() == '':
                mb.showerror('Ошибка',
                             'Обязательно заполните поле "Рейтинг"!')
            else:
                if rating_e.get().isdigit():
                    new.append(rating_e.get())
                    new.append(price_e.get())
                    new.append(info_e.get(1.0, 'end'))
                    new[9] = new[9].replace("\n", "")
                    landmarks.append(new)
                    showinfo.destroy()
                    tree.insert('', 'end', values=(landmarks[index][1],
                                                   landmarks[index][3],
                                                   landmarks[index][2],
                                                   landmarks[index][7],
                                                   landmarks[index][0]))
                else:
                    mb.showerror('Ошибка',
                                 'В поле "Рейтинг" должно быть числовое значение!')
        try:
            showinfo = tk.Toplevel()
            showinfo.title("Добавление новой строки")
            showinfo.geometry('500x610+450+140')
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
            info_e = tk.Text(showinfo, state='normal', width=30,
                             height=15, wrap='word')
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
            button_ok = ttk.Button(showinfo, text="Добавить",
                                   command=save_changes)
            button_ok.grid(row=10, column=1, padx=5, pady=5)
            showinfo.mainloop()
        except:
            mb.showerror('Ошибка', 'Вы ничего не выбрали!')

    def changing():
        """Автор: Царегородцева Елизавета 
           Цель: изменение данных в таблице
           Вход: event
           Выход: -"""
        def save_changes():
            """Автор: Царегородцева Елизавета 
               Цель: сохранение изменений
               Вход: event
               Выход: измененные глобальные переменные"""
            landmarks[index][5] = tel_e.get()
            landmarks[index][6] = ad_e.get()
            landmarks[index][8] = price_e.get()
            showinfo.destroy()
        try:
            item = tree.selection()[0]
            for i in range(len(table_ind)):
                if item == table_ind[i]:
                    index = i
            showinfo = tk.Toplevel()
            showinfo.title("Изменение данных")
            showinfo.geometry('500x610+450+140')
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
                             height=15, wrap='word')
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
            title_e.insert(0, landmarks[index][1])
            city_e.insert(0, landmarks[index][3])
            region_e.insert(0, landmarks[index][2])
            link_e.insert(0, landmarks[index][0])
            tel_e.insert(0, landmarks[index][5])
            ad_e.insert(0, landmarks[index][4])
            rating_e.insert(0, landmarks[index][7])
            schedule_e.insert(0, landmarks[index][6])
            price_e.insert(0, landmarks[index][8])
            info_e.configure(state='normal')
            info_e.insert('end', landmarks[index][9])
            info_e.configure(state='disabled')
            title_e['state'] = 'disabled'
            city_e['state'] = 'disabled'
            region_e['state'] = 'disabled'
            rating_e['state'] = 'disabled'
            link_e['state'] = 'disabled'
            button_ok = ttk.Button(showinfo, text="Сохранить изменения",
                                   command=save_changes)
            button_ok.grid(row=10, column=1, padx=5, pady=5)
            showinfo.mainloop()
        except:
            mb.showerror('Ошибка', 'Вы ничего не выбрали!')

    def showing():
        """Автор: Царегородцева Елизавета 
           Цель: открытие окна для просмотра данных
           Вход: event
           Выход: -"""
        try:
            item = tree.selection()[0]
            for i in range(len(table_ind)):
                if item == table_ind[i]:
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
            title_e.insert(0, landmarks[index][1])
            city_e.insert(0, landmarks[index][3])
            region_e.insert(0, landmarks[index][2])
            link_e.insert(0, landmarks[index][0])
            tel_e.insert(0, landmarks[index][5])
            ad_e.insert(0, landmarks[index][4])
            rating_e.insert(0, landmarks[index][7])
            schedule_e.insert(0, landmarks[index][6])
            price_e.insert(0, landmarks[index][8])
            info_e.configure(state='normal')
            info_e.insert('end', landmarks[index][9])
            info_e.configure(state='disabled')
            title_e['state'] = 'disabled'
            city_e['state'] = 'disabled'
            region_e['state'] = 'disabled'
            rating_e['state'] = 'disabled'
            link_e['state'] = 'disabled'
            showinfo.mainloop()
        except:
            mb.showerror('Ошибка', 'Вы ничего не выбрали!')

    def show_all():
        """Автор: Царегородцева Елизавета 
           Цель: отображение всех элементов таблицы
           Вход: event
           Выход: -"""
        for i in tree.get_children():
            tree.delete(i)
        for i in range(len(landmarks)):
            if count_1[i] == 0:
                tree.insert('', 'end', values=(landmarks[i][1],
                                               landmarks[i][3],
                                               landmarks[i][2],
                                               landmarks[i][7],
                                               landmarks[i][0]))
    city_group = tk.LabelFrame(tab_1, text='Выбор параметров')
    city_group.grid(column=0, row=0, pady=10, padx=10)
    label_city = tk.Label(city_group, text="Выберите город:")
    label_city.grid(column=0, row=1, pady=10, padx=10)
    combobox_1 = ttk.Combobox(city_group, values=cities.tolist())
    combobox_1.grid(column=0, row=2, pady=10, padx=10)
    combobox_1.current(0)
    button_city = ttk.Button(city_group, text="Выбрать", command=get_city)
    button_city.grid(column=0, row=3, pady=10, padx=10)
    button_all = ttk.Button(city_group, text="Показать все", command=show_all)
    button_all.grid(column=0, row=4, pady=10, padx=10)
    analysis_group = tk.LabelFrame(tab_1, text='Выбор метода анализа')
    analysis_group.grid(column=1, row=0, pady=10, padx=10)
    combobox_2 = ttk.Combobox(analysis_group,
                              values=["Базовая статистика",
                                      "Сводная таблица",
                                      "Столбчатая диаграмма",
                                      "Гистограмма",
                                      "Диаграмма Бокса-Вискера",
                                      "Диаграмма рассеивания"])
    combobox_2.grid(column=1, row=1, pady=10, padx=10)
    combobox_2.current(0)
    button_method = ttk.Button(analysis_group, text="Выбрать",
                               command=get_analysis)
    button_method.grid(column=1, row=2, pady=10, padx=10)
    editing_group = tk.LabelFrame(tab_1, text='Редактирование таблицы')
    editing_group.grid(column=2, row=0, pady=10, padx=10)
    button_delete = ttk.Button(editing_group, text="Удалить",
                               command=deleting)
    button_delete.grid(column=2, row=1, pady=10, padx=10)
    button_change = ttk.Button(editing_group, text="Изменить значения",
                               command=changing)
    button_change.grid(column=2, row=2, pady=10, padx=10)
    button_new = ttk.Button(editing_group, text="Добавить новую строку",
                            command=new_item)
    button_new.grid(column=2, row=3, pady=10, padx=10)
    more_group = tk.LabelFrame(tab_1, text='Дополнительно')
    more_group.grid(column=3, row=0, pady=10, padx=10)
    button_like = ttk.Button(more_group, text="Добавить в понравившееся",
                             command=liked)
    button_like.grid(column=3, row=1, pady=10, padx=10)
    button_show = ttk.Button(more_group, text="Просмотреть полностью",
                             command=showing)
    button_show.grid(column=3, row=2, pady=10, padx=10)
    columns = ("Название", "Город", "Регион", "Рейтинг", "Ссылка")
    tree = ttk.Treeview(tab_1, columns=columns, height=20)
    rate = []
    for i in range(len(landmarks)):
        rate.append(0)
        rate[i] = landmarks[i][7]
    table()
