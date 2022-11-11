import pandas as pd


def main():
    my_dataset = {
        'cars': ["BMW", "Volvo", "Ford"],
        'passings': [3, 7, 2]
    }

    my_var = pd.DataFrame(my_dataset)

    print(my_var)


if __name__ == '__main__':
    main()