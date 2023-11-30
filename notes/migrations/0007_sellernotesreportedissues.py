# Generated by Django 4.2.7 on 2023-11-30 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes', '0006_sellernotesreviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerNotesReportedIssues',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('remarks', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('against_downloads', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='against_downloads_issues', to='notes.downloads')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_issues', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='modified_issues', to=settings.AUTH_USER_MODEL)),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='notes.sellernotes')),
                ('reported_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reported_issues', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
