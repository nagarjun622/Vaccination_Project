# Vaccination Data Analysis

An exploratory data analysis project examining reported vaccination coverage, reported disease cases, incidence rates, vaccine introduction, and national vaccine schedules. The repository includes a saved analysis notebook, cleaned data extracts, SQL examples, a Power BI import workbook, and a static dashboard export.

> **Interpretation note:** These are descriptive analyses of reported data. They do not establish that vaccination caused a change in disease outcomes or measure vaccine effectiveness.

## Project overview

The project brings together five supplied workbook topics:

- Vaccination coverage
- Reported disease cases
- Disease incidence rates
- Vaccine introduction status
- Vaccine schedules

The workflow prepares reusable cleaned extracts, explores data quality and trends in Python, supports relational queries with SQLite/SQL, and provides a workbook structured for Power BI.

## Repository contents

| Path | Purpose |
|---|---|
| `Vaccination_EDA_Submission.ipynb` | Main exploratory analysis notebook, including saved outputs and interpretations. |
| `Vaccination Data Analysis Dashboard.pdf` | Static, shareable export of the Power BI report. |
| `PowerBI_Import_Workbook.xlsx` | Multi-table workbook prepared for import into Power BI. |
| `PowerBI_Build_Guide.md` | Notes for importing the workbook and building the interactive report. |
| `cleaned_data/` | Cleaned source extracts and derived analysis tables in CSV format. |
| `prepare_data.py` | Python data-preparation script. |
| `database_schema.sql` | SQLite schema definition. |
| `analysis_queries.sql` | Example analytical SQL queries. |
| `data_quality_summary.json` | Summary of dataset sizes, missing values, and preparation notes. |

The original source workbooks and the SQLite database are not included in this GitHub repository. The project submission folder shared separately may contain additional files.

## Analyses and outputs

The notebook and prepared tables support exploration of:

1. Coverage patterns by year, country, antigen, and region where available.
2. Reported case counts and incidence over time.
3. Country-level coverage and incidence comparisons for descriptive exploration.
4. Vaccine introduction status and schedule characteristics.
5. Data completeness, unusual values, and preparation assumptions.

The Power BI PDF is a static view of the dashboard. The Excel import workbook is provided to support the Power BI model; a native `.pbix` file is not included.

## Data quality and limitations

- Some reported coverage values exceed 100%, with extreme values reaching approximately 32,000% in the supplied data. These values require source verification; they may reflect reporting or denominator issues. Do not interpret them as plausible population coverage.
- The supplied data include an unusually large target-population value (approximately 11.7 trillion); investigate and flag it rather than treating it as valid without verification.
- Summary statistics across countries or records are generally unweighted unless explicitly stated. They should not be described as population-weighted estimates.
- Coverage and disease measures may differ in country, year, antigen/disease, and denominator coverage. Comparisons should only be made after checking that records are comparable.
- Country-level associations are ecological and descriptive. They cannot demonstrate individual-level effects or causation.
- The supplied workbooks do not provide all potentially relevant variables, including gender, education, urban/rural status, population density, socioeconomic group, and monthly observations.
- Missing values, excluded rows, and filters should be reviewed in the notebook before reusing a result.

## Reproducing the analysis

### Requirements

- Python 3.10 or newer is recommended.
- Jupyter Notebook or JupyterLab.
- Python packages used by the notebook and preparation script: `pandas`, `numpy`, `matplotlib`, `seaborn`, and `openpyxl`.

Install the packages in a virtual environment if needed:

```bash
python -m venv .venv
```

Activate the environment, then install dependencies:

```bash
python -m pip install pandas numpy matplotlib seaborn openpyxl jupyter
```

Launch Jupyter from the repository root:

```bash
jupyter notebook
```

Open `Vaccination_EDA_Submission.ipynb` and run cells in order. The repository contains cleaned CSV extracts under `cleaned_data/`; if a notebook cell requests the original Excel workbooks, obtain them from the separately shared project data folder and follow the file paths described in the notebook or `PowerBI_Build_Guide.md`.

### SQL

Use `database_schema.sql` for the database table structure and `analysis_queries.sql` for example queries. The SQLite database itself is omitted from GitHub; generate or obtain it using the preparation workflow and the original datasets before executing queries against a local database.

## Power BI

Use `PowerBI_Import_Workbook.xlsx` with Power BI to inspect the model tables and build or update the report. The repository contains a PDF export for convenient viewing. It does not contain an editable `.pbix` file.

## How to cite or reuse

This repository is an educational project. Cite the original data provider(s) identified in the source workbooks and assignment materials when reusing the data or findings. Check the terms of the original data before redistribution. No additional software license is specified in this repository.

## Submission note

This GitHub repository is the code and analysis copy. Refer to the separately shared Google Drive submission folder for any additional deliverables required by the course, including the explanation video. Confirm that your instructor can access both links.
