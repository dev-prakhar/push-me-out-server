# Generated by Django 3.1.1 on 2020-10-04 09:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notifier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationStateManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('enqueued', 'Enqueued'), ('started', 'Started'), ('completed', 'Completed'), ('failed', 'Failed')], default='enqueued', max_length=16)),
                ('info', models.JSONField(default=dict, help_text='Helper field to store extra info')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subscriber', models.ForeignKey(blank=True, help_text='Subscriber to be notified, all subscribers will be notified in case this is null', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='notifier.subscriber')),
            ],
        ),
    ]