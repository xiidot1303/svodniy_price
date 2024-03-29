from app.services.excel_service import read_excel_and_update_data
from app.models import Excel

def update_excel():
    for excel in Excel.objects.filter(is_uploaded=False):
        excel.is_uploaded = True
        excel.save()
        status, error = read_excel_and_update_data(f'files/{excel.file}')
        excel.status = status
        excel.error = error
        excel.save()