# Generated by Django 2.0.4 on 2018-04-26 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Traffic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP')),
                ('user_agent', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('path', models.TextField(blank=True)),
            ],
        ),
    ]
