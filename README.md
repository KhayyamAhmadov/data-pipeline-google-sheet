### Bu Python kodları Google Sheets-dən data oxuyur, lokala yazır (CSV/JSON) və update edir.

### Update əməliyyatları JSON mapping ilə idarə olunur, yəni hansı hüceyrələr update olunacaqsa update_config.json-da göstərilir.


- main.py                   Əsas run ediləcək script
- read_sheet.py             Google Sheets-dən oxuma funksiyaları
- write_local.py            CSV və JSON-lokala yazma funksiyaları
- update_sheet.py           Google Sheets-ə update funksiyaları
- update_config.json        Update mapping (range və values)
- config.py                 sheets_id və scopes təyin olunur

---

## Quraşdırma

- Virtual environment yaradın:

```bash
python -m venv venv
```

- Virtual environment-e daxil olmaq:
```bash
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

- Lazımi paketləri quraşdırın:
```bash
pip install -r requirements.txt
```

- config.py faylında:
```bash
sheets_id = "YOUR_SHEET_ID"
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
```

- Google Service Account açarını keys.json olaraq yerləşdirin.

---

## İstifadə qaydası (terminalda):
## 1️⃣ Read etmək

- Default range (A1:Z500) ilə oxumaq:
```bash
python main.py read
```

- Müəyyən range ilə oxumaq:
```bash
python main.py read "A1:C10"
```

---

## 2️⃣ Write etmək (lokala CSV + JSON)

- Default range (A1:Z500) ilə:
```bash
python main.py write
```

- Müəyyən range ilə:
```bash
python main.py write "A1:C20"
```

- Lokala yazılan fayllar:
```bash
sheet_data.csv

sheet_data.json
```

---

## 3️⃣ Update etmək (JSON mapping ilə)

- update_config.json faylında update etmək istədiyiniz hüceyrələri və dəyərləri qeyd edin:
```bash
{
  "updates": [
    {"range": "A1", "values": [["Hello"]]},
    {"range": "B2:C2", "values": [["Foo","Bar"]]}
  ]
}
```

- Update əməliyyatı:
```bash
python main.py update
```
- Script bütün mapping-ləri oxuyub Google Sheet-ə update edəcək.
