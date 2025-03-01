import pandas as pd
from pandas import DataFrame
from utils import parse_arguments


def csv_task(infile: str, out: str) -> None:
    try:
        df = convert_tsv_to_csv(infile="python_home_task_file.tsv", outfile=infile)
        add_price_edited_column(df=df, out=out, infile=infile)
    except Exception as ex:
        raise ex


def convert_tsv_to_csv(infile: str, outfile: str) -> DataFrame:
    try:
        df = pd.read_csv(infile, sep="\t")
        df.to_csv(outfile, index=False)
        print("Successfully made csv file.")
        return df
    except Exception as ex:
        raise Exception(f"Error in convert_tsv_to_csv: {str(ex)}")


def add_price_edited_column(df: DataFrame, out: str, infile: str) -> None:
    try:
        df["price_edited"] = pd.to_numeric(df["search_price"], errors="coerce")
        df.to_csv(out, index=False)
        print(f"Successfully converted {infile} to {out} with 'price_edited' column.")
    except Exception as ex:
        raise Exception(f"Error in add_price_edited_column: {str(ex)}")


if __name__ == '__main__':
    args = parse_arguments()
    try:
        csv_task(infile=args.infile, out=args.out)
    except Exception as ex:
        print(str(ex))
