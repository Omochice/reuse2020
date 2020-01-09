import pandas as pd
import json

filename = "test.csv"


def load_filled_csv(csv_name: str):
    df = pd.read_csv(csv_name)
    return df.fillna("")


def get_category(key: str) -> list:
    df = load_filled_csv(filename)
    return df.query(f"カテゴリ == '{key}'").values.tolist()


def get_item(key: str) -> list:
    df = load_filled_csv(filename)
    return df.query("ID == @key").values.tolist()[0]


def translate_catogory_name(category_name: str) -> str:
    with open("category.json", "r") as f:
        d = json.load(f)
    d = {item[0]: item[1] for item in d}
    return d[category_name]


if __name__ == "__main__":
    print(get_category("A"))
    print(get_item("4"))
