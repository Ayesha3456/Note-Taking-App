# Generated by Django 5.1.2 on 2024-11-06 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notetakingapp", "0002_rename_task_note"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="category",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="note",
            name="due_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="note",
            name="priority",
            field=models.CharField(
                choices=[("High", "High"), ("Medium", "Medium"), ("Low", "Low")],
                default="Medium",
                max_length=10,
            ),
        ),
    ]
