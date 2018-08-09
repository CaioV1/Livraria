# Generated by Django 2.0.7 on 2018-08-03 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('pais_origem', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=70)),
                ('data_lancamento', models.DateField()),
                ('sinopse', models.TextField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_livro', to='livros.Autor')),
                ('editora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='editora_livro', to='livros.Editora')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genero_livro', to='livros.Genero')),
            ],
        ),
        migrations.AddField(
            model_name='genero',
            name='livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livro_genero', to='livros.Livro'),
        ),
        migrations.AddField(
            model_name='editora',
            name='livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livro_editora', to='livros.Livro'),
        ),
        migrations.AddField(
            model_name='autor',
            name='livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livro_autor', to='livros.Livro'),
        ),
    ]
