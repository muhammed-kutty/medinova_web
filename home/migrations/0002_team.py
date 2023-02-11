# Generated by Django 4.1.5 on 2023-01-28 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=255)),
                ('doc_spec', models.TextField(max_length=255)),
                ('doc_img', models.ImageField(upload_to='doctors')),
                ('dep_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.department')),
            ],
        ),
    ]
