import datetime
import os

from src.reports import spends_by_categories
from src.services import investment_bank, transactions_from_excel, transactions_from_excel_into_list
from src.views import main_function

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_ = os.path.join(project_path, "KursovFirst", "data", "KursovOperations.xlsx")


def main_main():
    data = str(input("Введите дату для инвесткопилки в формате 'YYYY-MM':    "))
    limit = int(
        input("Введите предел, до которого нужно округлять суммы операций (целое число) для инвесткопилки____")
    )
    category = input("Введите категорию для фильтрации транзакций по категориям за определенную дату_____")
    filter_data = input(
        "Введите дату в формате 'DD.MM.YYYY' для выполнения фильтра по категориям за определенную дату ____"
    )
    first = main_function(datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"))
    second = investment_bank(data, transactions_from_excel_into_list(file_), limit)
    third = spends_by_categories(transactions_from_excel(file_), category, filter_data)
    return first, second, third


if __name__ == "__main__":
    print(main_main())
