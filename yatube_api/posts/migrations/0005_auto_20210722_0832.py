# Generated by Django 2.2.6 on 2021-07-22 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210722_0518'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique subscribers',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('following', 'user'), name='unique subscribers'),
        ),
    ]
