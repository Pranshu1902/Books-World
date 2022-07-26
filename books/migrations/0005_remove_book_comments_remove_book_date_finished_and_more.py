# Generated by Django 4.0.6 on 2022-07-26 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0004_remove_review_book_remove_review_reviewer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='book',
            name='date_finished',
        ),
        migrations.RemoveField(
            model_name='book',
            name='date_started',
        ),
        migrations.RemoveField(
            model_name='book',
            name='description',
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='default.png', upload_to='book_images'),
        ),
        migrations.AddField(
            model_name='book',
            name='pagesRead',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('Reading', 'Reading'), ('Competed', 'Completed'), ('Abandoned', 'Abandoned')], default='Reading', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='timeTaken',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='totalPages',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]