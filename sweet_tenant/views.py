from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django_tenants.utils import schema_context, connection

# Create your views here.
from client.models import Client
from sweet_shared.models import *
from django.shortcuts import render
from sweet_shared.models import Certificate


@login_required
def public_createuser(request):
    public_username = request.POST['public_username']

    user = None
    with schema_context('public'):
        user = User.objects.create_user(username=public_username, password=public_username)
        user.first_name = public_username
        user.save()
    return user


@login_required
def public_add_certificate(request, user_name, certificate_name):
    awarded_by = request.user
    tenant_schema_name = connection.schema_name
    # tenant_schema = Client.objects.get(name=tenant_schema_name)

    certificate = None
    with schema_context('public'):
        user = User.objects.get(username=user_name)
        certificate = Certificate(name=certificate_name, awardee=user)
        # connection.set_tenant(tenant_schema)  # restore context
        certificate.tenant_schema_name = tenant_schema_name
        certificate.tenant_awarded_by_user_id = awarded_by.id
        # connection.set_schema_to_public()
        certificate.save()
    return certificate

@login_required
def certificates_awarded_by_me(request):
    tenant_schema_name = connection.schema_name
    certificates = Certificate.objects.filter(tenant_schema_name=tenant_schema_name, tenant_awarded_by_user_id=request.user.id)
    return render(request, 'certificates_awarded_by_me.html', context={'certificates': certificates})
