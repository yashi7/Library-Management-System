# Generated by Django 4.2.7 on 2024-02-01 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Register_number', models.CharField(max_length=200)),
                ('Login_as', models.CharField(choices=[('Admin', 'Admin'), ('User', 'User'), ('Librarian', 'Librarian')], max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
