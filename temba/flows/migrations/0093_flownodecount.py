# Generated by Django 1.10.5 on 2017-03-30 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("flows", "0092_flowstart_include_active")]

    operations = [
        migrations.CreateModel(
            name="FlowNodeCount",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "is_squashed",
                    models.BooleanField(default=False, help_text="Whether this row was created by squashing"),
                ),
                ("node_uuid", models.UUIDField(db_index=True)),
                ("count", models.IntegerField(default=0)),
                ("flow", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="flows.Flow")),
            ],
            options={"abstract": False},
        )
    ]
