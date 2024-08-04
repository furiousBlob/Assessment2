# Questionnaire Comparison Tool
This Streamlit app allows you to compare two versions of a questionnaire by uploading Excel files. The app highlights differences between the versions and provides detailed reports on discrepancies.

## Accessing the App

The app is deployed online and can be accessed at:

[Visit the Questionnare Comparison Interface](https://assessment2-gdzf.onrender.com)

## Using the App

### Upload Version 1 of the Questionnaire

- Click the "Upload Version 1 of the Questionnaire" button.
- Select the Excel file containing the first version of the questionnaire.

### Upload the Final Version of the Questionnaire

- Click the "Upload Final Version of the Questionnaire" button.
- Select the Excel file containing the final version of the questionnaire.

## View Results

The app will display both versions of the questionnaire.
It will show a combined DataFrame with differences highlighted.
A detailed table of differences between the two versions will be provided.

## Script Overview
### Functions
- load_excel(file): Loads an Excel file into a DataFrame.
- highlight_differences(row): Highlights differences between two rows.
- create_diff_column(df_v1, df_final): Creates a DataFrame showing the differences between two DataFrames.
- print_differences(df_v1, df_final): Prints differences between two DataFrames.
- print_differences(df_v1, df_final) (Second definition): Returns a DataFrame with detailed differences.

## Features
- Comparison: Compares two versions of the questionnaire and highlights differences.
- Visualization: Displays a styled DataFrame where differences are highlighted.
- Reporting: Provides a detailed report of differences between the two versions in a tabular format.

## Running Locally

If you want to run the Streamlit app locally, ensure you have the following packages installed:

- `pandas`
- `streamlit`
-  `numpy`

You can install these packages using pip:

```bash
pip install pandas streamlit numpy
```

Then, run the app with:

```bash

streamlit run app.py
```

## Jupyter Notebooks
For further analysis and visualization, Jupyter notebooks are available that use Matplotlib to generate insights and heatmaps. These notebooks can be executed in a Jupyter environment.