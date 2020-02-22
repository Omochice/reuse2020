import pandas as pd
import json
import os
from collections import Counter

pwd = os.path.dirname(os.path.abspath(__file__))

csv_file = os.path.join(pwd, "data.csv")
category_file = os.path.join(pwd, "category.json")


def load_filled_csv(csv_name: str = csv_file):
    df = pd.read_csv(csv_name)
    return df.fillna("")


def get_n_contents():
    df = load_filled_csv(csv_file)
    counter = Counter(df.query("not status == '売約済み'")["カテゴリ"])
    d = load_category_list()
    ## [{en: A, jp:冷蔵庫, n_content: 10}]
    return [{"en": en, "jp": jp, "n_content": counter[en]} for (en, jp) in d]


def get_category(key: str) -> list:
    df = load_filled_csv(csv_file)
    return df.query(f"カテゴリ == '{key}' and not status == '売約済み'").values.tolist()


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
