from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
import os

class ConvertToPdfViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_convert_to_pdf_invalid_file(self):
        # Prepare a sample .txt file for upload (not supported)
        with open('./fileconverter/test_files/sample.txt', 'w') as file:
            file.write("This is an invalid file content.")

        with open('./fileconverter/test_files/sample.txt', 'rb') as file:
            file_data = {'file': SimpleUploadedFile('sample.txt', file.read(), content_type='text/plain')}
        
        response = self.client.post(reverse('convert'), file_data)

        # Assert the response status code and content
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'Only .docx files are supported.')

    def test_convert_to_pdf_successful(self):
        # Prepare a sample .docx file for upload
        with open('./fileconverter/test_files/sample.docx', 'rb') as file:
            file_data = {'file': SimpleUploadedFile('sample.docx', file.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')}
        
        response = self.client.post(reverse('convert'), file_data)

        # Assert the response status code and content
        self.assertEqual(response.status_code, 200)
        self.assertIn('pdf_url', response.json())
        self.assertTrue(response.json()['pdf_url'].endswith('.pdf'))
