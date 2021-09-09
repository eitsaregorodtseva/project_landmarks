"""Cтроит главное окно"""
from tkinter import Tk, ttk
import numpy as np
import pandas as pd
import get_data
import first_tab
import second_tab


def data_import(landmarks, contacts, informations):
    """Автор: Царегородцева Елизавета
       Цель: импортировать данные из excel файла
       Вход: глобальные переменные
       Выход: измененные глобальные переменные"""
    data_open = pd.read_excel('../Data/data.xlsx',
                              sheet_name='Основная таблица')
    landmarks = data_open.to_numpy()[:][:].tolist()
    for landmark in landmarks:
        del landmark[0]
    data_open = pd.read_excel('../Data/data.xlsx', sheet_name='Контакты')
    contacts = data_open.to_numpy()[:][:].tolist()
    for contact in contacts:
        del contact[0]
    data_open = pd.read_excel('../Data/data.xlsx',
                              sheet_name='Дополнительная информация')
    informations = data_open.to_numpy()[:][:].tolist()
    for information in informations:
        del information[0]
    return landmarks, contacts, informations


def get_cities(landmarks):
    """Автор: Царегородцева Елизавета
       Цель: получить список городов
       Вход: глобальные переменные
       Выход: список"""
    cities = (np.array(landmarks))[:, 3]
    cities_m = []
    for i in range(cities.size):
        if cities[i] not in cities_m:
            cities_m.append(cities[i])
    cities = np.array(cities_m)
    cities.sort()
    cities_m.clear()
    return cities


def main_window():
    """Автор: Царегородцева Елизавета
       Цель: построение главного окна
       Вход: -
       Выход: окно приложения"""
    root = Tk()
    root.title('Достопримечательности России')
    root.resizable(False, False)
    root.width = root.winfo_screenwidth() // 2
    root.height = root.winfo_screenheight() // 2
    root.geometry('+{}+{}'.format(root.width-400, root.height-400))
    notebook = ttk.Notebook(root, width=1000, height=700)
    tab_1 = ttk.Frame(root)
    tab_2 = ttk.Frame(root)
    notebook.add(tab_1, text="Главное окно")
    notebook.add(tab_2, text="Понравившееся")
    liked_list = []
    first_tab.firsttab(tab_1, tab_2, landmarks, cities, liked_list, table_ind,
                       new_ind, count_1, count_2)
    second_tab.secondtab(tab_2, liked_list, table_ind, new_ind, count_2)
    notebook.pack(fill='both', expand=True)
    root.mainloop()


get_data.get_html("https://autotravel.ru/top100.php")
landmarks, contacts, informations = [], [], []
landmarks, contacts, informations = data_import(landmarks, contacts,
                                                informations)

for i in range(len(landmarks)):
    landmarks[i][3] = contacts[i]
    landmarks[i][4] = informations[i]
df = pd.DataFrame.from_dict(landmarks)
for i in range(len(landmarks)):
    landmarks[i][3] = landmarks[i][2]
    landmarks[i][2] = landmarks[i][1]
    landmarks[i][1] = landmarks[i][0]
    landmarks[i][0] = contacts[i][0]
    landmarks[i][4] = contacts[i][1]
    landmarks[i].append(contacts[i][2])
    landmarks[i].append(informations[i][0])
    landmarks[i].append(informations[i][1])
    landmarks[i].append(informations[i][2])
    landmarks[i].append(informations[i][3])
cities = get_cities(landmarks)
contacts.clear()
informations.clear()
new_ind = []
count_1, count_2 = [], []
for landmark in landmarks:
    count_1.append(0)
    count_2.append(0)
table_ind = np.array(['I001', 'I002', 'I003', 'I004', 'I005', 'I006', 'I007',
                      'I008', 'I009', 'I00A', 'I00B', 'I00C', 'I00D', 'I00E',
                      'I00F', 'I010', 'I011', 'I012', 'I013', 'I014', 'I015',
                      'I016', 'I017', 'I018', 'I019', 'I01A', 'I01B', 'I01C',
                      'I01D', 'I01E', 'I01F', 'I020', 'I021', 'I022', 'I023',
                      'I024', 'I025', 'I026', 'I027', 'I028', 'I029', 'I02A',
                      'I02B', 'I02C', 'I02D', 'I02E', 'I02F', 'I030', 'I031',
                      'I032', 'I033', 'I034', 'I035', 'I036', 'I037', 'I038',
                      'I039', 'I03A', 'I03B', 'I03C', 'I03D', 'I03E', 'I03F',
                      'I040', 'I041', 'I042', 'I043', 'I044', 'I045', 'I046',
                      'I047', 'I048', 'I049', 'I04A', 'I04B', 'I04C', 'I04D',
                      'I04E', 'I04F', 'I050', 'I051', 'I052', 'I053', 'I054',
                      'I055', 'I056', 'I057', 'I058', 'I059', 'I05A', 'I05B',
                      'I05C', 'I05D', 'I05E', 'I05F', 'I060', 'I061', 'I062',
                      'I063', 'I064', 'I065', 'I066', 'I067', 'I068', 'I069'])
main_window()
