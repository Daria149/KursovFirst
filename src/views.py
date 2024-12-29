import json
import datetime
from pathlib import Path
from typing import Any

from src.services import transactions_from_excel
from src.utils import (
    cards_expences,
    get_currency,
    get_stock_price,
    get_top_transactions,
    greetting_time_now,
    datas_for_currency,
    datas_for_stocks,
)

file_folder = Path("C:/Users/Darya/Desktop/ProjectsHometasks/FilesForTasks")
data_folder = Path("C:/Users/Darya/Desktop/ProjectsHometasks/KursovFirst/data")


def main_function(data_and_time: str) -> Any:
    greetting = greetting_time_now(data_and_time)
    card_expences = cards_expences(transactions_from_excel(file_folder / "KursovOperations.xlsx"))
    transactions = get_top_transactions(transactions_from_excel(file_folder / "KursovOperations.xlsx"))
    currencies = get_currency(datas_for_currency(data_folder / "user_settings.json"))
    stock_prices = get_stock_price(datas_for_stocks(data_folder / "user_settings.json"))
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
