# Financial Data Analysis

This Python script performs financial data analysis on historical stock data, including calculating Simple Moving Averages (SMA) and Relative Strength Index (RSI). The analysis is based on a provided CSV file containing historical stock data.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [License](#license)

## Introduction

The Financial Data Analysis script is designed to analyze historical stock data stored in a CSV file. It calculates Simple Moving Averages (SMA) with a 5-day window and Relative Strength Index (RSI) with a 14-day window. The results are then written to separate CSV files for further analysis or visualization.

## Features

- Load historical stock data from a CSV file.
- Calculate Simple Moving Averages (SMA) for a 5-day window.
- Calculate Relative Strength Index (RSI) for a 14-day window.
- Write SMA and RSI results to separate CSV files.

## Requirements

- Python 3.x
- Required Python packages are listed in `requirements.txt` and can be installed using:

  ```bash
  pip install -r requirements.txt
Usage
Clone the repository:

bash
git clone https://github.com/your-username/financial-data-analysis.git
cd financial-data-analysis
Install dependencies:

bash

pip install -r requirements.txt
Run the script:

bash

python financial_analysis.py
The script will load historical data from the provided CSV file ("orcl.csv" in this example), calculate SMA and RSI, and save the results in "orcl-sma.csv" and "orcl-rsi.csv," respectively.

File Descriptions
financial_analysis.py: The main Python script containing functions for loading data, calculating SMA and RSI, and writing results to CSV files.
orcl.csv: Example CSV file containing historical stock data.
orcl-sma.csv: Output file containing Simple Moving Averages (SMA) results.
orcl-rsi.csv: Output file containing Relative Strength Index (RSI) results.
License
This project is licensed under the MIT License.

vbnet


Make sure to replace placeholder names like "financial_analysis.py" and "orcl.csv" w
