# Generated by Django 3.2.14 on 2022-08-13 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='название проекта')),
                ('url', models.URLField(max_length=64, verbose_name='ссылка на проект')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='текст заметки')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='дата изменения')),
                ('is_active', models.BooleanField(default=True, verbose_name='статус')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.project', verbose_name='проект')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
    ]