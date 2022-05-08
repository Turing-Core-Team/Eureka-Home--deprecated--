from __future__ import print_function

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2 import service_account

from internal.opportunities.infrastructure.dbrequest.model.opportunities import OpportunitiesModel
from internal.opportunities.infrastructure.dbrequest.model.request import RequestModel

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'
SAMPLE_RANGE_NAME = 'hoja 1!A1:w100'

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '118oriZebWeyFuUlzQjJuLiEDmE2CVHpIhmpglw51N40'


class Sheetsclient:
    def get_sample_range_name(self, sheet: int, ):

    def read(self, request_model: RequestModel) -> OpportunitiesModel:
        for i in range(request_model.range):
            try:
                service = build('sheets', 'v4', credentials=creds)

                # Call the Sheets API
                sheet = service.spreadsheets()
                result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range=SAMPLE_RANGE_NAME).execute()

                print(result)

            except HttpError as err:
                print('Intentos' + str(i))
                print(err)
                break

    def read_tags(self, ):