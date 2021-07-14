# Generated by Django 3.1.4 on 2020-12-29 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_download'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='files.documentpost'),
        ),
        migrations.AlterField(
            model_name='dislike',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disliked_post', to='files.documentpost'),
        ),
        migrations.AlterField(
            model_name='download',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files.documentpost'),
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_post', to='files.documentpost'),
        ),
    ]
