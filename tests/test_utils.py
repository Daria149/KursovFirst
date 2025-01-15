import os
from datetime import datetime
from unittest.mock import Mock, patch

import pytest
from freezegun import freeze_time

from src.services import transactions_from_excel
from src.utils import (
    cards_expences,
    datas_for_currency,
    datas_for_stocks,
    get_currency,
    get_stock_price,
    greetting_time_now,
    project_path,
)

file_folder = os.path.join(project_path, "data", "KursovOperations.xlsx")
for_stocks = os.path.join(project_path, "data")


@freeze_time("2019-10-05 08:15:15")
def test_1_greetting_time_now():
    mocked_datetime = Mock(return_value=(datetime(2024, 12, 2, 8, 15, 15)))
    datetime.strptime == mocked_datetime
    assert greetting_time_now("2019-10-05 08:15:15") == "Доброе утро"


@freeze_time("2024-12-01 15:15:15")
def test_2_greetting_time_now():
    mocked_datetime = Mock(return_value=(datetime(2024, 12, 1, 15, 15, 15)))
    datetime.strptime = mocked_datetime
    assert greetting_time_now("2024-12-01 15:15:15") == "Добрый день"


@freeze_time("2024-12-01 19:15:15")
def test_3_greetting_time_now():
    mocked_datetime = Mock(return_value=(datetime(2024, 12, 1, 19, 15, 15)))
    datetime.strptime = mocked_datetime
    assert greetting_time_now("2024-12-01 19:15:15") == "Добрый вечер"


@freeze_time("2024-12-01 01:15:15")
def test_4_greetting_time_now():
    mocked_datetime = Mock(return_value=(datetime(2024, 12, 1, 1, 15, 15)))
    datetime.strptime = mocked_datetime
    assert greetting_time_now("2024-12-01 01:15:15") == "Доброй ночи"


def test_1_cards_expences(card_expences_datas):
    """Функция, тестироующая вывод информации по расходам и кэшбэку по каждой карте."""
    assert cards_expences(transactions_from_excel(file_folder)) == card_expences_datas


@patch("requests.get")
def test_get_currency(mock_get):
    """Функция, тестирующая вывод Топ-5 транзакций по сумме платежа."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"base": "EUR", "rates": 87.08}
    result = get_currency("currency")
    assert result == {"base": "EUR", "rates": 87.08}
    mock_get.assert_called()


with pytest.raises(Exception):
    get_currency("RRR")


@patch("requests.get")
def test_get_stock_price(mock_get):
    """Функция, тестирующая вывод Курса валют."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "Meta Data": {
            "1. Information": "Daily Prices (open, high, low, close) and Volumes",
            "2. Symbol": "IBM",
            "3. Last Refreshed": "2025-01-05",
            "4. Output Size": "Compact",
            "5. Time Zone": "US/Eastern",
        },
        "Time Series (Daily)": {
            "2025-01-05": {
                "1. open": "217.8900",
                "2. high": "219.5900",
                "3. low": "214.7500",
                "4. close": "200.5000",
                "5. volume": "3716816",
            }
        },
    }
    assert get_stock_price(["IBM"]) == [{"stock": "IBM", "price": 200.5}]


@pytest.mark.parametrize(
    "f_path, expected",
    [
        ((os.path.join(for_stocks, "user_settings.json")), ("USD,EUR")),
        ((os.path.join(for_stocks, "for_test_utils.json")), ("EUR")),
    ],
)
def test_datas_for_currency(f_path, expected):
    assert datas_for_currency(f_path) == expected


@pytest.mark.parametrize(
    "f_path, expected",
    [
        ((os.path.join(for_stocks, "user_settings.json")), (["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"])),
        ((os.path.join(for_stocks, "for_test_utils.json")), (["AMZN", "TINK", "MSFT", "TSLA"])),
    ],
)
def test_datas_for_stocks(f_path, expected):
    assert datas_for_stocks(f_path) == expected
