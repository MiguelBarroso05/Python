from modules.data_import_module import load_csv, clean_and_process_data, save_to_database
from menus.interactions_menu import clean
import sqlite3
import os


def data_import_menu(db_path):
    table_name = "titanic_data"

    try:
        clean()
        file_name = input("Enter the name of the CSV file (example.csv): ")
        file_path = os.path.join("data", file_name)

        df = load_csv(file_path)
        if df is None:
            return 

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute(f"SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        if cursor.fetchone()[0] == 1:
            overwrite = input("Database already contains data.\nDo you want to overwrite? (y/n): ").lower()
            if overwrite != 'y':
                print("Operation canceled.")
                conn.close()
                return
            else:
                cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
                print("Existing data removed.\n")

        df = clean_and_process_data(df)
        save_to_database(df, conn, table_name)

        conn.close()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
