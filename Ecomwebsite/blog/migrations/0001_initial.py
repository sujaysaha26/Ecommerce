# Generated by Django 3.1.6 on 2021-05-20 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('head1', models.CharField(max_length=3000)),
                ('text1', models.CharField(default='', max_length=5000)),
                ('head2', models.CharField(default='', max_length=5000)),
                ('text2', models.CharField(default='', max_length=5000)),
                ('head3', models.CharField(default='', max_length=5000)),
                ('text3', models.CharField(default='', max_length=5000)),
                ('head4', models.CharField(default='', max_length=5000)),
                ('text4', models.CharField(default='', max_length=5000)),
                ('about', models.CharField(default='', max_length=5000)),
                ('details', models.CharField(default='', max_length=5000)),
                ('more', models.CharField(default='', max_length=5000)),
                ('publish_date', models.DateField()),
                ('images', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
