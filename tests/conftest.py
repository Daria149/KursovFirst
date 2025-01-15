import os

import pandas as pd
import pytest

from src.services import transactions_from_excel_into_list

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_folder = os.path.join(project_path, "data", "KursovOperations.xlsx")


@pytest.fixture
def card_expences_datas():
    r = [
        {"cashback": 462.07, "last_digits": "*1112", "total_spent": 46207.08},
        {"cashback": 17801.5, "last_digits": "*4556", "total_spent": 1780150.21},
        {"cashback": 173.68, "last_digits": "*5091", "total_spent": 17367.5},
        {"cashback": 4708.55, "last_digits": "*5441", "total_spent": 470854.8},
        {"cashback": 840.0, "last_digits": "*5507", "total_spent": 84000.0},
        {"cashback": 692.0, "last_digits": "*6002", "total_spent": 69200.0},
        {"cashback": 24874.2, "last_digits": "*7197", "total_spent": 2487419.56},
    ]
    return r


@pytest.fixture
def test_transaction():
    for_test_transaction = pd.DataFrame({"ID": ["50"], "state": ["EXECUTED"]})
    return for_test_transaction


@pytest.fixture
def for_test_transactions_from_excel():
    transaction_from_excel_list = transactions_from_excel_into_list(file_folder)
    return transaction_from_excel_list
