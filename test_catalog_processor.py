import pandas as pd


def test_price_column():
    df = pd.read_csv("python_home_task_file_with_price.csv")
    assert "price_edited" in df.columns, "Column 'price_edited' is missing!"
    assert all(df["price_edited"] == df["search_price"].astype(float)), "'price_edited' values are incorrect"


def test_knitwear_without_jumpers():
    df = pd.read_csv("python_home_task_file_regex.csv")
    assert "custom_5" in df.columns, "Column 'custom_5' is missing!"
    for value in df["custom_5"].dropna():
        if "knit" in value.lower() and "jumper" not in value.lower():
            assert False, f"Found 'knit' without 'jumper': {value}"
