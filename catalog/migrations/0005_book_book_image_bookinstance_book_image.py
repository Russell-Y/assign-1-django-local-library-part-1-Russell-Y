# Generated by Django 5.1.5 on 2025-02-27 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_author_author_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='book_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
