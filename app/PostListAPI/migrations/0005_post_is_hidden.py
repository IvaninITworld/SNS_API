# Generated by Django 4.2.5 on 2023-09-14 13:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("PostListAPI", "0004_rename_update_date_post_updated_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="is_hidden",
            field=models.BooleanField(default=False),
        ),
    ]
