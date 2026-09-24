# Power BI guide for the web app shown in your screenshot

I prepared `PowerBI_Import_Workbook.xlsx` in this folder. It contains the cleaned data as named Excel tables on separate sheets, plus country and year dimensions. This is the fastest route from the Power BI web home screen.

## Import the project tables

1. In the left navigation, click **My workspace**.
2. Choose **New item** (or **New**) → **Semantic model**.
3. Choose **Excel** and select `PowerBI_Import_Workbook.xlsx` from this folder. The workbook contains formatted tables so Power BI can import the sheets as separate model tables.
4. Preview the data and continue with **Create a report** (or create the semantic model, then choose **Create report** beside it).
5. Save the report in **My workspace** as `Vaccination Analysis`.

Microsoft's web workflow supports importing a workbook with one or more Excel tables and creating a semantic model from it. If your screen only offers a single CSV or only a semantic model you cannot edit, stop and use Power BI Desktop for the full multi-table report. [Excel/web import guide](https://learn.microsoft.com/en-us/power-bi/create-reports/service-report-create-new) · [semantic models from Excel/CSV](https://learn.microsoft.com/en-us/power-bi/connect-data/service-datasets-understand).

## Check the model

The workbook has these tables: `Coverage_Admin`, `Candidate_Association`, `Disease_Cases`, `Incidence_Rates`, `Vaccine_Intro`, `Vaccine_Schedule`, `DimCountry`, and `DimYear`.

In Model view (if available), ensure these one-to-many relationships exist, with dimensions on the 1 side and single-direction filtering:

- `DimCountry[code]` → each fact table's `code` column.
- `DimYear[year]` → each fact table's `year` column.

Do not connect disease and coverage fact tables directly. The candidate table already contains the explicit country-year vaccine/disease pairs for a descriptive scatter plot. Country dimension includes the countries mapped in the introduction source; coverage records with no mapped WHO region can show blank region.

## Build four report pages

Use the **Visualizations** and **Data** panes. Add a visual, then drag fields to its Axis, Values, Legend, or Location buckets. Add slicers by choosing the Slicer visual and dragging in the relevant field.

### Page 1 — Coverage Overview
- Card: median of `Coverage_Admin[coverage]` (restrict to 0–100 for this display and disclose the restriction).
- Line chart: `year` on X-axis; median `coverage` on Y-axis; `antigen` as legend or slicer.
- Slicers: `DimYear[year]`, `DimCountry[who_region]`, country name, antigen.

### Page 2 — Low-Coverage Prioritization
- Table with country, WHO region, year, antigen, target number, doses, coverage.
- Sort coverage ascending; filter to a chosen year and relevant antigen.
- Keep a data-quality note/table for values below 0 or above 100 and doses greater than targets. These are review flags, not proof all over-100 values are errors.

### Page 3 — Disease Outcomes
- Line chart from `Disease_Cases`: year by sum of cases, with disease as legend/slicer.
- Separate line chart from `Incidence_Rates`: year by median incidence, filtered to one disease and its denominator.
- Scatter chart from `Candidate_Association`: coverage on X, incidence_rate on Y, disease or antigen as legend. Add a visible note: “Country-level ecological association; not causal effectiveness evidence.”

### Page 4 — Program Readiness
- Bar chart from `Vaccine_Intro`: WHO region by count of Intro = Yes, or a table of country, vaccine description, year, intro status.
- Bar chart from `Vaccine_Schedule`: schedule rounds by row count and target-population description.
- Note that schedule rows are planned schedules, not completed doses.

If the web editor cannot create measures, use the field dropdown in the visual's Values bucket to change the aggregation to **Median**, **Count**, or **Sum**. Keep incidence filtered by disease/denominator; keep the 95% goal for measles-relevant coverage only.

## Save and obtain the deliverable

Save the report. Check whether **File → Download this file** is available and whether the dialog offers a `.pbix` with data. Power BI Service restricts PBIX downloads for some file-upload/report scenarios; if the option is unavailable, the web report can still be saved in My workspace, but it may not satisfy a requirement for a native PBIX. Use Power BI Desktop if available to produce the PBIX. [Microsoft PBIX download limits](https://learn.microsoft.com/en-us/power-bi/create-reports/service-export-to-pbix).

Finally, add `Vaccination_Analysis.pbix` to the Drive submission folder if you obtain one. Do not claim the PBIX is included unless the file is actually there.
