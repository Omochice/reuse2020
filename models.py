import pandas as pd
import json
import os

pwd = os.path.dirname(os.path.abspath(__file__))

csv_file = os.path.join(pwd, "test.csv")
category_file = os.path.join(pwd, "category.json")


def load_filled_csv(csv_name: str):
    df = pd.read_csv(csv_name)
    return df.fillna("")


def get_category(key: str) -> list:
    df = load_filled_csv(csv_file)
    return df.query(f"カテゴリ == '{key}'").values.tolist()


def get_item(key: str) -> list:
    df = load_filled_csv(csv_file)
    return df.query("ID == @key").values.tolist()[0]


def translate_catogory_name(category_name: str) -> str:
    d = load_category_list()
    d = {item[0]: item[1] for item in d}
    return d[category_name]


def load_category_list() -> list:
    with open(category_file, "r") as f:
        d = json.load(f)
    return d


if __name__ == "__main__":
    print(get_category("A"))
    print(get_item("4"))
