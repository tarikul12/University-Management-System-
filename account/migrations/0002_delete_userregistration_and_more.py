# Generated by Django 5.0.6 on 2024-10-12 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserRegistration',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='is_staff',
            new_name='is_faculty',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='is_superuser',
            new_name='is_student',
        ),
        migrations.AddField(
            model_name='account',
            name='first_name',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='account',
            name='is_superadmin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='last_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=models.CharField(default='0000000000', max_length=50),
        ),
        migrations.AddField(
            model_name='account',
            name='user_type',
            field=models.CharField(choices=[('admin', 'Admin'), ('student', 'student'), ('faculty', 'faculty'), ('superadmin', 'Super Admin')], default='customer', max_length=20),
        ),
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]