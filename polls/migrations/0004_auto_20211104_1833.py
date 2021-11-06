# Generated by Django 3.2.9 on 2021-11-04 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20211104_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_question',
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='choices', to='polls.question'),
        ),
    ]