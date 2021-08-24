# Generated by Django 3.2.6 on 2021-08-24 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sweet_shared', '0002_certificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='awarded_by',
            field=models.ForeignKey(default=None, blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='certificates_awarded', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='certificate',
            name='awardee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to=settings.AUTH_USER_MODEL),
        ),
    ]
