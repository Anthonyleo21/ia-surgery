from django.db import models

# Create your models here.

class Surgery(models.Model):
    surgery = models.PositiveSmallIntegerField()
    hospital_number = models.PositiveSmallIntegerField()
    age = models.IntegerField()  # Permitir números negativos
    reactal_temp = models.FloatField()  # Permitir decimales
    pulse = models.IntegerField()
    respiratory_rate = models.IntegerField()
    mucous_membrane = models.PositiveSmallIntegerField()
    capillary_refill_time = models.PositiveSmallIntegerField()
    peristalsis = models.IntegerField()  # Permitir números negativos
    abdominal_distention = models.IntegerField()
    nasogastric_tube = models.IntegerField()
    nasogastric_reflux = models.IntegerField()
    nasogastric_reflux_ph = models.FloatField()  # Permitir decimales
    rectal_exam_feces = models.IntegerField()
    abdomen = models.IntegerField()
    packed_cell_volume = models.FloatField()  # Permitir decimales
    total_protein = models.FloatField()  # Permitir decimales
    abdomo_appearance = models.IntegerField()
    abdomo_protein = models.FloatField()  # Permitir decimales
    surgical_lesion = models.IntegerField()
    lesion_1 = models.IntegerField()
    lesion_2 = models.IntegerField()
    lesion_3 = models.IntegerField()
    co_data = models.IntegerField()
    outcome = models.IntegerField()
