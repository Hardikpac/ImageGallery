# Generated by Django 3.1.4 on 2020-12-23 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='myimg')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('genre', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=140)),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
