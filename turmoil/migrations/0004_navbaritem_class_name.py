# Generated by Django 5.0.6 on 2024-05-30 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turmoil', '0003_advertisement_navbaritem_notice_sitelogo_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbaritem',
            name='class_name',
            field=models.CharField(choices=[('navigation-item', 'Navigation Item'), ('navigation-item play', 'Navigation Item Play')], default='navigation-item', max_length=50),
        ),
    ]
