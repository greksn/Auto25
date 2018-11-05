# Generated by Django 2.1.1 on 2018-11-04 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=5000)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]