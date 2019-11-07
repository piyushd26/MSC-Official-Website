# Generated by Django 2.2.2 on 2019-11-06 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=50)),
                ('photourl', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Core',
            fields=[
                ('members_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='members.Members')),
            ],
            bases=('members.members',),
        ),
        migrations.CreateModel(
            name='Executive',
            fields=[
                ('members_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='members.Members')),
            ],
            bases=('members.members',),
        ),
        migrations.CreateModel(
            name='Secretaries',
            fields=[
                ('members_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='members.Members')),
            ],
            bases=('members.members',),
        ),
    ]
