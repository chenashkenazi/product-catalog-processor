import pandas as pd
from utils import parse_arguments


def regex_task(infile: str, out: str):
    try:
        df = pd.read_csv(infile)
        filtered_df = df[df["custom_5"].str.contains(r"knit", case=False, na=False) == False
                         | df["custom_5"].str.contains(r"knit.*jumper|jumper.*knit", case=False, na=False)]
        filtered_df.to_csv(out, index=False)
        print(f"Filtered products saved to {out}")
    except Exception as ex:
        raise Exception(f"Error in regex_task: {str(ex)}")


if __name__ == '__main__':
    args = parse_arguments()
    try:
        regex_task(infile=args.infile, out=args.out)
    except Exception as ex:
        print(str(ex))
