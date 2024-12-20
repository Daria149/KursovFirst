from datetime import datetime
from unittest.mock import patch

import pytest

from src.services import transactions_from_excel
from src.utils import cards_expences, get_currency, get_stock_price, greetting_time_now


@pytest.mark.parametrize(
    ("time_now", "expected_answer"),
    [
        (datetime(2024, 12, 2, 8, 15, 15), "Доброе утро"),
        (datetime(2024, 12, 1, 15, 15, 15), "Добрый день"),
        (datetime(2024, 12, 1, 19, 15, 15), "Добрый вечер"),
        (datetime(2024, 12, 1, 0, 15, 15), "Доброй ночи"),
    ],
)
@patch("src.utils.datetime")
def test_1_greetting_time_now(mocked_datetime, time_now, expected_answer):
    mocked_datetime.now.return_value = time_now
    assert greetting_time_now() == expected_answer


@pytest.fixture
def test_1_cards_expences():
    """Функция, тестироующая вывод информации по расходам и кэшбэку по каждой карте."""
    assert cards_expences(
        transactions_from_excel(
            "C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\ForworkKursovOperations.xlsx"
        )
    ) == [
        {"last_digits": "*4556", "total_spent": 7827.740000000001, "cashback": 78.28},
        {"last_digits": "*5091", "total_spent": 253.09, "cashback": 2.53},
        {"last_digits": "*7197", "total_spent": 1919.9, "cashback": 19.2},
    ]


@patch("requests.get")
def test_get_currency(mock_get):
    """Функция, тестирующая вывод Топ-5 транзакций по сумме платежа."""
    mock_get.return_value == {"currency": "EUR", "rate": 87.08}
    mock_get.return_value.status_code = 200
    assert get_currency("currency") == [{"currency": "EUR", "rate": 87.08}]
    mock_get.assert_called()


with pytest.raises(Exception):
    get_currency("RRR")


@patch("requests.get")
def test_get_stock_price(mock_get):
    """Функция, тестирующая вывод Курса валют."""
    mock_get.return_value.status_code = 200
    mock_get.return_value = {"AAPL": 5091}
    assert get_stock_price("AAPL") == {"AAPL": 5091}


with pytest.raises(Exception):
    get_stock_price("RRR")
