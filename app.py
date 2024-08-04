import streamlit as st
import pandas as pd
import numpy as np

def load_excel(file):
    if file == uploaded_file_final:
        return pd.read_excel(file, header=5)
    else:
        return pd.read_excel(file)

def highlight_differences(row):
    return ['color: black' if row[0] != row[1] else '' for _ in row]

def create_diff_column(df_v1, df_final):
    diff_columns = []
    for col in df_v1.columns:
        diff_columns.append(df_v1[col] != df_final[col])
    return pd.DataFrame(diff_columns).T

st.title("Questionnaire Comparison Tool")

uploaded_file_v1 = st.file_uploader("Upload Version 1 of the Questionnaire", type=["xlsx"])
uploaded_file_final = st.file_uploader("Upload Final Version of the Questionnaire", type=["xlsx"])

if uploaded_file_v1 and uploaded_file_final:
    df_v1 = load_excel(uploaded_file_v1)
    df_final = load_excel(uploaded_file_final)
    
    st.write("Version 1 of the Questionnaire")
    st.dataframe(df_v1)

    st.write("Final Version of the Questionnaire")
    st.dataframe(df_final)

    # Ensure the indices are aligned
    df_v1.reset_index(drop=True, inplace=True)
    df_final.reset_index(drop=True, inplace=True)

    #  Create a DataFrame with differences
    diff_df = create_diff_column(df_v1, df_final)
    diff_df.columns = [f"{col}_diff" for col in df_v1.columns]

    # Combine the datasets for better visualization
    combined_df = pd.concat([df_v1.add_suffix('_v1'), df_final.add_suffix('_final')], axis=1)

    # Apply highlighting function
    combined_df_styled = combined_df.style.apply(highlight_differences, axis=1)

    st.write("Combined DataFrame with Differences Highlighted")
    st.dataframe(combined_df_styled)

    # Function to print out the differences per column
    def print_differences(df_v1, df_final):
        differences_report = []
        for column in df_v1.columns:
            differences = df_v1[column] != df_final[column]
            if differences.any():
                differences_report.append(f"Differences in column: {column}")
                for i, diff in enumerate(differences):
                    if diff:
                        version_1_value = df_v1.at[i, column]
                        final_version_value = df_final.at[i, column]
                        if pd.notna(version_1_value) and pd.notna(final_version_value):
                            differences_report.append(f"Row {i+1}: Version 1 = {df_v1.at[i, column]}, Final Version = {df_final.at[i, column]}")
                differences_report.append("\n")
        return differences_report

    # Display the differences
    differences_report = print_differences(df_v1, df_final)
    for report in differences_report:
        st.write(report)

    def print_differences(df_v1, df_final):
        differences = []
        
        for column in df_v1.columns:
            col_diffs = df_v1[column] != df_final[column]
            if col_diffs.any():
                for i, diff in enumerate(col_diffs):
                    if diff:
                        version_1_value = df_v1.at[i, column]
                        final_version_value = df_final.at[i, column]
                        if pd.notna(version_1_value) and pd.notna(final_version_value):
                            differences.append({
                                'Row': i + 1,
                                'Column': column,
                                'Version 1': df_v1.at[i, column],
                                'Final Version': df_final.at[i, column]
                            })
                        
        # Convert the differences list to a DataFrame
        differences_df = pd.DataFrame(differences)
        return differences_df

    # Assuming df_v1 and df_final are already defined
    differences_df = print_differences(df_v1, df_final)

    # Display the differences in a table
    st.write("Differences between Version 1 and Final Version:")
    st.dataframe(differences_df)

