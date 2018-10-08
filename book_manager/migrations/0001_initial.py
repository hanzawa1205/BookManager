# Generated by Django 2.1.1 on 2018-09-07 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('price', models.FloatField()),
            ],
            options={
                'verbose_name': '图书信息',
                'verbose_name_plural': '图书信息',
                'db_table': 'book_detail',
            },
        ),
    ]