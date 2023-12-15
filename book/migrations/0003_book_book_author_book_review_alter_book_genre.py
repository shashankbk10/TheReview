# Generated by Django 4.1.4 on 2023-03-11 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_rename_books_book_rename_description_book_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_author',
            field=models.CharField(default='Not Known', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='review',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=100),
        ),
    ]