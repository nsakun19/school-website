# Generated by Django 2.1 on 2018-12-08 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0004_auto_20181208_0754'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notices',
            options={'ordering': ['notice_date']},
        ),
    ]