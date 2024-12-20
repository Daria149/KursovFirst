from src.reports import spends_by_categories
from src.services import investment_bank, transactions_from_excel, transactions_from_excel_into_list
from src.views import main_function


def main_main():
    data = str(input("Введите дату для инвесткопилки в формате 'YYYY-MM' ____"))
    limit = int(
        input("Введите предел, до которого нужно округлять суммы операций (целое число) для инвесткопилки____")
    )
    transactions = transactions_from_excel_into_list(
        "C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\KursovOperations.xlsx"
    )
    category = input("Введите категорию для фильтрации транзакций по категориям за определенную дату_____")
    filter_data = input(
        "Введите дату в формате 'DD.MM.YYYY' для выполнения фильтра по категориям за определенную дату ____"
    )
    transactions_for_categories = transactions_from_excel(
        "C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\KursovOperations.xlsx"
    )
    first = main_function()
    second = investment_bank(data, transactions, limit)
    third = spends_by_categories(transactions_for_categories, category, filter_data)
    return first, second, third


if __name__ == "__main__":
    print(main_main())
