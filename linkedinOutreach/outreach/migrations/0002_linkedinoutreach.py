# Generated by Django 4.0.5 on 2023-03-18 18:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('outreach', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkedinOutreach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_column='created_on', default=django.utils.timezone.localtime)),
                ('updated_on', models.DateTimeField(db_column='updated_on', default=django.utils.timezone.localtime)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('linkedin_url', models.TextField()),
            ],
            options={
                'ordering': ('-updated_on', '-created_on'),
                'get_latest_by': 'updated_on',
                'abstract': False,
                'default_permissions': (),
            },
        ),
    ]
