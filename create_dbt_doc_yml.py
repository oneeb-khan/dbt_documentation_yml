'''
Extract Individual contribution history when required
'''
import gspread
import yaml
import sys
from datetime import datetime

client = gspread.oauth()

GS_DOC_NAME = 'Analytics Tables'
DBT_YML_FILE = 'dbt_test.yml'

with open(DBT_YML_FILE, 'r+') as f:
    dbt_yml = yaml.load(f, Loader=yaml.FullLoader)
    dbt_tables = dbt_yml['sources'][0]['tables']
    # ['loader'][0]['tables']
    # with client.open(f"{GS_DOC_NAME}") as sh:
    # TODO: READ DESCRIPTION FROM GOOGLE SHEET FOR EACH TABLE
    # TODO: UPDATE DESCRIPTION IN dbt_test.yml FOR FOLLOWING TABLE NAME

    sh = client.open(f"{GS_DOC_NAME}")
    dbt_tables = dbt_tables[-1]
    for table in dbt_tables:
        for column in table['columns']:
            worksheet = sh.worksheet(table['name'])
            # TODO: READ DESCRIPTION FROM GOOGLE SHEET FOR EACH COLUMN
            # TODO: UPDATE DESCRIPTION IN dbt_test.yml FOLLOWING COLUMN NAME





    # print(dbt_tables)

# sheet = client.open(f"{GS_DOC_NAME}").worksheet(f"{GS_SHEET_NAME}")

# print(sheet.get_all_values())

# Extract and print all of the values
# list_of_hashes = sheet.get_all_records()
# print(list_of_hashes)

# contributor_name = input("Contributor Name: ")
# names_list = sheet.col_values(1)
# if contributor_name not in names_list:
# 	print("Contributor not found")
# 	exit()

# index = names_list.index(contributor_name)

# transaction_history = sheet.row_values(index+1)[8:-3]

# # create month_year arr from June 2020 to May 2024
# month_year_arr = ['June 2020', 'July 2020', 'August 2020', 'September 2020', 'October 2020', 'November 2020', 'December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021', 'October 2021', 'November 2021', 'December 2021', 'January 2022', 'February 2022', 'March 2022', 'April 2022', 'May 2022', 'June 2022', 'July 2022', 'August 2022', 'September 2022', 'October 2022', 'November 2022', 'December 2022', 'January 2023', 'February 2023', 'March 2023', 'April 2023', 'May 2023', 'June 2023', 'July 2023', 'August 2023', 'September 2023', 'October 2023', 'November 2023', 'December 2023', 'January 2024', 'February 2024', 'March 2024', 'April 2024', 'May 2024']
# for i in range(len(month_year_arr)):
# 	month_name, year = month_year_arr[i].split()
# 	if (int(year) == datetime.now().year and datetime.strptime(month_name, "%B").month <= datetime.now().month) or int(year) < datetime.now().year:
		
# 		print(month_year_arr[i],"|", transaction_history[i*2],"|", transaction_history[i*2+1])