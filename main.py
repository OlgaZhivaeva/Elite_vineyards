import collections
import datetime
import pandas as pd
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from  pprint import pprint


def get_years(number):
    """Функция для правильного склонения слова год с числительными"""
    list_digit = list(str(number))
    if len(list_digit) >= 2 and list_digit[-2] == '1' and list_digit[-1] in ('1', '2', '3', '4'):
        return 'лет'
    if list_digit[-1] == '1':
        return 'год'
    if list_digit[-1] in ('2', '3', '4'):
        return 'года'
    return 'лет'


excel_df_2 = pd.read_excel(io='wine2.xlsx', na_values=['N/A', 'NA'], keep_default_na=False)
wines_list = excel_df_2.to_dict('records')
wines = collections.defaultdict(list)
for wine in wines_list:
    wines[wine["Категория"]].append(wine)
pprint(wines)

# wines_dict = {}
# wine_dict = {}
# for wine in wines_list:
#     wine_dict['Картинка'] = wine['Картинка']
#     wine_dict['Название'] = wine['Название']
#     wine_dict['Сорт'] = wine['Сорт']
#     wine_dict['Цена'] = wine['Цена']
#     if wines_dict.get(wine["Категория"]):
#         wines_dict[wine["Категория"]].append(wine_dict)
#     else:
#         wines_dict[wine["Категория"]] = [wine_dict]
# pprint(wines_dict)


# excel_df = pd.read_excel(io='wine.xlsx')
# wines = excel_df.to_dict('records')

year_production_start = datetime.datetime(year=1920, month=1, day=1)
current_year = datetime.datetime.now().year
number = current_year - year_production_start.year
years = get_years(number)
delta = f'{number} {years}'

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(
    delta=delta,
    wines=wines
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)


server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()

