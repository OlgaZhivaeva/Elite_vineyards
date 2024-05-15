import argparse
import collections
import datetime
import pandas as pd
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


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


def get_link_to_excel():
    """Функция получает ссылку на excel файл из командной строки"""
    parser = argparse.ArgumentParser(description='Сайт Новое русское вино')
    parser.add_argument('-l', '--link_to_excel', default='wine3.xlsx', help='Ссылка на ваш excel файл')
    args = parser.parse_args()
    return args.link_to_excel


def main():
    link = get_link_to_excel()
    excel_df = pd.read_excel(io=link, na_values=['N/A', 'NA'], keep_default_na=False)
    wines_list = excel_df.to_dict('records')
    wines = collections.defaultdict(list)
    for wine in wines_list:
        wines[wine["Категория"]].append(wine)

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
    url = "http://127.0.0.1:8000"
    print(f"Перейдите на сайт по адресу {url}")

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
