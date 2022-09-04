# Generated by Django 4.0.6 on 2022-09-04 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_specialization_project_programming_language_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='github_member',
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_link', models.CharField(choices=[('GH', 'Github'), ('GL', 'Gitlab'), ('TG', 'Telegram'), ('LD', 'Linkenid')], default='GH', max_length=2)),
                ('link', models.URLField(max_length=256)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.member')),
            ],
        ),
    ]
