# Generated by Django 3.2.13 on 2022-06-30 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUserModel',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('phone', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=200)),
                ('national_code', models.CharField(max_length=10, unique=True)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('condition', models.BooleanField(default=False)),
            ],
        ),
    ]
