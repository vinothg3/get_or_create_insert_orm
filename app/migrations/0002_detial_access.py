# Generated by Django 4.1.7 on 2023-05-31 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='detial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cricket')),
            ],
        ),
        migrations.CreateModel(
            name='access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Wife', models.CharField(max_length=100)),
                ('Child', models.IntegerField()),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.detial')),
            ],
        ),
    ]