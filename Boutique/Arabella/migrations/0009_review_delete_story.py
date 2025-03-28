# Generated by Django 4.2.10 on 2024-03-20 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arabella', '0008_story'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='review/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='story',
        ),
    ]
