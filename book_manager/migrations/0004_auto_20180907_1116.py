# Generated by Django 2.1.1 on 2018-09-07 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_manager', '0003_reader'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reader',
            name='number',
        ),
        migrations.AddField(
            model_name='reader',
            name='email',
            field=models.EmailField(default=2, max_length=254, verbose_name='邮箱'),
            preserve_default=False,
        ),
    ]
