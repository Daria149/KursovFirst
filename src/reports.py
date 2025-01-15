import datetime
import json
import logging
import os
from functools import wraps
from typing import Optional

import pandas as pd

from src.services import transactions_from_excel

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_folder = os.path.join(project_path, "logs", "reports.log")


logger = logging.getLogger("reports")
file_handler = logging.FileHandler(log_folder, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.ERROR)
logger.setLevel(logging.INFO)


def file_decorator(file):
    """Декоратор, записывающий данные в файл."""

    def decorator_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logger.info("Начало записи данных в файл json")
                result = func(*args, **kwargs)
                with open(file, "w", encoding="utf-8") as file_1:
                    json.dump(result, file_1)
                return result
            except Exception as e:
                print(f"Не удалось записать данные в json-файл - {e}")
                logger.error(f"Не удалось записать данные в json-файл - {e}")

        return wrapper

    return decorator_func


@file_decorator(os.path.join(project_path, "data", "for_reports"))
def spends_by_categories(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """Функция, фильтрующая траты по категориям за последние три месяца."""
    logger.info("Выполняется функция, фильтрующая траты по категориям")
    if date is None:
        date = datetime.date.today()
    else:
        date = datetime.datetime.strptime(date, "%d.%m.%Y")
    start_date = date - datetime.timedelta(days=91)
    transactions_by_categories = transactions.loc[
        (pd.to_datetime(transactions["Дата операции"], dayfirst=True) <= date)
        & (pd.to_datetime(transactions["Дата операции"], dayfirst=True) >= start_date)
        & (transactions["Категория"] == category)
    ]
    tr = pd.DataFrame(transactions_by_categories)
    t = tr.to_dict(orient="records")
    logger.info("Функция, фильтрующая траты по категориям, завершилась успешно")
    return t


if __name__ == "__main__":
    spends_by_categories(
        transactions_from_excel("C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\KursovOperations.xlsx"),
        "Супермаркеты",
        "18.10.2021",
    )
