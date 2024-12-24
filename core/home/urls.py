from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pdf-to-word/', views.pdf_to_word, name='pdf_to_word'),
    path('pdf-to-ppt/', views.pdf_to_ppt, name='pdf_to_ppt'),
    path('pdf-to-jpg/', views.pdf_to_jpg, name='pdf_to_jpg'),
    path('lock-pdf/', views.lock_pdf, name='lock_pdf'),
    path('unlock-pdf/', views.unlock_pdf, name='unlock_pdf'),
    path('jpg-to-pdf/', views.jpg_to_pdf, name='jpg_to_pdf'),
    path('ppt-to-pdf/', views.ppt_to_pdf, name='ppt_to_pdf'),
    path('word-to-pdf/', views.word_to_pdf, name='word_to_pdf'),
    path('merge-pdf/', views.merge_pdf, name='merge_pdf'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('update/', views.update_view, name='update'),
    path('delete/', views.delete_view, name='delete'),
    path('logout/', views.logout_view, name='logout'),
    path('split-pdf/', views.split_pdf, name='split_pdf'),  
    path('pdf-to-html/', views.pdf_to_html , name='pdf_to_html'),
    path('pdf-to-excel/', views.pdf_to_excel, name='pdf_to_excel'),
    path('excel-to-pdf/', views.excel_to_pdf, name='excel_to_pdf'),
    path('html-to-pdf/', views.html_to_pdf, name='html_to_pdf'),
    
    path('compress_pdf/', views.compress_pdf, name='compress_pdf'),
    path('add_watermark/', views.add_watermark, name='add_watermark'),
    path('rotate_pdf/', views.rotate_pdf, name='rotate_pdf'),
  
    path('add_numbering_pdf/', views.add_numbering_pdf, name='add_numbering_pdf'),
    path('sign_pdf/', views.sign_pdf, name='sign_pdf'),
    path('ocr_pdf/', views.ocr_pdf, name='ocr_pdf'),
]
