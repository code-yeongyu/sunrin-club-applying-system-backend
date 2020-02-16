# Generated by Django 3.0.3 on 2020-02-16 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20200214_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='club',
            field=models.CharField(choices=[('uf', 'unifox'), ('em', 'emotion'), ('tl', 'teamlog'), ('l7', 'layer7'), ('nf', 'nefus')], max_length=2),
        ),
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='application',
            name='number',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='application',
            name='phone_number',
            field=models.CharField(max_length=11),
        ),
    ]
