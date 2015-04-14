# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(unique=True, max_length=100)),
                ('total_rating', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Jadwal_kelas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hari', models.CharField(max_length=20)),
                ('jammulai', models.TimeField()),
                ('jamselesai', models.TimeField()),
                ('ruangan', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('waktu_order', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order_item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qty', models.IntegerField(default=1)),
                ('consumer_type', models.CharField(max_length=20)),
                ('food', models.ForeignKey(to='polls.Food')),
                ('order', models.ForeignKey(to='polls.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pembayaran',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('waktu_bayar', models.DateTimeField(auto_now_add=True)),
                ('total_pembayaran', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(default=0)),
                ('komentar', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=15)),
                ('nama_user', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='review',
            name='dosen',
            field=models.ForeignKey(to='polls.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='food',
            field=models.ForeignKey(to='polls.Food'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pembayaran',
            name='sekretariat',
            field=models.ForeignKey(to='polls.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='dosen',
            field=models.ForeignKey(related_name='dosen', to='polls.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='sekretariat',
            field=models.ForeignKey(related_name='sekretariat', blank=True, to='polls.User', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='jadwal_kelas',
            name='dosen',
            field=models.ForeignKey(to='polls.User'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='jadwal_kelas',
            unique_together=set([('dosen', 'hari', 'jammulai', 'jamselesai')]),
        ),
    ]
