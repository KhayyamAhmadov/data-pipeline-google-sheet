import csv
import pandas as pd

def write_csv(data, filename="output.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print(f"Data CSV-yə yazıldı: {filename}")

def write_excel(data, filename="output.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Data Excel-ə yazıldı: {filename}")
