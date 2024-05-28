from django.db import models

class Insurance(models.Model):
    insurance_id = models.TextField()
    insurance_name = models.TextField()

    def __str__(self):
        return self.insurance_name


class Setting(models.Model):
    setting_name = models.CharField(max_length=255)
    setting_value = models.CharField(max_length=255)


class OfficeCode(models.Model):
    office_code_id = models.TextField()
    office_code_name = models.TextField()

    def __str__(self):
        return self.insurance_name
