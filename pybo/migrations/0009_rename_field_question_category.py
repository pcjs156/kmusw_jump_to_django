# Generated by Django 3.2.6 on 2021-09-23 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0008_question_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='field',
            new_name='category',
        ),
    ]
