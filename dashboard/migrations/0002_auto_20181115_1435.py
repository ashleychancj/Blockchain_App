# Generated by Django 2.1.3 on 2018-11-15 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('join_date', models.DateField(verbose_name='join date')),
                ('major', models.CharField(max_length=50)),
                ('grad_date', models.DateField(verbose_name='graduation date')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='Mentors',
            new_name='Mentor',
        ),
        migrations.DeleteModel(
            name='Mentees',
        ),
    ]
