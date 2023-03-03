from app.views import *
from app.services.excel_service import read_excel_and_update_data

def test(request):
    read_excel_and_update_data()
    return HttpResponse('fe')