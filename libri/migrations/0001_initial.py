# Generated by Django 3.1.4 on 2021-02-20 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CasaEditrice',
            fields=[
                ('CodCasaEd', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('Sede', models.CharField(max_length=256)),
                ('Nome', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Collane',
            fields=[
                ('CodCollane', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('Nome', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='NonSeriale',
            fields=[
                ('CodLibro', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('Straniero', models.BooleanField(default=False)),
                ('TitoloOrig', models.CharField(blank=True, max_length=256, null=True)),
                ('Titolo', models.CharField(max_length=256)),
                ('Sottotitolo', models.CharField(blank=True, max_length=256, null=True)),
                ('AnnoEd', models.IntegerField()),
                ('Illustrazioni', models.BooleanField(default=False)),
                ('ISBN', models.CharField(max_length=13)),
                ('Genere', models.CharField(max_length=256)),
                ('NumPub', models.IntegerField(blank=True, null=True)),
                ('CopertinaRigida', models.BooleanField(default=False)),
                ('Ristampa', models.BooleanField(default=False)),
                ('nRistampa', models.IntegerField(blank=True, null=True)),
                ('Edizione', models.IntegerField()),
                ('NumPagine', models.IntegerField()),
                ('Curatore', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PostfazionePre',
            fields=[
                ('CodPostfazione', models.CharField(max_length=4, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Scaffale',
            fields=[
                ('CodScaffale', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('CatScaffale', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Seriale',
            fields=[
                ('CodLibro', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('Straniero', models.BooleanField(default=False)),
                ('TitoloOrig', models.CharField(blank=True, max_length=256, null=True)),
                ('Titolo', models.CharField(max_length=256)),
                ('Sottotitolo', models.CharField(blank=True, max_length=256, null=True)),
                ('AnnoEd', models.IntegerField()),
                ('Illustrazioni', models.BooleanField(default=False)),
                ('ISSN', models.CharField(max_length=8)),
                ('Genere', models.CharField(max_length=256)),
                ('NumPub', models.IntegerField(blank=True, null=True)),
                ('CopertinaRigida', models.BooleanField(default=False)),
                ('Ristampa', models.BooleanField(default=False)),
                ('nRistampa', models.IntegerField(blank=True, null=True)),
                ('Edizione', models.IntegerField()),
                ('NumPagine', models.IntegerField()),
                ('Curatore', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TradAutCur',
            fields=[
                ('CodAutore', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('Nome', models.CharField(max_length=256)),
                ('Cognome', models.CharField(max_length=256)),
                ('Nazione', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Utenti',
            fields=[
                ('CodUser', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('Nome', models.CharField(max_length=256)),
                ('Cognome', models.CharField(max_length=256)),
                ('Nazione', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='SingoliLibri',
            fields=[
                ('CodLibro', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('IDNonseriale', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='libri.nonseriale')),
                ('IDSeriale', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='libri.seriale')),
            ],
        ),
        migrations.AddField(
            model_name='seriale',
            name='Critico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='criticoS', to='libri.tradautcur'),
        ),
        migrations.AddField(
            model_name='seriale',
            name='IDAutoreCuratore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='libri.tradautcur'),
        ),
        migrations.AddField(
            model_name='seriale',
            name='IDCasaEd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='libri.casaeditrice'),
        ),
        migrations.AddField(
            model_name='seriale',
            name='IDCollana',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='libri.collane'),
        ),
        migrations.AddField(
            model_name='seriale',
            name='IDPostPrefazione',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='libri.postfazionepre'),
        ),
        migrations.AddField(
            model_name='seriale',
            name='Traduttore',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='traduttoreS', to='libri.tradautcur'),
        ),
        migrations.CreateModel(
            name='Prestito',
            fields=[
                ('CodPrestito', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('Dateinizio', models.DateField()),
                ('DataFine', models.DateField()),
                ('Ritardo', models.BooleanField(default=False)),
                ('IDLibro', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='libri.singolilibri')),
                ('IDUtente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='libri.utenti')),
            ],
        ),
        migrations.AddField(
            model_name='postfazionepre',
            name='autPostfazione',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='AutPost', to='libri.tradautcur'),
        ),
        migrations.AddField(
            model_name='postfazionepre',
            name='autPrefazione',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='AutPre', to='libri.tradautcur'),
        ),
        migrations.CreateModel(
            name='Posizione',
            fields=[
                ('CodPosizione', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('IDLibro', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='libri.singolilibri')),
                ('IDScaffale', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='libri.scaffale')),
            ],
        ),
        migrations.AddField(
            model_name='nonseriale',
            name='Critico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='criticoN', to='libri.tradautcur'),
        ),
        migrations.AddField(
            model_name='nonseriale',
            name='IDAutoreCuratore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='libri.tradautcur'),
        ),
        migrations.AddField(
            model_name='nonseriale',
            name='IDCasaEd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='libri.casaeditrice'),
        ),
        migrations.AddField(
            model_name='nonseriale',
            name='IDCollana',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='libri.collane'),
        ),
        migrations.AddField(
            model_name='nonseriale',
            name='IDPostPrefazione',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='libri.postfazionepre'),
        ),
        migrations.AddField(
            model_name='nonseriale',
            name='Traduttore',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='traduttoreN', to='libri.tradautcur'),
        ),
    ]
