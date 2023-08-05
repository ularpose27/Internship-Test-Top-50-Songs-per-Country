# Internship Test, Top 50 Songs per Country

This project has the objective of computing, on a daily basis, the top 50 songs that have been most listened to in each country over the last 7 days.

## Requirements

To run the script, you need the following:

- Python 3.x
- pandas library

## Installation

1. Clone this repository to your local machine or download the script directly.
2. Make sure you have Python installed. If not, download and install it from the official website (https://www.python.org/downloads/).
3. Install the pandas library by running the following command in your terminal or command prompt:

```bash
pip install pandas
```

## Usage

1. Prepare your log file: The log file should contain streaming data with three elements per line, separated by a pipe `|`. The three elements represent SongID, UserID, and Country.

2. Run the script: Execute the script by running the following command in your terminal or command prompt:

```bash
python main.py
```

3. Input filename: When prompted, enter the name of your log file, including the extension (e.g., `log_file.txt`). Press Enter to proceed.

4. Results: The script will read the log file, process the data, and generate separate text files for each country with the top 50 songs and their respective stream counts. The output files will be named in the format `country_top50_YYYYMMDD.txt`, where `YYYYMMDD` represents the current date.

## Daily Top 50 Songs

This project is designed to provide daily updates on the top 50 most-listened songs in each country over the last 7 days. As you run the script on a daily basis, the generated output files will contain the latest data reflecting the most listened songs by country

## Sample Log File Format

The log file should follow this format:

```
SongID|UserID|Country
1111|1001|US
3333|1002|US
2222|1003|UK
1111|1004|UK
3333|1005|UK
4444|1006|US
...
```

## Important Notes

- If the log file contains lines with invalid formats or missing elements, the script will print error messages and skip those lines.
- The script will drop any rows with missing data (NaN) before generating the top 50 lists.
- The `SongID` and `UserID` should be integers. Any non-integer values will be skipped.
- The `Country` names will be converted to uppercase for consistency.
- Make sure to use the script named `main.py` to run the code.
-For the purpose of trying the script, please use the file named sample_listen-2021-12-01 copy.txt


