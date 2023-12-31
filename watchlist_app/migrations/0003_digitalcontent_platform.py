# Generated by Django 4.2.7 on 2023-11-10 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0002_digitalcontent_streamingplatform_delete_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='digitalcontent',
            name='platform',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='digital_content', to='watchlist_app.streamingplatform'),
            preserve_default=False,
        ),
    ]
