# Generated by Django 4.1.3 on 2022-12-02 08:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_alter_bias_word_word'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='id',
        ),
        migrations.AddField(
            model_name='entry',
            name='bias_words',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entry',
            name='sentence',
            field=models.TextField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Bias_word',
        ),
    ]
