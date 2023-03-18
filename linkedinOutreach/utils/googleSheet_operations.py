import gspread

from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]


def read_google_sheet(sheet_name, tab_name):
    creds = ServiceAccountCredentials.from_json_keyfile_name("utils/credentials/cred.json", scope)
    client = gspread.authorize(creds)
    masterSheet = client.open(sheet_name).worksheet(tab_name)
    return masterSheet.get_all_records(), masterSheet


def update_status(linkedin_url, sheet, col_count, msg):
    cell = sheet.find(linkedin_url)
    try:
        sheet.update_cell(cell.row, cell.col + col_count, msg)
        # sheet.update_cell(cell.row, cell.col + 3, str(datetime.now()))
    except:
        pass
