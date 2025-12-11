from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from config import sheets_id, scopes

service_account_file = 'keys.json'

def get_sheet_service():
    credentials = Credentials.from_service_account_file(
        service_account_file, scopes=scopes
    )
    service = build('sheets', 'v4', credentials=credentials)
    return service.spreadsheets()

def update_sheet(range_name, values):
    sheet = get_sheet_service()
    body = {'values': values}
    result = sheet.values().update(spreadsheetId=sheets_id, range=range_name, valueInputOption="RAW", body=body).execute()
    print(f"{result.get('updatedCells')} hüceyrə yeniləndi")
