# Generated by Django 2.2.1 on 2019-06-19 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Divisao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('ativo', models.BooleanField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('ativo', models.BooleanField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('divisao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotacoes.Divisao')),
            ],
        ),
        migrations.CreateModel(
            name='Lotacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField()),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoas.Pessoa')),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotacoes.Setor')),
            ],
        ),
    ]
