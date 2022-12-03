# Generated by Django 4.1.3 on 2022-12-03 17:50

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ("job_portal", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="country",
            field=django_countries.fields.CountryField(default="", max_length=2),
            preserve_default=False,
        ),
    ]