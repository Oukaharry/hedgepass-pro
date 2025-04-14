# Generated by Django 5.2 on 2025-04-13 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accountpair',
            options={},
        ),
        migrations.AlterModelOptions(
            name='performancedata',
            options={},
        ),
        migrations.RemoveIndex(
            model_name='performancedata',
            name='main_perfor_date_50f009_idx',
        ),
        migrations.RemoveIndex(
            model_name='performancedata',
            name='main_perfor_pair_id_d7c629_idx',
        ),
        migrations.RemoveField(
            model_name='accountpair',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='accountpair',
            name='live_account_login',
        ),
        migrations.RemoveField(
            model_name='accountpair',
            name='live_account_password',
        ),
        migrations.RemoveField(
            model_name='accountpair',
            name='live_account_server',
        ),
        migrations.RemoveField(
            model_name='accountpair',
            name='prop_account_login',
        ),
        migrations.RemoveField(
            model_name='accountpair',
            name='prop_account_password',
        ),
        migrations.RemoveField(
            model_name='accountpair',
            name='prop_account_server',
        ),
        migrations.RemoveField(
            model_name='accountpair',
            name='prop_account_trading_type',
        ),
        migrations.RemoveField(
            model_name='performancedata',
            name='date',
        ),
        migrations.RemoveField(
            model_name='performancedata',
            name='efficiency',
        ),
        migrations.RemoveField(
            model_name='performancedata',
            name='hedge_equity',
        ),
        migrations.RemoveField(
            model_name='performancedata',
            name='live_equity',
        ),
        migrations.RemoveField(
            model_name='performancedata',
            name='trades_count',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='accountpair',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
