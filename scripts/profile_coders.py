import pandas as pd
from algorithms.elias_delta import EliasDeltaCoder
from algorithms.elias_gamma import EliasGammaCoder
from algorithms.golomb import GolombCoder
from algorithms.index_compression import IndexCompressionImplementor
from algorithms.unary import UnaryCoder
from tabulate import tabulate


def main():
    nums_lower_limit = int(input("Enter the Lower Limit of numbers :\t"))
    nums_upper_limit = int(input("Enter the Upper Limit of numbers :\t"))
    skip_value = int(input("Enter the Skip between numbers :\t"))
    default_b_value = int(input("Enter the Default 'b' value :\t"))

    data = []
    coders: list[IndexCompressionImplementor] = [
        UnaryCoder(),
        EliasGammaCoder(),
        EliasDeltaCoder(),
        GolombCoder(default_b_value),
    ]
    for coder in coders:
        for number in range(nums_lower_limit, nums_upper_limit + 1, skip_value):
            encoded = coder.encode(number)
            data.append(
                {
                    "Coder Name": str(coder),
                    "Number": number,
                    "Encoded Message": str(encoded),
                    "Message Size": len(encoded),
                }
            )

    df = pd.DataFrame(data)
    df.to_csv("docs/profile_coders.csv")

    del df["Encoded Message"]
    print(tabulate(df, headers="keys", tablefmt="fancy_grid"))


if __name__ == "__main__":
    main()
