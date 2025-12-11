import csv
import json

def write_to_csv(data, filename="data.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f"CSV yazıldı: {filename}")

def write_to_json(data, filename="data.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"JSON yazıldı: {filename}")