import pandas as pd


def main():
    return pd.read_csv('read_csv/data.csv')


if __name__ == "__main__":
    result = main()
    print(pd.options.display.max_rows)
    print(result.to_sql('name_1', 'con_1'))
