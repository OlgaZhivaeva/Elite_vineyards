# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

Скачайте исходный код репозитория
```commandline
git clone https://github.com/OlgaZhivaeva/Elite_vineyards
```

Перейдите в папку проекта
```commandline
cd Elite_vineyards
```

Используйте python3. Установите и активируйте виртуальное окружение.<br> 
Установите зависимости при помощи `pip`
```commandline
pip install -r requirements.txt
```

Запустите сайт командой
```commandline
python3 main.py
```

Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

Вы можете загрузить на сайт свои данные. Для этого составьте свою таблицу в Excel [по образцу](wine3.xlsx) и
укажите путь к ней при запуске сайта
```commandline
python3 main.py -l путь_к_вашему_excel_файлу
```


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
