import datetime
import json
import logging
import os
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv

from src.services import transactions_from_excel

log_folder = Path("C:/Users/Darya/Desktop/ProjectsHometasks/KursovFirst/logs")


logger = logging.getLogger("views")
file_handler = logging.FileHandler(log_folder / "views.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
logger.setLevel(logging.ERROR)


def greetting_time_now(now_data):
    """Функция, приветствующая пользователя в зависимости от текущего времени."""
    logger.info("Выполняется функция приветствия greeting_time_now")
    current_time = datetime.datetime.strptime(now_data, "%Y-%m-%d %H:%M:%S")
    hour = int(current_time.hour)
    if 6 <= hour <= 12:
        greeting = "Доброе утро"
    elif 12 <= hour <= 18:
        greeting = "Добрый день"
    elif 18 <= hour <= 23 or hour == 00:
        greeting = "Добрый вечер"
    elif 1 <= hour <= 6:
        greeting = "Доброй ночи"
    return greeting


def cards_expences(transactions: Any) -> list[dict]:
    """Функция, выводящая информация по расходам и кэшбэку по каждой карте."""
    logger.info("Выполняется функция, выводящая информация по расходам и кэшбэку по каждой карте")
    cards = (
        transactions.loc[transactions["Сумма платежа"] < 0]
        .groupby(by="Номер карты")
        .agg("Сумма платежа")
        .sum()
        .to_dict()
    )
    logger.info("Получены расходы по картам.")
    card_expences = []
    for card, expences in cards.items():
        card_expences.append(
            {"last_digits": card, "total_spent": abs(expences), "cashback": abs(round(expences / 100, 2))}
        )
    logger.info("Расходы и кэшбэк по каждой карте готовы.")
    return card_expences


def get_top_transactions(d_transactions: Any) -> list[dict]:
    """Функция, выводящая Топ-5 транзакций по сумме платежа."""
    logger.info("Выполняется функция, выводящая Топ-5 транзакций по сумме платежа.")
    first_transactions = d_transactions.sort_values(by="Сумма платежа", ascending=True).iloc[0:4, :]
    top_transactions = first_transactions.to_dict(orient="records")
    result_top_transactions = []
    for trans in top_transactions:
        trans_data = str(
            (datetime.datetime.strptime(trans["Дата платежа"], "%d.%m.%Y").date().strftime("%d.%m.%Y")).replace(
                "-", "."
            )
        )
        result_top_transactions.append(
            {
                "date": trans_data,
                "amount": trans["Сумма платежа"],
                "category": trans["Категория"],
                "description": trans["Описание"],
            }
        )
    logger.info("Выведен список Топ-5 транзакций по сумме платежа")
    return result_top_transactions


def datas_for_currency(file_path: Any) -> Any:
    datas_for_currencies = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                currency_info = json.load(f)
                datas_for_currencies = currency_info
            except json.JSONDecodeError:
                logging.error("Ошибка декодирования")
                return datas_for_currencies
    except FileNotFoundError:
        logging.error("Ошибка поиска файла")
    list_currencies = datas_for_currencies.get("user_currencies")
    result_currencies = ",".join(list_currencies)
    return f"{result_currencies}"


def datas_for_stocks(file_path: Any) -> Any:
    data_for_stocks = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                stocks_info = json.load(f)
                data_for_stocks = stocks_info
            except json.JSONDecodeError:
                logging.error("Ошибка декодирования")
                return data_for_stocks
    except FileNotFoundError:
        logging.error("Ошибка поиска файла")
    list_stocks = data_for_stocks.get("user_stocks")
    return f"{list_stocks}"


def get_currency(currencies: Any) -> list[dict]:
    """Функция, выводящая Курс валют."""
    logging.info("Выполняется функция, выводящая Курс валют.")
    load_dotenv()
    APIKEY = os.getenv("API_KEY_GET_CURRENCY")
    url = f"https://api.apilayer.com/exchangerates_data/latest"
    headers = {"apikey": f"{APIKEY}"}
    response_currencies = []
    parameters = {"symbols": currencies, "base": "RUB"}
    response = requests.get(url, params=parameters, headers=headers)
    if response.status_code != 200:
        logging.error("Ошибка")
        raise Exception(f"{response.status_code}")
        response_currencies = []
    else:
        result_response = response.json()
        currency_dict = {"currency_rates": f"{result_response["base"]}", "rate": result_response["rates"]}
        response_currencies.append(currency_dict)
        logging.info("Данные получены.")
    return response_currencies


def get_stock_price(stocks_datas: Any) -> list[dict]:
    """Функция, выводящая стоимость акций из S&P500"""
    logger.info("Выполняется функция, выводящая стоимость акций из S&P500")
    stock_prices = []
    APIKEY_STOCK = os.getenv("API_KEY_GET_STOCK")
    for stock in stocks_datas:
        url = f"https://financialmodelingprep.com/api/v3/stock/list?apikey={APIKEY_STOCK}&symbol={stock}"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"{response.status_code}")
        else:
            get_datas = response.json()
            stock_prices.append({"stock": stock, "price": get_datas["price"]})
    logger.info("Выведен список со стоимостью акций из S&P500")
    return stock_prices


if __name__ == "__main__":
    greetting_time_now(datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"))
    cards_expences(transactions_from_excel())
    get_top_transactions(transactions_from_excel())
    get_currency()
    get_stock_price()


# if __name__ == '__main__':
#     print(greetting_time_now(datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")))

# if __name__ == '__main__':
#     print(get_currency(datas_for_currency("C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\KursovFirst\\data\\user_settings.json")))
#
# if __name__ == '__main__':
#     print(datas_for_currency("C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\KursovFirst\\data\\user_settings.json"))
# if __name__ == '__main__':
#     print(get_top_transactions(transactions_from_excel("C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\ForworkKursovOperations.xlsx")))

# if __name__ == '__main__':
#     print(get_stock_price(datas_for_stocks("C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\KursovFirst\\data\\user_settings.json")))
