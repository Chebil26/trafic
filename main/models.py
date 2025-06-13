from django.db import models

class Wilaya(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    # You can add additional fields here if needed

    def __str__(self):
        return self.name


class Commune(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    wilaya = models.ForeignKey('Wilaya', on_delete=models.CASCADE, related_name='communes')

    def __str__(self):
        return self.name


class Route(models.Model):
    id_route = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Section(models.Model):
    num_section = models.AutoField(primary_key=True)
    lieu_d = models.CharField(max_length=255)
    lieu_f = models.CharField(max_length=255)
    route = models.ForeignKey('Route', on_delete=models.CASCADE, related_name='sections')
    commune = models.ForeignKey('Commune', on_delete=models.CASCADE, related_name='sections')
    code = models.IntegerField (null=True)
   
    def __str__(self):
        return f"Section {self.code}: {self.lieu_d} -> {self.lieu_f}"


class BruteData(models.Model):
    id = models.AutoField(primary_key=True)
    section = models.ForeignKey('Section', on_delete=models.CASCADE, related_name='brute_data')

    def __str__(self):
        return f"BruteData {self.id} for Section {self.section.num_section}"


class Traffic(models.Model):
    id = models.OneToOneField('BruteData', on_delete=models.CASCADE, primary_key=True, related_name='traffic')
    date= models.DateField()
    heure= models.TimeField()
    trafic = models.FloatField()
    percent_PL = models.FloatField()
    percent_VL = models.FloatField()
    TJM_7d = models.IntegerField()
    TJM_5d = models.IntegerField()
    VL = models.FloatField()
    PL = models.FloatField()
    
    def __str__(self):
        return f"Trafic for BruteData {self.id_id}"


class Campagne(models.Model):
    id = models.AutoField(primary_key=True)
    annee = models.IntegerField()
    trimestre = models.IntegerField(choices=[(1, 'Q1'), (2, 'Q2'), (3, 'Q3'), (4, 'Q4')])
    brute_data = models.ManyToManyField('BruteData', related_name='campagnes')

    def __str__(self):
        return f"Campagne {self.annee} - T{self.trimestre}"
    

class sens(models.Model):
    id = models.AutoField(primary_key=True)
    sens = models.IntegerField(choices=[(1,'01'),(2,'02')])

    def __str__(self):
        return f"Sens {self.sens}"
