import gspread
import yaml
import sys
from datetime import datetime

client = gspread.oauth()

GS_DOC_NAME = 'Analytics Tables'
DBT_YML_FILE = 'schema.yml'

dbt_yml = {}

with open(DBT_YML_FILE, 'r') as f:
    dbt_yml = yaml.load(f, Loader=yaml.FullLoader)
    dbt_tables = dbt_yml['models']
    
    # TODO: READ DESCRIPTION FROM GOOGLE SHEET FOR EACH TABLE
    # TODO: UPDATE DESCRIPTION IN dbt_test.yml FOR FOLLOWING TABLE NAME

    sh = client.open(f"{GS_DOC_NAME}")

    for table_index, table in enumerate(dbt_tables):
        #// TODO: HANDLE CASE WHERE TABLE NAME IS NOT FOUND IN GOOGLE SHEET
        #// TODO: HANDLE CASE WHERE DESCRIPTION FIELD ALREADY EXISTS AND IS POPULATED
        #// TODO: HANDLE CASE WHERE DESCRIPTION FIELD ALREAD EXISTS AND IS EMPTY IN SHEETS
        # TODO: HANDLE CASE WHERE WORKSHEET DOES NOT EXIST
        if table['name'] == 'test':
            try:
                worksheet = sh.worksheet(table['name'])
                first_column = worksheet.col_values(1)

                for col_index, column in enumerate(dbt_tables[table_index]['columns']):

                    for index, col_name in enumerate(first_column):
                        if column['name'] == col_name:
                            
                            if column.get('description', '') == '' \
                            and worksheet.cell(index+1, 3).value != '':
                                column['description'] = worksheet.cell(index+1, 3).value
                            
                            elif column.get('description', '') != '' \
                            and worksheet.cell(index+1, 3).value != '':
                                print(f"Previous column description: {column['description']}")
                                print(f"New column description: {worksheet.cell(index+1, 3).value}")
                                bool_input = input('Do you want to overwrite the previous column description? (y/n)')
                                if bool_input == 'y' or bool_input == 'Y':
                                    column['description'] = worksheet.cell(index+1, 3).value
            
            except(gspread.exceptions.WorksheetNotFound):
                print(f"Worksheet not found: {table['name']}")

        
            
with open(DBT_YML_FILE, 'w') as f:
    yaml.dump(dbt_yml, f, Dumper=yaml.Dumper, sort_keys=False)
            #// TODO: READ DESCRIPTION FROM GOOGLE SHEET FOR EACH COLUMN
            #// TODO: UPDATE DESCRIPTION IN dbt_test.yml FOLLOWING COLUMN NAME
            



