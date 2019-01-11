# Generated by Django 2.1.5 on 2019-01-09 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheretofindme', '0003_auto_20190108_2136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='internetidentity',
            options={'ordering': ('seq', 'created_at'), 'verbose_name_plural': 'Internet Identities'},
        ),
        migrations.AddField(
            model_name='internetidentity',
            name='seq',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='internetidentity',
            unique_together={('user', 'seq')},
        ),
    ]
