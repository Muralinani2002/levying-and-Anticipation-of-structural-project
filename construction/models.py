# Create your models here.
from django.db import models

class MaterialQuality(models.Model):
    QUALITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    quality = models.CharField(max_length=100, choices=QUALITY_CHOICES)

    class Meta:
        db_table = 'construction_materialquality'



class DesignComplexity(models.Model):
    COMPLEXITY_CHOICES = [
        ('Complex', 'Complex'),
        ('Moderate', 'Moderate'),
        ('Simple', 'Simple'),
    ]
    complexity = models.CharField(max_length=10, choices=COMPLEXITY_CHOICES)

class ConstructionCost(models.Model):
    material_quality = models.ForeignKey(MaterialQuality, on_delete=models.CASCADE)
    design_complexity = models.ForeignKey(DesignComplexity, on_delete=models.CASCADE)
    cost = models.FloatField()
