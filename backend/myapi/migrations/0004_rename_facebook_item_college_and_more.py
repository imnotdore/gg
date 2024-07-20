# Generated by Django 5.0.6 on 2024-07-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_alter_item_zipcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Facebook',
            new_name='College',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='Instagram',
            new_name='Date_of_Birth',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='School',
            new_name='Elementary',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='StudentID',
            new_name='Fathers_name',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='Tiktok',
            new_name='Mothers_name',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='Twitter',
            new_name='Secondary',
        ),
        migrations.AddField(
            model_name='item',
            name='Student_No',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='ZipCode',
            field=models.TextField(default=''),
        ),
    ]