from pathlib import Path
from unittest.mock import patch

import pytest

from src.services import investment_bank, transactions_from_excel, transactions_from_excel_into_list


file_folder = Path("C:/Users/Darya/Desktop/ProjectsHometasks/FilesForTasks")


@patch("pandas.read_excel")
def test_transactions_from_excel_into_list(mock_read_excel, test_transaction):
    """Функция, тестирующая функцию чтения данных из excel-файла, преобразующая в список словарей."""
    mock_read_excel.return_value = test_transaction
    assert transactions_from_excel_into_list("id,state\\n50,EXECUTED") == [{"ID": "50", "state": "EXECUTED"}]


@pytest.mark.parametrize("for_tests, expected", [(transactions_from_excel_into_list(file_folder / "transaction"), {})])
def test_2_transactions_from_excel_into_list(for_tests, expected):
    """Функция, тестирующая функцию чтения данных из excel-файла с неккоректным путём к файлу/"""
    assert for_tests == expected


@pytest.mark.parametrize("for_tests, expected", [(transactions_from_excel(file_folder / "transaction"), [])])
def test_transactions_from_excel(for_tests, expected):
    """Функция, тестирующая функцию чтения данных из excel-файла."""
    assert for_tests == expected


def test_transactions_2_from_excel():
    """Функция, тестирующая функцию чтения данных из excel-файла."""
    assert (
        len(
            transactions_from_excel(
                "C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\KursovOperations.xlsx"
            )
        )
        == 6705
    )


def test_3_transactions_from_excel():
    """Функция, тестирующая функцию чтения данных из excel-файла."""
    assert (
        transactions_from_excel(
            "C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\KursovOperations.xlsx"
        ).shape
    ) == (6705, 15)


def test_investment_bank(for_test_transactions_from_excel):
    """Функция, тестирующая возврат суммы, для «Инвесткопилки» за определённый период."""
    assert investment_bank("2018-10", for_test_transactions_from_excel, 200) == (
        '{\n    "Инвесткопилка": {\n        "2018-10": 114.0\n    }\n}'
    )


def test_2_investment_bank(for_test_transactions_from_excel):
    """Функция, тестирующая возврат суммы, для «Инвесткопилки» за определённый период."""
    assert (
        investment_bank("2018-10", for_test_transactions_from_excel, 50)
        == '{\n    "Инвесткопилка": {\n        "2018-10": 14.0\n    }\n}'
    )


def test_3_investment_bank(for_test_transactions_from_excel):
    """Функция, тестирующая возврат суммы, для «Инвесткопилки» за определённый период."""
    assert (
        investment_bank("2018-10", for_test_transactions_from_excel, 50.5)
        == '{\n    "Инвесткопилка": {\n        "2018-10": 15.0\n    }\n}'
    )


def test_4_investment_bank(for_test_transactions_from_excel):
    """Функция, тестирующая возврат суммы, для «Инвесткопилки» за определённый период."""
    assert (
        investment_bank("2019-09", for_test_transactions_from_excel, 5)
        == '{\n    "Инвесткопилка": {\n        "2019-09": 3.0\n    }\n}'
    )


def test_5_investment_bank():
    """Функция, тестирующая возврат суммы, для «Инвесткопилки» за определённый период."""
    assert investment_bank(10, [], 10) is None


def test_6_investment_bank():
    """Функция, тестирующая возврат суммы, для «Инвесткопилки» за определённый период."""
    assert investment_bank("", [], 10) is None
