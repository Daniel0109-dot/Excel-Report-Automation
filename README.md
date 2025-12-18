# Excel Administrative Report Automation

**Overview**

This project automates the processing of administrative Excel spreadsheets by applying predefined business rules, normalizing data, and generating structured outputs segmented by organizational criteria (such as directorates or departments).

The automation was designed to replace repetitive manual work commonly found in administrative and HR-related routines, improving consistency, reducing errors, and saving operational time.

Although originally inspired by real-world corporate needs, the project has been adapted and generalized to be safely shared as a portfolio example.

**Problem Statement**

Administrative teams often work with multiple Excel files generated from different sources, formats, or systems. Common issues include:

- Inconsistent column name and data formats
- Manual filtering and merging of spreadsheets
- Repetitive application of the same business rules
- Error-prone copy-and-paste workflows

These tasks are time-consuming, difficult to audit, and scale poorly as data volume increases.

**Solution**

This project provides a Python-based automation that:
- Reads Excel files from predefined directories
- Normalizes textual and date fields
- Applies business rules to classify and filter records
- Consolidates data into a structured "database-like" spreadsheet
- Generates output files organized by business logic (e.g., per directorate)

The goal is not to replace full BI systems, but to offer a lightweight, transparent, and easily adaptable automation layer.

**Features**

- Automatically detects and loads the most recent Excel file from the input directory
- Standardizes and normalizes column names for consistent processing
- Infers missing business attributes based on predefined rules
- Filters and organizes essential data fields
- Groups records according to business logic and responsibility mappings
- Generates structured Excel reports with safe and readable filenames
- Uses date-based naming conventions to improve file organization

**Technologies Used**

To run this project locally, you will need:
- **Python 3.10 or higher**
- **Excel (.xlsx)** - Input/Output format
- **pandas** - Data manipulation
- **openpyxl** - Excel file handling

**Prerequisites**
- Python 3.10 or higher
- Basic command-line usage
- Excel files following a known structural pattern

These dependencies can be installed using 'pip'.

**Installation**

1. Clone this repository:

git clone https://github.com/Daniel0109-dot/Excel-Report-Automation.git

2. Navigate to the project directory:

cd Excel-Report-Automation

3. Install the required dependencies:

pip install -r requirements.txt

**Usage**

1. Place the input Excel files inside the `input/` directory.

2. Run the main script:

python main.py

3. Find generated reports in output/generated_reports/

**Project Structure**

```text
excel-report-automation/
├── input/
│   └── example_files/
│
├── output/
│   └── generated_reports/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── file_loader.py
│   ├── text_utils.py
│   ├── data_cleaning.py
│   ├── business_rules.py
│   └── report_generator.py
│
├── main.py
├── requirements.txt
├── README.md
├── README_PT.md
├── .gitignore
└── LICENSE
```
The Project follows a modular structure, separating data loading, cleaning,business rules, and report generation to improve readability and maintenance.
 
**Design Decisions**

- Modular architecture: Each step of the process(loading, cleaning, rules, output) is isolated to improve readability and maintainability.
- Explicit business rules: Rules are written in code instead of hidden in Excel formulas, making them easier to audit and change.
- Deterministic behavior: No probabilistic models are used; the same input always produces the same output.
- Human-readable outputs: Generated files prioritize clarity over compression or performance.

**Known Limitations**

- Input Excel files are expected to follow a known structural pattern
- Business rules are static and coded directly(no external configuration yet)
- No automatic schema validation is performed
- Error handling is intentionally simple to keep the logic transparent

**Future Improvements**

- External configuration of rules via JSON or YAML
- Structured logging and execution reports
- Automated schema validation
- Optional integration with Power Automate or cloud storage

**License**

This project is licensed under the MIT License.
You are free to use, modify, and distribute this software with proper attribution.

**Disclaimer**

This project is a generalized and anonymized version of real administrative automations. No proprietary data, internal processes, or confidential information are included.

**Author**

Developed as a part of a professional portfolio focused on process automation and administrative data analysis.
