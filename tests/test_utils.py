from datetime import datetime
from unittest.mock import patch, Mock
from pathlib import Path
import pytest
from freezegun import freeze_time
from src.services import transactions_from_excel
from src.utils import (
    cards_expences,
    get_currency,
    get_stock_price,
    greetting_time_now,
    datas_for_stocks,
    datas_for_currency,
)

file_folder = Path("C:/Users/Darya/Desktop/ProjectsHometasks/FilesForTasks")
for_stocks = Path("C:/Users/Darya/Desktop/ProjectsHometasks/KursovFirst/data")


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
    assert cards_expences(transactions_from_excel(file_folder / "KursovOperations.xlsx")) == card_expences_datas


@patch("requests.get")
def test_get_currency(mock_get):
    """Функция, тестирующая вывод Топ-5 транзакций по сумме платежа."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"base": "EUR", "rates": 87.08}
    result = get_currency("currency")
    assert result == [{"currency_rates": "EUR", "rate": 87.08}]
    mock_get.assert_called()


with pytest.raises(Exception):
    get_currency("RRR")


@patch("requests.get")
def test_get_stock_price(mock_get):
    """Функция, тестирующая вывод Курса валют."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"stock": "AAPL", "price": 5091}
    assert get_stock_price(["AAPL", "AMZN"]) == [{"price": 5091, "stock": "AAPL"}, {"price": 5091, "stock": "AMZN"}]


with pytest.raises(Exception):
    get_stock_price("RRR")


@pytest.mark.parametrize(
    "f_path, expected",
    [((for_stocks / "user_settings.json"), ("USD,EUR")), ((for_stocks / "for_test_utils.json"), ("EUR"))],
)
def test_datas_for_currency(f_path, expected):
    assert datas_for_currency(f_path) == expected


@pytest.mark.parametrize(
    "f_path, expected",
    [
        ((for_stocks / "user_settings.json"), ("['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'TSLA']")),
        ((for_stocks / "for_test_utils.json"), ("['AMZN', 'TINK', 'MSFT', 'TSLA']")),
    ],
)
def test_datas_for_stocks(f_path, expected):
    assert datas_for_stocks(f_path) == expected
