# Generated by Django 3.1.4 on 2021-02-25 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20190329_0022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='ingredient',
            name='owner',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
