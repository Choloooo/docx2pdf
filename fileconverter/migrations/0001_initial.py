# Generated by Django 4.2.10 on 2024-03-01 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConvertedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_file', models.FileField(upload_to='uploads/')),
                ('converted_pdf', models.FileField(blank=True, upload_to='pdfs/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]