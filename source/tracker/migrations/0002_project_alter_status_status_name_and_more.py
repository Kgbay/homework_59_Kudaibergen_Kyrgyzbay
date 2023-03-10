# Generated by Django 4.1.7 on 2023-03-09 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, verbose_name='Дата начало')),
                ('finish_date', models.DateField(blank=True, verbose_name='Дата окончания')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.AlterField(
            model_name='status',
            name='status_name',
            field=models.CharField(choices=[('New', 'Новый'), ('In progress', 'В процессе'), ('Done', 'Выполнено')], default='New', max_length=20, verbose_name='Наименование статуса'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='type',
            name='type_name',
            field=models.CharField(choices=[('Task', 'Задача'), ('Bug', 'Ошибка'), ('Enhancement', 'Улучшение')], default='Task', max_length=20, verbose_name='Наименование типа'),
        ),
    ]
