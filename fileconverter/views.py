from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import default_storage
import docx2pdf
import os
import uuid

from converter import settings
from .forms import UploadForm
import traceback
import os
from django.core.files.storage import default_storage
from converter import settings
from .forms import UploadForm
import docx2pdf

def convert_to_pdf(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            
            # User uploads a DOCX file through the frontend
            
            # Backend receives the file, validates it, and saves it to S3 with a unique name under the 'docx' directory
            file_path = default_storage.save(f'docx/{uuid.uuid4()}.docx', file)

            # Backend triggers the conversion process using docx2pdf.convert()
            try:
                # Convert the file to PDF
                output_pdf_name = os.path.splitext(file_path)[0] + '.pdf'
                output_pdf_path = f'pdf/{os.path.basename(output_pdf_name)}'
                docx2pdf.convert(file_path, output_pdf_path)

                # Converted PDF file is saved to S3 with a unique name under the 'pdf' directory
                # Construct S3 URLs for both DOCX and PDF files
                docx_url = f'https://{settings.AWS_S3_CUSTOM_DOMAIN}/{file_path}'
                pdf_url = f'https://{settings.AWS_S3_CUSTOM_DOMAIN}/{output_pdf_path}'
                print('PDF converted and saved to:', output_pdf_path)
                print('Download your PDF here:', pdf_url)

                # Response containing the URLs is sent back to the frontend
                return JsonResponse({'docx_url': docx_url, 'pdf_url': pdf_url})
            except Exception as e:
                error_msg = f'Error converting file: {e}'
                print(error_msg)
                return JsonResponse({'error': error_msg}, status=500)
            
    else:
        form = UploadForm()
    return render(request, 'converter/upload.html', {'form': form})
