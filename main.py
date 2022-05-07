from _future_ import print_function

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'
SAMPLE_RANGE_NAME = 'tags!A1:A5'

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '118oriZebWeyFuUlzQjJuLiEDmE2CVHpIhmpglw51N40'

def main():


    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        '''values = result.get('values', [])'''

        print(result)

    except HttpError as err:
        print(err)


if __name__ == "__main__":
    main()