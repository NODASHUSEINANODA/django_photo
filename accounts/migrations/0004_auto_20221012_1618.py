# Generated by Django 2.2.20 on 2022-10-12 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20221012_1614'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='followership',
            unique_together={('follower', 'followee')},
        ),
    ]
