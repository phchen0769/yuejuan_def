# Generated by Django 4.2.7 on 2023-11-16 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('users', '0002_remove_userprofile_name_alter_userprofile_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='UsersProfile',
        ),
    ]