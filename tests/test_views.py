import datetime
from unittest.mock import patch

from src.views import main_function


@patch("json.dumps")
def test_main_function(mock_json):
    """Функция, тестирующая основную функцию"""
    mock_json.return_value == "Всё"
    assert main_function(datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")) == "Всё"
