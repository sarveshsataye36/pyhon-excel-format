import io
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import openpyxl
import pandas as pd

def index(request):
    return render(request, 'excels/fileupload.html')


def upload_excel(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']


        header_row_num = int(request.POST.get('header_row_num', 0))  # Get the starting row from the request, default is 0
        if(header_row_num > 0):
            header_row_num = header_row_num -1

        # Read the Excel file using pandas
        df = pd.read_excel(excel_file,skiprows=header_row_num)
        
        # Get column headers
        column_names = df.columns.tolist()

        return JsonResponse({'column_names': column_names})
    else:
        return JsonResponse({'error': 'No file was uploaded.'}, status=400)


def create_excel(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']
        column_names = request.POST.getlist('selected_columns')

        header_row_num = int(request.POST.get('header_row_num', 0))  # Get the starting row from the request, default is 0
        if(header_row_num > 0):
            header_row_num = header_row_num -1
            
        df = pd.read_excel(excel_file,skiprows=header_row_num)

        # Filter columns
        filtered_df = df[column_names]
        

        # Create a new Excel file
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            filtered_df.to_excel(writer, index=False)

        # Create HTTP response with the new Excel file
        response = HttpResponse(
            output.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=filtered_data.xlsx'
        return response

        # If request method is GET or no file was uploaded, render the upload form
        return redirect('index')

    #     return JsonResponse({'column_names':column_names})
    #     # return JsonResponse({'column_names': column_names})
    else:
        return redirect('index')
