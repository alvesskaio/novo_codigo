# Generated by Django 5.1.2 on 2024-11-01 14:01

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Convite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=255)),
                ('data_envio', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_expiracao', models.DateTimeField()),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SistemaConvite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limite_convites', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=255)),
                ('convidados', models.ManyToManyField(blank=True, to='content_app.usuario')),
                ('convites_enviados', models.ManyToManyField(blank=True, related_name='convites_enviados', to='content_app.convite')),
            ],
        ),
        migrations.AddField(
            model_name='convite',
            name='usuario_convidado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='convites_recebidos', to='content_app.usuario'),
        ),
        migrations.AddField(
            model_name='convite',
            name='usuario_convindante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convites_feitos', to='content_app.usuario'),
        ),
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('convite_usado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content_app.convite')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content_app.usuario')),
            ],
        ),
    ]
