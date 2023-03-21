# Generated by Django 4.1 on 2022-12-20 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_alter_room_room_feature_alter_room_room_small_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='special')),
                ('special_title', models.CharField(blank=True, max_length=10, null=True, verbose_name='Title')),
                ('special_slug', models.CharField(max_length=10, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
            ],
            options={
                'verbose_name_plural': 'Special Offers',
                'ordering': ['special_title'],
            },
        ),
        migrations.AlterField(
            model_name='room',
            name='room_price',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Room Price'),
        ),
        migrations.AddIndex(
            model_name='specialoffer',
            index=models.Index(fields=['special_title', 'special_slug'], name='room_specia_special_e9401f_idx'),
        ),
        migrations.AddIndex(
            model_name='specialoffer',
            index=models.Index(fields=['price'], name='room_specia_price_3fd419_idx'),
        ),
    ]