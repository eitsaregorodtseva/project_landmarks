"""Парсинг сайта."""
import re
import random
import requests
import pandas as pd
from pandas import ExcelWriter as ew
from bs4 import BeautifulSoup


def get_html(url):
    """Автор: Царегородцева Елизавета
       Цель: получить данные для парсинга сайта
       Вход: ссылка на сайт
       Выход: html - код"""
    response = requests.get(url)
    response = response.text
    landmarks = []
    contacts = []
    information = []
    get_names(response, landmarks, contacts, information)
    export_to_excel(landmarks, contacts, information)


def get_names(data, landmarks, contacts, information):
    """Автор: Царегородцева Елизавета 
       Цель: парсинг сайта
       Вход: html - код
       Выход: список данных"""
    soup = BeautifulSoup(data, 'html.parser')
    items = soup.find('div', {'class': 'autocard-masonry'}
                      ).find_all('div', {'class': 'autocard'})
    for item in items:
        lm_price = random.randint(200, 400)
        lm_link = 'https://autotravel.ru' + item.find('a').get('href')
        lm_title = item.find('a').text
        places = item.find('p', {'class': 'mb-2 text-muted t0'}).find_all('a')
        i = 0
        for place in places:
            if i == 0:
                lm_region = place.text
                i += 1
            else:
                lm_city = place.text
        lm_info = item.find('div', {'class': 'tj t0'}).text
        if lm_info.partition('Режим работы:'):
            lm_info = lm_info.partition('Режим работы:')
            lm_schedule = lm_info[2]
            lm_info = list(lm_info)
            del lm_info[1]
            del lm_info[1]
            lm_info = ''.join(lm_info)
        if lm_info.partition('Адрес:'):
            lm_info = lm_info.partition('Адрес:')
            lm_ad = lm_info[2]
            lm_info = list(lm_info)
            del lm_info[1]
            del lm_info[1]
            lm_info = ''.join(lm_info)
            lm_rating = float(item.find('strong').text)
            if lm_ad.partition('тел.'):
                lm_ad = lm_ad.partition('тел.')
                lm_tel = lm_ad[2]
                lm_ad = list(lm_ad)
                del lm_ad[1]
                del lm_ad[1]
                lm_ad = ''.join(lm_ad)
                lm_ad = re.sub(r"[^\w]*$", '', lm_ad)
            else:
                if lm_ad.partition('Тел.'):
                    lm_ad = lm_ad.partition('Тел.')
                    lm_tel = lm_ad[2]
                    lm_ad = list(lm_ad)
                    del lm_ad[1]
                    del lm_ad[1]
                    lm_ad = ''.join(lm_ad)
                    lm_ad = re.sub(r"[^\w]*$", '', lm_ad)
        landmarks.append({
            'lm_title': lm_title,
            'lm_region': lm_region,
            'lm_city': lm_city,
            'contacts': 'Контакты',
            'information': 'Дополнительная информация'
            })
        contacts.append({
            'lm_link': lm_link,
            'lm_contacts_ad': lm_ad,
            'lm_contacts_tel': lm_tel
            })
        information.append({
            'lm_schedule': lm_schedule,
            'lm_rating': lm_rating,
            'lm_price': lm_price,
            'lm_info': lm_info
            })
    return landmarks, contacts, information


def export_to_excel(landmarks, contacts, information):
    """Автор: Царегородцева Елизавета
       Цель: преобразование списка с данными в DataFrame объект и сохранение полученной базы данных в файл xlsx
       Вход: список данных
       Выход: файл xlsx"""
    df1 = pd.DataFrame.from_dict(landmarks)
    df2 = pd.DataFrame.from_dict(contacts)
    df3 = pd.DataFrame.from_dict(information)
    landmarks.clear()
    contacts.clear()
    information.clear()
    wrt = ew('../Data/data.xlsx', engine='xlsxwriter')
    df1.to_excel(wrt, 'Основная таблица')
    df2.to_excel(wrt, 'Контакты')
    df3.to_excel(wrt, 'Дополнительная информация')
    wrt.save()
    