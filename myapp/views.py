# views.py
import pandas as pd
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import Employee

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Read the uploaded Excel file
            excel_file = request.FILES['file']
            df = pd.read_excel(excel_file)

            # Iterate over the DataFrame and update/create records
            for _, row in df.iterrows():
                employee_id = row['ID']  # Change 'ID' to the actual column name in your Excel file
                name = row['Name']        # Change 'Name' accordingly
                department = row['Department']  # Change 'Department' accordingly

                # Update or create employee record
                Employee.objects.update_or_create(
                    employee_id=employee_id,
                    defaults={'name': name, 'department': department}
                )

            return redirect('myapp:upload_success')  # Redirect to a success page
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
