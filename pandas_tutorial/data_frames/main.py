import pandas as pd


def main(data_in: dict):
    return pd.DataFrame(data_in)


def read_csv():
    return pd.read_csv('data_frames/data.csv')


def named_index():
    data_in = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
    }
    return pd.DataFrame(data_in, index=["day1", "day2", "day3"])


if __name__ == "__main__":
    data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
    }

    result = main(data)
    print(result)
    print(result.loc[0])
    print(result.loc[[0, 1]])

    print('Named indexes')
    df = named_index()
    print(df)
    # refer to the named index:
    print(df.loc["day2"])

    csv_result = read_csv()
    print(csv_result)