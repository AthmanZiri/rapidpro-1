# Generated by Django 1.10.5 on 2017-02-16 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("contacts", "0053_auto_20170208_1450")]

    operations = [
        migrations.AddField(
            model_name="contacturn",
            name="auth",
            field=models.TextField(help_text="Any authentication information needed by this URN", null=True),
        )
    ]
