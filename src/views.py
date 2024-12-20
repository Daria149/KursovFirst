import json

from src.services import transactions_from_excel
from src.utils import cards_expences, get_currency, get_stock_price, get_top_transactions, greetting_time_now


def main_function():
    greetting = greetting_time_now()
    card_expences = cards_expences(
        transactions_from_excel("C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\KursovOperations.xlsx")
    )
    transactions = get_top_transactions(
        transactions_from_excel("C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\KursovOperations.xlsx")
    )
    currencies = get_currency("C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\KursovFirst\\data\\user_settings.json")
    stock_prices = get_stock_price(
        "C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\KursovFirst\\data\\user_settings.json"
    )
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
    main_function()
