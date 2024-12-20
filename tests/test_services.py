from unittest.mock import patch

import pandas as pd
import pytest

from src.services import investment_bank, transactions_from_excel, transactions_from_excel_into_list


@patch("pandas.read_excel")
def test_transactions_from_excel_into_list(mock_read_excel):
    """Функция, тестирующая функцию чтения данных из excel-файла, преобразующая в список словарей."""
    mock_read_excel.return_value = pd.DataFrame({"ID": ["50"], "state": ["EXECUTED"]})
    assert transactions_from_excel_into_list("id,state\\n50,EXECUTED") == [{"ID": "50", "state": "EXECUTED"}]


def test_2_transactions_from_excel_into_list():
    """Функция, тестирующая функцию чтения данных из excel-файла с неккоректным путём к файлу/"""
    assert (
        transactions_from_excel_into_list("C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\transaction")
        == {}
    )


def test_transactions_from_excel():
    """Функция, тестирующая функцию чтения данных из excel-файла."""
    assert (
        len(
            transactions_from_excel(
                "C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\KursovOperations.xlsx"
            )
        )
        == 6705
    )


def test_2_transactions_from_excel():
    """Функция, тестирующая функцию чтения данных из excel-файла с неккоректным путём к файлу."""
    assert transactions_from_excel("C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\transaction") == []


def test_3_transactions_from_excel():
    """Функция, тестирующая функцию чтения данных из excel-файла."""
    assert (
        transactions_from_excel(
            "C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\ForworkKursovOperations.xlsx"
        ).shape
    ) == (21, 15)


@pytest.fixture
def test_investment_bank():
    """Функция, тестирующая возврат суммы, для «Инвесткопилки» за определённый период."""
    assert (
        investment_bank(
            "2018-10",
            transactions_from_excel_into_list(
                "C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\ForworkKursovOperations.xlsx"
            ),
            200,
        )
        == '{\n    "Инвесткопилка": {\n        "2018-10": 160.0\n    }\n}'
    )


def test_2_investment_bank():
    """Функция, тестирующая возврат суммы, для «Инвесткопилки» за определённый период."""
    assert investment_bank(10, [], 10) == None
