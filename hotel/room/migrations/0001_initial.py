# Generated by Django 4.1 on 2022-12-17 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_feature_title', models.CharField(blank=True, max_length=20, null=True, verbose_name='Room Feature')),
                ('room_feature_desc', models.TextField(verbose_name='Room Feature Description')),
            ],
            options={
                'verbose_name_plural': 'Room Features',
            },
        ),
        migrations.CreateModel(
            name='RoomSmallImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_img', models.ImageField(upload_to='room/small')),
            ],
            options={
                'verbose_name_plural': 'Room Small Images',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(choices=[('Single Room', 'Single Room'), ('Double Room', 'Double Room'), ('Premiere Room', 'Premiere Room'), ('Deluxe Room', 'Deluxe Room'), ('EnSuite Room', 'EnSuite Room'), ('Master EnSuite Room', 'Master EnSuite Room')], default='Single Room', max_length=30, verbose_name='Room')),
                ('room_slug', models.CharField(max_length=30, unique=True, verbose_name='Room Slug')),
                ('room_description', models.TextField(verbose_name='Room Description')),
                ('room_price', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Room Price')),
                ('room_small_description', models.TextField(verbose_name='Additional Description')),
                ('room_big_img', models.ImageField(upload_to='room', verbose_name='Room Big Image')),
                ('room_feature', models.ManyToManyField(related_name='room', to='room.roomfeature')),
                ('room_small_img', models.ManyToManyField(related_name='room', to='room.roomsmallimage', verbose_name='Room Small Image')),
            ],
            options={
                'verbose_name_plural': 'Rooms',
                'ordering': ['room'],
            },
        ),
        migrations.AddIndex(
            model_name='room',
            index=models.Index(fields=['room', 'room_slug'], name='room_room_room_320bee_idx'),
        ),
        migrations.AddIndex(
            model_name='room',
            index=models.Index(fields=['room_description'], name='room_room_room_de_06e200_idx'),
        ),
        migrations.AddIndex(
            model_name='room',
            index=models.Index(fields=['room_price'], name='room_room_room_pr_c4c016_idx'),
        ),
    ]
