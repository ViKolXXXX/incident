# Generated by Django 2.2.1 on 2019-09-17 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orion', '0002_auto_20190917_0939'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='face',
            unique_together={('familiya', 'imya', 'otchestvo', 'date_rojdeniya')},
        ),
    ]