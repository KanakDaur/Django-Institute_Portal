# Generated by Django 3.0.3 on 2020-06-10 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20200610_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.FileField(default='student_icon.png', upload_to='student_images'),
        ),
    ]
