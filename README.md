# Product Catalog Processor

This project processes a TSV file containing a clothing catalog and applies specific modifications to its data.

## Tasks
1. csv-task:

   This task processes the file `python_home_task_file.tsv`, and its output is saved as `python_home_task_file_with_price.csv`.

   It performs the following operations:
      - Converts the TSV catalog file to CSV
      - Adds a column named `price_edited` which contains all the values from the `search_price` column
2. regex-task:

   This task processes the file `python_home_task_file.csv`, and its output is saved as `python_home_task_file_regex.csv`.

   It performs the following operation:
    - Removes all the knit products without jumpers from the `python_home_task_file.csv` file.

## How to run

Clone the git repository: paste the following command in your terminal:
```bash
git clone https://github.com/chenashkenazi/product-catalog-processor.git
```

Then, navigate to the project directory:
```bash
cd product-catalog-processor
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the csv-task:
```bash
python csv-task.py --infile python_home_task_file.csv --out python_home_task_file_with_price.csv
```

Run the regex-task:
```bash
python regex-task.py --infile python_home_task_file.csv --out python_home_task_file_regex.csv
```

Optional: run unit tests to make sure everything went well:
```bash
pytest test_catalog_processor.py
```

Thank you for the opportunity!
