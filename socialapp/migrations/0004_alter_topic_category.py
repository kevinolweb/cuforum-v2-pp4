# Generated by Django 3.2.18 on 2023-04-17 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0003_alter_comment_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='socialapp.topiccategory'),
        ),
    ]