# Generated by Django 1.10.5 on 2017-05-11 18:30

from django.db import migrations

from temba.utils import chunk_list


def populate_attachments(Msg):
    msg_ids = list(Msg.objects.exclude(media=None).values_list("id", flat=True))
    if not msg_ids:
        return

    print("Fetched %d message ids with media to update..." % len(msg_ids))

    num_updated = 0
    for id_batch in chunk_list(msg_ids, 1000):
        for msg in Msg.objects.filter(id__in=id_batch):
            msg.attachments = [msg.media]
            msg.save(update_fields=("attachments",))

        num_updated += len(id_batch)
        print(" > Updated %d of %d messages with media" % (num_updated, len(id_batch)))


def apply_as_migration(apps, schema_editor):
    Msg = apps.get_model("msgs", "Msg")
    populate_attachments(Msg)


def apply_manual():
    from temba.msgs.models import Msg

    populate_attachments(Msg)


class Migration(migrations.Migration):

    dependencies = [("msgs", "0095_msg_attachments")]

    operations = [migrations.RunPython(apply_as_migration)]
