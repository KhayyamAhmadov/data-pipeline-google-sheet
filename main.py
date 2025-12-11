import sys
import json
from read_sheet import read_sheet
from write_local import write_to_csv, write_to_json
from update_sheet import update_sheet
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


def run_read(range_="A1:Z500"):
    print(f"Google Sheets-dən {range_} aralığı oxunur.")
    data = read_sheet(range_)
    print(data)

def run_write(range_="A1:Z500"):
    print(f"Google Sheets-dən {range_} aralığı oxunur və lokala yazılır.")
    data = read_sheet(range_)
    write_to_csv(data, "sheet_data.csv")
    write_to_json(data, "sheet_data.json")

def run_update():
    print("Google Sheets-ə JSON mapping ilə update edilir.")
    try:
        with open("update_config.json", "r", encoding="utf-8") as f:
            config = json.load(f)

        for u in config.get("updates", []):
            range_ = u["range"]
            values = u["values"]
            update_sheet(range_, values)
            print(f"V Updated {range_} -> {values}")

        print("Bütün updates tamamlandı!")

    except FileNotFoundError:
        print("X update_config.json tapılmadı!")
    except Exception as e:
        print("X Update zamanı xəta:", e)

def show_help():
    print("""
    İstifadə:
        python main.py read [RANGE]      → Sheet-dən oxu
        python main.py write [RANGE]     → Sheet-dən oxu + lokala yaz
        python main.py update            → JSON mapping ilə Sheet-ə update et

    Qeyd:
        RANGE optional-dir, default A1:Z500-dir
        Məsələn:
            python main.py read "A1:C10"
            python main.py write "A1:C20"
""")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
        sys.exit()

    command = sys.argv[1].lower()
    range_ = sys.argv[2] if len(sys.argv) > 2 else "A1:Z500"

    if command == "read":
        run_read(range_)
    elif command == "write":
        run_write(range_)
    elif command == "update":
        run_update()
    else:
        print("X Yanlış komanda!")
        show_help()
