# Generated by Django 4.2.1 on 2023-07-07 16:27

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customuser_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_image',
            field=models.ImageField(null=True, upload_to='users/images', validators=[users.models.validate_image]),
        ),
    ]
