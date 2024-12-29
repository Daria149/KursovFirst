import numpy as np
from pathlib import Path


from src.reports import spends_by_categories
from src.services import transactions_from_excel

file_folder = Path("C:/Users/Darya/Desktop/ProjectsHometasks/FilesForTasks")
test_path = Path("C:/Users/Darya/Desktop/ProjectsHometasks/KursovFirst/data")


def test_spends_by_categories():
    """Функция, тестирующая функцию, фильтрующую траты по категориям за последние три месяца."""
    assert (
        spends_by_categories(
            transactions_from_excel(file_folder / "KursovOperations.xlsx").replace(np.nan, 0),
            "Авиабилеты",
            "18.10.2021",
        )
    ) == [
        {
            "MCC": 4511.0,
            "Бонусы (включая кэшбэк)": 59,
            "Валюта операции": "RUB",
            "Валюта платежа": "RUB",
            "Дата операции": "04.10.2021 19:44:04",
            "Дата платежа": "06.10.2021",
            "Категория": "Авиабилеты",
            "Кэшбэк": 0.0,
            "Номер карты": 0,
            "Округление на инвесткопилку": 0,
            "Описание": "Тинькофф Авиа",
            "Статус": "OK",
            "Сумма операции": -2980.0,
            "Сумма операции с округлением": 2980.0,
            "Сумма платежа": -2980.0,
        }
    ]


def test_2_spends_by_categories():
    """Функция, тестирующая функцию, фильтрующую траты по категориям за последние три месяца."""
    assert spends_by_categories(
        transactions_from_excel(file_folder / "KursovOperations.xlsx"), "Супермаркеты") is None
