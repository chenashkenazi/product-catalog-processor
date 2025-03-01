import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", required=True, help="Input file")
    parser.add_argument("--out", required=True, help="Output file")
    return parser.parse_args()
