# Generated by Django 3.2 on 2021-08-02 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constat_d_etat', '0009_auto_20210801_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artgraphique',
            name='absence_cadre',
        ),
        migrations.RemoveField(
            model_name='peinturesurbois',
            name='absence_cadre',
        ),
        migrations.RemoveField(
            model_name='peinturesurtoile',
            name='absence_cadre',
        ),
        migrations.AddField(
            model_name='constatartgraphique',
            name='absence_cadre',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='constatpeinturesurbois',
            name='absence_cadre',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='constatpeinturesurtoile',
            name='absence_cadre',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='constatartgraphique',
            name='auteur',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='constatartgraphique',
            name='remarque',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='constatpeinturesurbois',
            name='auteur',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='constatpeinturesurbois',
            name='remarque',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='constatpeinturesurtoile',
            name='auteur',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='constatpeinturesurtoile',
            name='remarque',
            field=models.TextField(null=True),
        ),
    ]
