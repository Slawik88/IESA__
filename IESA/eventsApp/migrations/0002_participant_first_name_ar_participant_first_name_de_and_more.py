# Generated by Django 4.2.8 on 2023-12-23 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='first_name_ar',
            field=models.CharField(help_text='Enter your first name.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='first_name_de',
            field=models.CharField(help_text='Enter your first name.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='first_name_en',
            field=models.CharField(help_text='Enter your first name.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='first_name_fr',
            field=models.CharField(help_text='Enter your first name.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='first_name_ru',
            field=models.CharField(help_text='Enter your first name.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='first_name_uk',
            field=models.CharField(help_text='Enter your first name.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='last_name_ar',
            field=models.CharField(help_text='Enter your last name.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='last_name_de',
            field=models.CharField(help_text='Enter your last name.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='last_name_en',
            field=models.CharField(help_text='Enter your last name.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='last_name_fr',
            field=models.CharField(help_text='Enter your last name.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='last_name_ru',
            field=models.CharField(help_text='Enter your last name.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='last_name_uk',
            field=models.CharField(help_text='Enter your last name.', max_length=255, null=True),
        ),
    ]
