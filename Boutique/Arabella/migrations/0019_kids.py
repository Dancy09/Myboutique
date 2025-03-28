# Generated by Django 4.2.10 on 2024-03-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arabella', '0018_kurtis'),
    ]

    operations = [
        migrations.CreateModel(
            name='kids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='fabric/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
