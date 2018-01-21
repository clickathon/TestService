# Generated by Django 2.0.1 on 2018-01-21 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0003_auto_20180121_0910'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionWebApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('image', models.FileField(blank=True, upload_to='post_image')),
            ],
        ),
    ]
