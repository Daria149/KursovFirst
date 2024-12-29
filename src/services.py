import datetime
import json
import logging
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd

log_folder = Path("C:/Users/Darya/Desktop/ProjectsHometasks/KursovFirst/logs")

logger = logging.getLogger("services")
file_handler = logging.FileHandler(log_folder / "services.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
logger.setLevel(logging.ERROR)


def transactions_from_excel(file_path: str) -> Any:
    """Функция, читающая данные из Excel-файла."""
    try:
        datas = pd.read_excel(file_path)
    except FileNotFoundError:
        logging.error("Файл не найден")
        datas = []
    logging.info("Файл читается")
    return datas


def transactions_from_excel_into_list(file_path: str) -> Any:
    """Функция, читающая данные из Excel-файла."""
    try:
        datas = pd.read_excel(file_path)
        dict_datas = list(datas.to_dict(orient="records"))
    except FileNotFoundError:
        logging.error("Файл не найден")
        dict_datas = {}
    logging.info("Файл читается")

    return dict_datas


def investment_bank(month: str, transactions: List[Dict[str, Any]], limit: int) -> float:
    """Функция, возвращает сумму, которую удалось бы отложить в «Инвесткопилку» за определённый период."""
    logging.info("Выполняется функция, возвращает сумму, которую удалось бы отложить в «Инвесткопилку».")
    # final_date = datetime.datetime.strptime(str_data, "%Y-%m")
    # obj_month = datetime.datetime.strptime(month, "%Y-%m")
    transaction_by_month = []
    for trans in transactions:
        get_data = datetime.datetime.strptime(trans["Дата операции"], "%d.%m.%Y %H:%M:%S").date()
        str_data = datetime.datetime.strftime(get_data, "%Y-%m")
        if str_data == month:
            transaction_by_month.append(trans)
            try:
                if transaction_by_month:
                    logging.info("Выполнена сортировка по дате")
                    for d in transaction_by_month:
                        if abs(d["Сумма операции"]) <= limit and abs(d["Сумма операции"]) % limit != 0:
                            total = limit - abs(d["Сумма операции"])
                            invest_total = abs(d["Сумма операции"]) + total
                            d["Округление на инвесткопилку"] = round(total, 2)
                            d["Сумма операции с округлением"] = invest_total
                        elif abs(d["Сумма операции"]) >= limit and abs(d["Сумма операции"]) % limit != 0:
                            total = limit - abs(d["Сумма операции"]) % limit
                            invest_total = abs(d["Сумма операции"]) + total
                            d["Округление на инвесткопилку"] = round(total, 2)
                            d["Сумма операции с округлением"] = invest_total
                        else:
                            d["Округление на инвесткопилку"] = 0
                            d["Сумма операции с округлением"] = d["Сумма операции"]
                        logging.info("Выполнен расчет кэшбэка по каждой категории.")
                        piggy_bank = 0
                    for t in transaction_by_month:
                        piggy_bank += t["Округление на инвесткопилку"]
                    for_answer = {"Инвесткопилка": {f"{month}": round(piggy_bank, 2)}}
                    json_piggy_bank = json.dumps(for_answer, indent=4, ensure_ascii=False)
                else:
                    raise ValueError
            except TypeError:
                print("Что-то не так.")
                logger.error("Видимо неверный формат даты.")
                json_piggy_bank = 0
            return json_piggy_bank


if __name__ == "__main__":
    transactions_from_excel()
    transactions_from_excel_into_list()
    investment_bank()


# if __name__ == '__main__':
#     print(transactions_from_excel("C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\ForworkKursovOperations.xlsx").shape)


# if __name__ == '__main__':
#     print(transactions_from_excel_into_list(
#     "C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\ForworkKursovOperations.xlsx"))


# if __name__ == '__main__':
#     print(investment_bank("2018-10", transactions_from_excel_into_list(
#     "C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\KursovOperations.xlsx"), 0))
