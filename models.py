import pandas as pd

filename = "test.csv"


def get_category(key: str) -> list:
    df = pd.read_csv(filename)
    return df.query(f"category == '{key}'").values.tolist()


def get_item(key: str) -> list:
    df = pd.read_csv(filename)
    return df.query(f"id == '{key}'").values.tolist()


if __name__ == "__main__":
    print(get_category("A"))
