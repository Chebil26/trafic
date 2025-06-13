from django.db import models


class Wilaya(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name or f"Wilaya {self.id}"


class Commune(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    wilaya = models.ForeignKey('Wilaya', on_delete=models.CASCADE, related_name='communes', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.wilaya.name if self.wilaya else 'No Wilaya'})"


class Route(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name or f"Route {self.id}"


class Section(models.Model):
    lieu_d = models.CharField(max_length=255, null=True, blank=True)
    lieu_f = models.CharField(max_length=255, null=True, blank=True)
    route = models.ForeignKey('Route', on_delete=models.CASCADE, related_name='sections', null=True, blank=True)
    commune = models.ForeignKey('Commune', on_delete=models.CASCADE, related_name='sections', null=True, blank=True)
    code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Section {self.code} ({self.lieu_d} → {self.lieu_f})"


class BruteData(models.Model):
    section = models.ForeignKey('Section', on_delete=models.CASCADE, related_name='brute_data', null=True, blank=True)

    def __str__(self):
        return f"BruteData {self.id} (Section {self.section.code if self.section else 'No Section'})"


class Traffic(models.Model):
    id = models.OneToOneField('BruteData', on_delete=models.CASCADE, primary_key=True, related_name='traffic')
    date = models.DateField(null=True, blank=True)
    heure = models.TimeField(null=True, blank=True)
    trafic = models.FloatField(null=True, blank=True)
    percent_PL = models.FloatField(null=True, blank=True)
    percent_VL = models.FloatField(null=True, blank=True)
    TJM_7d = models.IntegerField(null=True, blank=True)
    TJM_5d = models.IntegerField(null=True, blank=True)
    VL = models.FloatField(null=True, blank=True)
    PL = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Traffic on {self.date} at {self.heure} (ID {self.id_id})"


class Campagne(models.Model):
    annee = models.IntegerField(null=True, blank=True)
    trimestre = models.IntegerField(
        choices=[(1, 'Q1'), (2, 'Q2'), (3, 'Q3'), (4, 'Q4')],
        null=True,
        blank=True
    )
    brute_data = models.ManyToManyField('BruteData', related_name='campagnes', blank=True)

    def __str__(self):
        return f"Campagne {self.annee} - T{self.trimestre}"


class Sens(models.Model):
    sens = models.IntegerField(choices=[(1, '01'), (2, '02')], null=True, blank=True)

    def __str__(self):
        return f"Sens {self.get_sens_display() if self.sens else 'N/A'}"
