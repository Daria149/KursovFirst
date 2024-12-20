# Проект KursovFirst



## Описание:

Проект KursovFirst - это проект, реализующий некоторые функции для анализа расходов, банковских операций.
Проект также представляет возможность проанализировать некоторые данные финансовых рынков.

Сервис "Веб-страницы" содержится в модулях utils, views. Основная функция для сервиса находится в модуле views.
Модуль utils содержит функции, реализующие следующие операции: 
1. Приветствие
2. Информация по каждой карте о сумме расходов и кэшбэке.
3. Топ-5 транзакций по сумме платежа.
4. Курс валют.
5. Стоимость акций из S&P500.

Сервис "Сервисы" в модуле services реализуют идею Инвесткопилки.
Инвесткопилка отражает сумму округления расходов с учетом лимита, которая будет попадать на счет «Инвесткопилки».

Сервис "Отчеты" в модуле reports фильтрует траты по категориям за последние три месяца.
Данные записываются в json-файл.





## Установка:

1. Клонируйте репозиторий:

```
git@github.com:Daria149/KursovFirst.git
```

2. Установите зависимости:

```
pip install -r requirements.txt
```

## Использование:
1. Откройте приложение в вашем веб-браузере.
2. Введите новую информацию для запросов, а также данные с идентификационными данными согласну шаблону env.
3. Запустите проект.


## Тестирование:
Проект содержит блок с тестами для проверки кода из основных модулей. 
При необходимости можно запустить выполнение тестов.


## Документация:
Для получения дополнительной информации обратитесь к файлу README.md.