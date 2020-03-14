# Generated by Django 3.0.4 on 2020-03-14 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191124_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(choices=[('NP', 'Not played'), ('T', 'Tied'), ('W', 'Won'), ('WO', 'Walk over')], max_length=2)),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='game_player1', to='main.Player')),
                ('player2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='game_player2', to='main.Player')),
                ('winner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='game_winner', to='main.Player')),
            ],
        ),
    ]
