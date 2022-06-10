'''
Extract Individual contribution history when required
'''
import gspread
import os
import sys
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
# scope = ['https://spreadsheets.google.com/feeds']
scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name('API_Key/client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
GS_DOC_NAME = 'Analytics Tables'
GS_SHEET_NAME = 'Lorem Ipsum'
sheet = client.open(f"{GS_DOC_NAME}").worksheet(f"{GS_SHEET_NAME}")

# Extract and print all of the values
# list_of_hashes = sheet.get_all_records()
# print(list_of_hashes)

contributor_name = input("Contributor Name: ")
names_list = sheet.col_values(1)
if contributor_name not in names_list:
	print("Contributor not found")
	exit()

index = names_list.index(contributor_name)

transaction_history = sheet.row_values(index+1)[8:-3]

# create month_year arr from June 2020 to May 2024
month_year_arr = ['June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020', 'December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021', 'November 2021', 'December 2021', 'January 2022', 'February 2022', 'March 2022', 'April 2022', 'May 2022', 'June 2022', 'July 2022', 'August 2022', 'September 2022', 'October 2022', 'November 2022', 'December 2022', 'January 2023', 'February 2023', 'March 2023', 'April 2023', 'May 2023', 'June 2023', 'July 2023', 'August 2023', 'September 2023', 'October 2023', 'November 2023', 'December 2023', 'January 2024', 'February 2024', 'March 2024', 'April 2024', 'May 2024']
for i in range(len(month_year_arr)):
	month_name, year = month_year_arr[i].split()
	if (int(year) == datetime.now().year and datetime.strptime(month_name, "%B").month <= datetime.now().month) or int(year) < datetime.now().year:
		
		print(month_year_arr[i],"|", transaction_history[i*2],"|", transaction_history[i*2+1])