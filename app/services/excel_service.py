import xlrd
from app.services.drug_service import (
    update_or_create_drug_by_data, 
    update_or_create_provider_by_data, 
)
from app.utils import fix_format_date_in_excel

from datetime import datetime

def read_excel_and_update_data(file_url = 'files/prices.xls'):
    # open workbook
    book = xlrd.open_workbook(file_url)
    # set sheet1 that drugs list
    sheet1 = book.sheet_by_index(0)
    # set sheet2 that providers list
    sheet2 = book.sheet_by_index(1)

    ## READ PROVIDERS PAGE
    # get values of providers
    provider_values = [
        {
            'name': str(sheet2.cell_value(i, 1)).lower(),
            'phone': sheet2.cell_value(i, 2),
            'address': sheet2.cell_value(i, 3)
        }
        for i in range(2, sheet2.nrows)
    ]
    # update or create objects
    update_or_create_provider_by_data(provider_values)

    ## READ DRUGS PAGE
    # get values of drugs
    drug_values = [
        {
            'title': sheet1.cell_value(i, 1), 'title_en': sheet1.cell_value(i, 2), 
            'term': fix_format_date_in_excel(sheet1.cell_value(i, 8)), 'price': str(sheet1.cell_value(i, 5)), 
            'provider_name': sheet1.cell_value(i, 9), 'manufacturer': sheet1.cell_value(i, 10), 
            'country': sheet1.cell_value(i, 11) 
        }
        for i in range(2, sheet1.nrows)
        ]
    # update or create objects
    update_or_create_drug_by_data(drug_values)
