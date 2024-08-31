# Generated by Django 5.0.7 on 2024-07-30 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DesignComplexity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complexity', models.CharField(choices=[('Complex', 'Complex'), ('Moderate', 'Moderate'), ('Simple', 'Simple')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialQuality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ConstructionCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField()),
                ('design_complexity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construction.designcomplexity')),
                ('material_quality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construction.materialquality')),
            ],
        ),
    ]
