# Generated by Django 5.1.3 on 2024-12-07 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('root', '0003_score_tester'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('desc', models.TextField()),
                ('categorys', models.ManyToManyField(to='root.ctaegory')),
            ],
        ),
    ]
