# Generated by Django 3.1.7 on 2021-03-10 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210309_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='income_certificates',
            field=models.ImageField(null=True, upload_to='income_certificates'),
        ),
        migrations.AddField(
            model_name='application',
            name='marks_cards_10th',
            field=models.ImageField(null=True, upload_to='marks_cards_10th'),
        ),
    ]
