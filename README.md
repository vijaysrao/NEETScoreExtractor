# NEETScoreExtractor

## Summary
A Python program to extract NEET UG scores

## Background
National Testing Agency of India published NEET-UG scores across all examination centres based on Supreme Court's order. The scores can be downloaded [here](https://neet.ntaonline.in/frontend/web/common-scorecard/index).

## Program
This program can parse recursively into folders, read the .pdf files and saves a Comma Separated Value (.csv) file for further analysis.
The csv file has the following format:
<test-center-number>,<score-1>,<score-2>,...

## How to use
1. Download the scores pdf files of interest to a folder (e.g., ~/NEET in Linux or Documents/NEET/ in Windows). If need be, you can create subfolders, say one per district, and store the relevant score pdf files in that.
2. Download `results.py` program into NEET folder
3. Open a command prompt in the NEET folder and run `python results.py`

## Dependencies
The first dependency is that you should install Python 3.10+ version and pip. Download [here](https://www.python.org/). Search Google for relevant instructions.

In case you get errors on a missing package, you should install PyPDF2, `pip install PyPDF2`.

## Using the output
Once the results.py is run completely, a file `data.csv` is created in the same folder. Open it in Excel or your favorite spreadsheet or scientific computing tools like MATLAB. And enjoy analyzing the data!
