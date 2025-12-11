from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from config import sheets_id, scopes

service_account_file = 'keys.json'

def get_sheet_service():
    credentials = Credentials.from_service_account_file(service_account_file, scopes=scopes)
    service = build('sheets', 'v4', credentials=credentials)
    return service.spreadsheets()

def read_sheet(range_name="A1:Z500"):
    sheet = get_sheet_service()
    result = sheet.values().get(spreadsheetId=sheets_id, range=range_name).execute()
    data = result.get('values', [])
    return data