from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Certificate
from .utils import generate_certificate_from_template

def certificate_details(request, certificate_id):
    certificate = get_object_or_404(Certificate, id=certificate_id)
    context = {
        'certificate': certificate,
        'name': certificate.name,
        'public_key': certificate.public_key,
        'private_key': certificate.private_key,
        'uuid': certificate.uuid,
        'template': certificate.template,
    }
    
    # Simulate passing to a config
    config_snippet = f"""
    # Device Configuration
    certificate_uuid: {certificate.uuid}
    public_key: {certificate.public_key}
    private_key: {certificate.private_key}
    """
    context['config_snippet'] = config_snippet
    
    return render(request, 'certificate_details.html', context)

def download_certificate(request, certificate_id, file_type):
    certificate = get_object_or_404(Certificate, id=certificate_id)
    if file_type == 'crt':
        content = certificate.public_key
        filename = f"{certificate.name}.crt"
    elif file_type == 'key':
        content = certificate.private_key
        filename = f"{certificate.name}.key"
    else:
        return HttpResponse("Invalid file type", status=400)
    
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response