import pandas as pd
from zipfile import ZipFile
import os
from typing import ByteString
import seaborn as sns
import matplotlib.pyplot as plt


def uncompress_file():
    with ZipFile("archive.zip") as z:
        z.extractall()
    z.close()


def read_file(filepath: str | ByteString = os.getcwd()) -> pd.DataFrame:
    files: list[str] = list(
        filter(
            lambda x: x if x.endswith(".csv") else None,
            [f for f in os.listdir(filepath)],
        )
    )

    df = [pd.read_csv(f) for f in files]

    return pd.concat(df)


def main():
    if not os.path.exists("credit_card_transactions.csv"):
        uncompress_file()
    df = read_file()
    ax = sns.barplot(data=df, x="category", hue="gender", y="amt", ci=None)
    print(ax.containers)
    ax.bar_label(ax.containers[0], fmt="%.2f", label_type="center", color="black")
    ax.bar_label(ax.containers[1], fmt="%.2f", label_type="center", color="black")

    plt.show()


if __name__ == "__main__":
    main()
