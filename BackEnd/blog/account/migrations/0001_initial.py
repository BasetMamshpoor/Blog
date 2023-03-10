# Generated by Django 4.0 on 2022-08-19 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFollow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('following_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='auth.user')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='auth.user')),
            ],
        ),
    ]
