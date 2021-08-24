from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django_tenants.utils import schema_context

from sweet_tenant.models import Event


class Certificate(models.Model):
    name = models.CharField(max_length=128)
    awardee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="certificates")

    tenant_schema_name = models.CharField(max_length=128)
    tenant_awarded_by_user_id = models.BigIntegerField()
    tenant_event_id = models.BigIntegerField()

    @property
    def awarded_to(self):
        awarded_to = None
        with schema_context('public'):
            awarded_to = User.objects.get(pk=self.awardee.id)

        return awarded_to

    @property
    def awarded_by(self):
        tenant_awarded_by = None
        with schema_context(self.tenant_schema_name):
            tenant_awarded_by = User.objects.get(pk=self.tenant_awarded_by_user_id)

        return tenant_awarded_by

    @property
    def event(self):
        event = None
        with schema_context(self.tenant_schema_name):
            event = Event.objects.get(pk=self.tenant_event_id)

        return event
