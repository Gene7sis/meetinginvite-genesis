# Generated by Django 4.0.8 on 2023-01-19 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitations', '0003_alter_gifttable_bank_image_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Places',
            new_name='Place',
        ),
        migrations.AlterField(
            model_name='invitationbase',
            name='itinerary',
            field=models.ImageField(blank=True, upload_to='itinerary'),
        ),
    ]
