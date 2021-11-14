# Generated by Django 3.2.8 on 2021-10-16 18:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='Last Name')),
                ('site', models.CharField(blank=True, max_length=100, verbose_name='Web Site')),
            ],
            options={
                'verbose_name': 'author',
                'verbose_name_plural': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Category Name')),
                ('enabled', models.BooleanField(default=True, verbose_name='Is Enabled?')),
                ('order', models.IntegerField(verbose_name='Order')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Resource Name')),
                ('slug', models.CharField(max_length=200, verbose_name='Slug')),
                ('note', models.TextField(blank=True, default='', max_length=300, verbose_name='Note')),
                ('rating', models.FloatField(default=5.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('enabled', models.BooleanField(default=True, verbose_name='Is Enabled?')),
                ('local', models.CharField(choices=[('EN', 'English'), ('TR', 'Turkish')], default='TR', max_length=2, verbose_name='Language')),
                ('level', models.CharField(choices=[('BGN', 'Beginner'), ('EXP', 'Experienced'), ('PRO', 'Professional')], default='BGN', max_length=3, verbose_name='Level')),
                ('content', models.CharField(choices=[('BK', 'Book'), ('DC', 'Document'), ('LN', 'Link')], default='DC', max_length=2, verbose_name='Type of Resource')),
                ('file_name', models.CharField(max_length=255, verbose_name='File Name')),
                ('file_id', models.CharField(default='', max_length=100)),
                ('url', models.CharField(blank=True, max_length=100, verbose_name='Website')),
                ('image', models.ImageField(blank=True, default='not-found.jpg', upload_to='resource_imgs', verbose_name='Image')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ManyToManyField(related_name='resource_authors', to='record.Author', verbose_name='Authors')),
                ('category', models.ManyToManyField(to='record.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'resource',
                'verbose_name_plural': 'resources',
            },
        ),
        migrations.AddConstraint(
            model_name='resource',
            constraint=models.UniqueConstraint(condition=models.Q(('content', 'DC')), fields=('file_name',), name='unique_document_file_name'),
        ),
    ]