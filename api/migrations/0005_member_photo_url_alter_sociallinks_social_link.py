# Generated by Django 4.0.6 on 2022-10-14 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_member_github_member_sociallinks'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='photo_url',
            field=models.URLField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='sociallinks',
            name='social_link',
            field=models.CharField(choices=[('GH', 'Github'), ('GL', 'Gitlab'), ('TG', 'Telegram'), ('LD', 'Linkenid'), ('DS', 'Discord')], default='GH', max_length=2),
        ),
    ]
