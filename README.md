# Automation Test Language

## Introduction

This is guideline for running/developing automation testing for the Automation Test project (in this time, it is only in prototype level).

Automation Test Language is an automated testing project using `pytest` and `selenium`. This project helps run test cases for verifying mutiple languages for website, generate test reports in XML format, and convert them to Excel.

## System Requirements

- Python 3.10.4
- `pip` for installing dependencies

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/BaGiaXiTrum99/AutomationTestLanguage_Selenium.git
   cd AutomationTestLanguage_Selenium
   ```

2. Create Virtual Environment:

   For Windows:

   ```cmd
   python -m venv .venv
   .venv\Scripts\activate
   ```

   For Linux:

   ```sh
   python -m venv .venv
   .venv/bin/activate
   ```

3. Install dependencies:

   For Windows:

   ```cmd
   pip install -r requirements.txt
   ```

   For Linux:

   ```sh
   source setup.sh
   ```

4. Copy contents from file `.env.example` to `.env`, edit username and password for bypassing proxy.

5. If using Linux, need set permission:
   ```sh
   sudo chmod -R 777 .
   ```

## Usage

### Run all test cases

```sh
python main.py
```

### Run all test cases in specific folder

- Go to `main.py` file, edit the `TEST_FOLDER = "tests"` to path of subfolder in your test folder.

### Create new test case
- Refer to sample test case at `tests/questions.py`.
- Add `.json` at `data` in case you need to run more language.
- Rename `.json` to `.json.bk` in case you don't need to run that language.

### Test Report

- Test results will be saved in `./reports/report_<time>.xml`, for any customization report.
- After running `python main.py`, the report will be converted to Excel.

## Project Structure

```text
lux_automation_test/
│── tests/ # Folder containing test cases
│── reports/ # Folder storing test reports
│── main.py # Script to execute tests
│── requirements.txt # List of required dependencies
│── setup.sh # Setup script (if applicable)
│── README.md # User guide document
```
