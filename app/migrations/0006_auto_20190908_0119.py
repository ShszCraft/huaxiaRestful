# Generated by Django 2.1.9 on 2019-09-07 17:19

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190825_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='标签', max_length=50)),
                ('image', models.ImageField(help_text='记录标签图', upload_to=app.models.ClassActivity.get_upload_to)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(default='C', help_text='记录文章的标题', max_length=255, null=True, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(default='C', help_text='记录文章内容', null=True, verbose_name='内容'),
        ),
        migrations.AddField(
            model_name='article',
            name='class_activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.ClassActivity'),
        ),
    ]
