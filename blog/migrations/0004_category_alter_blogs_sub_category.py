# Generated by Django 4.1.1 on 2022-10-07 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_name_blogs_title_blogs_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=35)),
            ],
        ),
        migrations.AlterField(
            model_name='blogs',
            name='sub_category',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
