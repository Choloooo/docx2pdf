# views.py

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.files.storage import default_storage
from io import BytesIO
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

def word_to_pdf(request):
    if request.method == 'POST' and request.FILES['file']:
        # Get the uploaded DOCX file from the request
        docx_file = request.FILES['file']
        
        # Read the content of the DOCX file
        docx_doc = Document(docx_file)

        # Create a buffer for the PDF content
        buffer = BytesIO()

        # Create a PDF document
        pdf = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()

        # Generate PDF content from the DOCX document
        pdf_content = []
        for paragraph in docx_doc.paragraphs:
            pdf_content.append(Paragraph(paragraph.text, styles["Normal"]))

        # Build the PDF document
        pdf.build(pdf_content)

        # Get the PDF content from the buffer
        pdf_buffer = buffer.getvalue()

        # Save PDF to Amazon S3
        pdf_filename = f'pdf/{os.path.splitext(docx_file.name)[0]}.pdf'
        default_storage.save(pdf_filename, BytesIO(pdf_buffer))

        # Get the URL of the saved PDF file
        pdf_url = default_storage.url(pdf_filename)
        
        
        print("Download URL:", pdf_url)

        # Return JSON response with PDF URL
        return JsonResponse({'pdf_url': pdf_url})

    return render(request, 'converter/upload.html')



def pdf_to_word(request):
    return render(request, 'comingsoon.html')

def ppt_to_pdf(request):
    return render(request, 'comingsoon.html')

def merge_pdf(request):
    return render(request, 'comingsoon.html')

def sign_pdf(request):
    return render(request, 'comingsoon.html')