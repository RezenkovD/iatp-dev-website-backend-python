# Generated by Django 4.0.6 on 2022-10-17 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_member_photo_url_alter_sociallinks_social_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='projects', to='api.member'),
        ),
        migrations.AlterField(
            model_name='sociallinks',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='social_links', to='api.member'),
        ),
    ]