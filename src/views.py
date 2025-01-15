import datetime
import json
import os
from typing import Any

from src.services import transactions_from_excel
from src.utils import (
    cards_expences,
    datas_for_currency,
    datas_for_stocks,
    get_currency,
    get_stock_price,
    get_top_transactions,
    greetting_time_now,
)

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_ = os.path.join(project_path, "data", "KursovOperations.xlsx")
file_json = os.path.join(project_path, "data", "user_settings.json")


def main_function(data_and_time: str) -> Any:
    greetting = greetting_time_now(data_and_time)
    card_expences = cards_expences(transactions_from_excel(file_))
    transactions = get_top_transactions(transactions_from_excel(file_))
    currencies = get_currency(datas_for_currency(file_json))
    stock_prices = get_stock_price(datas_for_stocks(file_json))
    json_result = json.dumps(
        {
            "greeting": greetting,
            "cards": card_expences,
            "top_transactions": transactions,
            "currency_rates": currencies,
            "stock_prices": stock_prices,
        },
        indent=4,
        ensure_ascii=False,
    )
    return json_result


if __name__ == "__main__":
    main_function(datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"))
