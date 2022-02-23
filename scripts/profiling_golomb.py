import sys

import pandas as pd
import plotly.express as px
from algorithms.golomb import GolombCoder


def main(args: list[str]):
    max_num_check = int(args[0])
    max_b_value = int(args[1])

    data = []
    for b in range(1, max_b_value + 1):
        coder = GolombCoder(b)
        for n in range(1, max_num_check + 1):
            encoded = coder.encode(n)
            data.append(
                {
                    "Coder Name": str(coder),
                    "Number": n,
                    "Encoded Message": str(encoded),
                    "Message Size": len(encoded),
                }
            )

    df = pd.DataFrame(data)
    df.to_csv("docs/profiling_golomb.csv")
    px.line(
        df, x="Number", y="Message Size", color="Coder Name", title="Golomb on `b`"
    ).show()


if __name__ == "__main__":
    main(sys.argv[1:])
