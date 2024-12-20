from cmath import nan

from src.reports import file_decorator, spends_by_categories
from src.services import transactions_from_excel


def test_spends_by_categories():
    """Функция, тестирующая функцию, фильтрующую траты по категориям за последние три месяца."""
    assert (
        spends_by_categories(
            transactions_from_excel(
                "C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\KursovOperations.xlsx"
            ),
            "Супермаркеты",
            "18.10.2021",
        )
    ) == {
        "MCC": 5411.0,
        "Бонусы (включая кэшбэк)": 1,
        "Валюта операции": "RUB",
        "Валюта платежа": "RUB",
        "Дата операции": "17.10.2021 22:45:49",
        "Дата платежа": "18.10.2021",
        "Категория": "Супермаркеты",
        "Кэшбэк": nan,
        "Номер карты": "*7197",
        "Округление на инвесткопилку": 0,
        "Описание": "Магнит",
        "Статус": "OK",
        "Сумма операции": -55.99,
        "Сумма операции с округлением": 55.99,
        "Сумма платежа": -55.99,
    }


def test_2_spends_by_categories():
    """Функция, тестирующая функцию, фильтрующую траты по категориям за последние три месяца."""
    assert (
        len(
            (
                spends_by_categories(
                    transactions_from_excel(
                        "C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\KursovOperations.xlsx"
                    ),
                    "Супермаркеты",
                )
            )
        )
        == 0
    )
