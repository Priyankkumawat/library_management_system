# Generated by Django 4.0.3 on 2022-05-15 20:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IssueBook',
            fields=[
                ('name', models.CharField(db_column='Name', max_length=20)),
                ('mobile', models.CharField(db_column='Mobile', max_length=12)),
                ('enrollment', models.CharField(db_column='Enrollment', max_length=12)),
                ('book', models.CharField(db_column='Book', max_length=4, primary_key=True, serialize=False)),
                ('issue_date', models.DateField(db_column='Issue Date', default=datetime.date(2022, 5, 16))),
                ('isreturn', models.CharField(db_column='Isreturn', default='No', max_length=8)),
            ],
            options={
                'db_table': 'issue_book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Studbook',
            fields=[
                ('number', models.CharField(db_column='Number', max_length=9, primary_key=True, serialize=False)),
                ('table_number', models.CharField(blank=True, db_column='Table number', max_length=12, null=True)),
                ('subject_num', models.CharField(blank=True, db_column='Subject name', max_length=12, null=True)),
                ('book_number', models.CharField(blank=True, db_column='book number', max_length=11, null=True)),
                ('book_name', models.CharField(db_column='Book name', max_length=59)),
                ('author', models.CharField(blank=True, db_column='Author', max_length=34, null=True)),
                ('publication', models.CharField(blank=True, db_column='Publication', max_length=41, null=True)),
                ('edition', models.CharField(db_column='Edition', default='First', max_length=13)),
                ('quantity', models.CharField(db_column='Quntity', default='1', max_length=2)),
            ],
            options={
                'db_table': 'studbook',
                'managed': False,
            },
        ),
    ]
