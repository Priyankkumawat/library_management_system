# Generated by Django 4.0.3 on 2022-04-22 06:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stud', '0003_rename_cur_date_issuebook_issue_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuebook',
            name='issue_date',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]