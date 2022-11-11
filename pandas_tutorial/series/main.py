import pandas as pd


def key_value(data_in: dict):
    return pd.Series(data_in, index=['day1', 'day2'])


def main(data_in: list):
    return pd.Series(data_in, index=['x', 'y', 'z'])


def create_data_frame(data_in: dict):
    return pd.DataFrame(data_in)


if __name__ == "__main__":
    data = [1, 7, 4]
    result = main(data)
    print(result)
    print(result[0])
    print(result['y'])
    data = calories = {"day1": 420, "day2": 380, "day3": 390}
    result = key_value(data)
    print('Key value dict as data')
    print(result)

    print('Create data frame')
    data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
    }
    result = create_data_frame(data)
    print(result)
