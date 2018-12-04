# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-12-04 11:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('files', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='The name of the portfolio', max_length=255)),
                ('accounts_file', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts_file_portfolios', to='files.RelatedFile')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolios', to=settings.AUTH_USER_MODEL)),
                ('location_file', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location_file_portfolios', to='files.RelatedFile')),
                ('reinsurance_info_file', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reinsurance_info_file_portfolios', to='files.RelatedFile')),
                ('reinsurance_source_file', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reinsurance_source_file_portfolios', to='files.RelatedFile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortfolioStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
