import gspread

client = gspread.oauth()

GS_DOC_NAME = 'Analytics Tables'
sh = client.open(GS_DOC_NAME)

try:
    worksheet = sh.worksheet('test')

except(gspread.exceptions.WorksheetNotFound):
    print("Worksheet not found: test2")
