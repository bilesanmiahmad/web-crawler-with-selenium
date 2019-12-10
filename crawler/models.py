from django.db import models
# from auditlog.models import AuditlogHistoryField
# from auditlog.registry import auditlog

# Create your models here.
# class PartyManagementServiceBaseModel(models.Model):
#     name = models.CharField(max_length=100, db_index=True, null=True, blank=True)
#     displayString = models.CharField(max_length=200, null=True, blank=True)
#     active = models.BooleanField(default=True)
#     activated = models.BooleanField(default=True)

#     # Audit properties
#     creation_date = models.DateTimeField(auto_now_add=True, editable=False, null=True)
#     last_modified_date = models.DateTimeField(auto_now=True, editable=False, null=True)
#     history = AuditlogHistoryField()

#     def __str__(self):
#         return self.name

#     class Meta:
#         abstract = True


class Schedule(models.Model):
    booking_number = models.BigIntegerField('Booking Number', unique=True)
    customer_reference = models.CharField('Customer Reference', max_length=20, blank=True)
    loading_port = models.CharField('Loading Port', max_length=50, blank=True)
    vessel_departure = models.DateField()
    vessel_name = models.CharField(max_length=30, blank=True)
    discharge_port = models.CharField(max_length=50, blank=True)
    created_date = models.DateField()
    created_by = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.booking_number)