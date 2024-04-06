from django.urls import path
from fileconverter import views

urlpatterns = [
    path('', views.word_to_pdf, name='word2pdf'),
    path('PDF2Word/', views.pdf_to_word, name='PDF2Word'),


    path('PPT2PDF/', views.ppt_to_pdf, name='PPT2PDF'),
    path('MergePDF/', views.merge_pdf, name='MergePDF'),
    path('SignPDF/', views.sign_pdf, name='SignPDF'),

]





