import pandas as pd
from datetime import datetime, timedelta


def load_csv(file_path):
    """
    Loads a CSV file into a DataFrame.
    """
    try:
        if not file_path.endswith(".csv"):
            raise ValueError("Invalid file type. Please provide a .csv file.")

        df = pd.read_csv(file_path)
        print("CSV file loaded successfully.")
        return df
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")


def clean_and_process_data(df):
    """
    Cleans and preprocesses the DataFrame:
    - Fills missing values.
    - Converts column types.
    - Creates a new column 'Age_Milliseconds' representing age in milliseconds since the Epoch.
    """
    try:
        # Fill missing values
        if 'Age' in df.columns:
            df['Age'] = df['Age'].fillna(df['Age'].mean())

        if 'Fare' in df.columns:
            df['Fare'] = df['Fare'].fillna(0)

        df = df.fillna("Unknown")

        # Convert column types
        if 'Age' in df.columns:
            df['Age'] = df['Age'].astype(float)

        if 'Pclass' in df.columns:
            df['Pclass'] = df['Pclass'].astype(int)

        # Create 'Age_Milliseconds' column using the epoch
        epoch = datetime(1970, 1, 1)
        if 'Age' in df.columns:
            df['Age_Milliseconds'] = df['Age'].apply(
                lambda age: int((epoch + timedelta(days=age * 365.25)).timestamp() * 1000)
            )

        print("Data preprocessing complete. Column 'Age_Milliseconds' added.")
        return df
    except Exception as e:
        print(f"An error occurred during data cleaning: {e}")


def save_to_database(df, conn, table_name):
    """
    Saves a DataFrame to an SQLite database.
    """
    try:
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        print("Data successfully saved to the database.")
    except Exception as e:
        print(f"An error occurred while saving to the database: {e}")
