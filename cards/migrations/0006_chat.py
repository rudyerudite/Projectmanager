# Generated by Django 3.0.4 on 2020-03-25 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_auto_20200323_0656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(blank=True, max_length=50)),
                ('author', models.CharField(blank=True, max_length=50)),
                ('card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cards.Cards')),
            ],
        ),
    ]