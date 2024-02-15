from django.db import models


class HeartDiseasePrediction(models.Model):
    age = models.IntegerField(verbose_name="Age of the individual")
    sex = models.BooleanField(
        verbose_name="Gender of the individual (1 = male, 0 = female)"
    )
    cp = models.CharField(max_length=255, verbose_name="Chest pain type")
    trestbps = models.IntegerField(verbose_name="Resting blood pressure (in mm Hg)")
    chol = models.IntegerField(verbose_name="Serum cholesterol level (in mg/dl)")
    fbs = models.BooleanField(
        verbose_name="Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)"
    )
    restecg = models.CharField(
        max_length=255, verbose_name="Resting electrocardiographic results"
    )
    thalach = models.IntegerField(verbose_name="Maximum heart rate achieved")
    exang = models.BooleanField(
        verbose_name="Exercise-induced angina (1 = yes, 0 = no)"
    )
    oldpeak = models.FloatField(
        verbose_name="ST depression induced by exercise relative to rest"
    )
    slope = models.CharField(
        max_length=255, verbose_name="The slope of the peak exercise ST segment"
    )
    ca = models.IntegerField(
        verbose_name="Number of major vessels colored by fluoroscopy"
    )
    thal = models.CharField(
        max_length=255,
        verbose_name="Thalassemia - a blood disorder (3 = normal; 6 = fixed defect; 7 = reversible defect)",
    )

    def _str_(self):
        return f"Age: {self.age}, Sex: {'Male' if self.sex else 'Female'}, Chest Pain Type: {self.cp}"
