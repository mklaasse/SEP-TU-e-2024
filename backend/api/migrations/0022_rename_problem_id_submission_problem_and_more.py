# Generated by Django 5.0.4 on 2024-05-27 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_rename_benchmarkset_benchmarkrelations_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='problem_id',
            new_name='problem',
        ),
        migrations.AlterField(
            model_name='specifiedproblem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]