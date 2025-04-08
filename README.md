# X.509 Certificate Generator Prototype

This is a prototype for my GSoC 2025 proposal to add X.509 Certificate Generator Templates to OpenWISP. It shows how users can create certificate templates and generate certificates with options like duration and key length. Below are instructions to set it up and run it locally.

## Prerequisites
Before you start, make sure you have these installed:
- **Python 3.8 or higher** (check with `python --version` or `python3 --version`)
- **Git** (check with `git --version`)
- **pip** (Python package manager, usually comes with Python)

## Installation Steps
Follow these steps carefully to run the prototype on your local machine:

1. **Clone the Repository**  
   ```git clone https://github.com/SitaGanesh/x509-certificate-generator-prototype.git```
   
  ```cd x509-certificate-generator-prototype```
  
2. **Set Up a Virtual Environment**  
Create and activate a virtual environment to keep things clean:
- On Windows:
  
    ```python -m venv venv```

    ```venv\Scripts\activate```
  
- On Mac/Linux:
  
    ```python3 -m venv venv```

    ```source venv/bin/activate```

You’ll see `(venv)` in your terminal when it’s active.

3. **Install Dependencies**  
Install Django with this command:

   ```pip install django```


4. **Set Up the Database**  
Run these commands to create and prepare the SQLite database:

```
python manage.py makemigrations
python manage.py migrate
```

5. **Create a Superuser**  
Set up an admin account to log in:

```
python manage.py createsuperuser
```

6. **Run the Server**  
Start the Django development server:

```
python manage.py runserver
```

You’ll see a message like `Starting development server at http://127.0.0.1:8000/`.

7. **Access the Admin Panel**  
Open your browser and go to:

```http://127.0.0.1:8000/admin/```

Log in with the superuser credentials you created.


## How to Test It
1. In the admin panel, click “Templates” under the “Certificates” section.
2. Click “Add Template,” fill in details (e.g., Name: `WebServerCert`, Type: `General Purpose Certificate`), and save.
3. Select the template, choose “Generate Certificate” from the actions dropdown, and click “Go.”
4. Check the “Certificates” section to see the generated certificate with keys and UUID.
5. Visit `http://127.0.0.1:8000/certificate/<id>/` (replace `<id>` with the certificate’s ID) to see its details.

### Notes
- This prototype uses simulated keys for now. In OpenWISP, it’ll use real certificate generation.
- The code is a starting point for my GSoC project, showing the workflow I’ll build on.

If you run into issues, feel free to contact me!




## Code Templates with Explanations


models.py

```
from django.db import models

class Template(models.Model):
    TYPE_CHOICES = [('certificate', 'General Purpose Certificate'), ('other', 'Other')]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='certificate')
    ca_name = models.CharField(max_length=100, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True, help_text="In days")
    key_length = models.IntegerField(blank=True, null=True, default=2048)
    digest_algorithm = models.CharField(max_length=50, blank=True, null=True, default='sha256')

    def __str__(self): return self.name

class Certificate(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    public_key = models.TextField()
    private_key = models.TextField()
    uuid = models.UUIDField(unique=True)

```

- What It Does: Defines the Template for creating certificates and the Certificate to store generated ones. Users set options like key length here.
- In OpenWISP: This will store the new template type and link to OpenWISP’s CA system, letting users generate certificates for any purpose.

utils.py

```
import uuid
from .models import Template

def generate_certificate_from_template(template):
    if template.type != 'certificate':
        raise ValueError("Not a certificate template")
    key_length = template.key_length or 2048
    digest = template.digest_algorithm or 'sha256'
    cert_name = f"Cert_{template.name}_{uuid.uuid4().hex[:8]}"
    public_key = f"-----BEGIN PUBLIC KEY-----\n(Simulated {key_length}-bit public key)\n-----END PUBLIC KEY-----"
    private_key = f"-----BEGIN PRIVATE KEY-----\n(Simulated {key_length}-bit private key)\n-----END PRIVATE KEY-----"
    return {'name': cert_name, 'public_key': public_key, 'private_key': private_key, 'uuid': str(uuid.uuid4())}
```

-What It Does: Takes a template and generates a certificate with keys and a UUID.
-In OpenWISP: This will connect to OpenWISP’s real certificate generation (instead of fake keys) to create usable X.509 certificates.

admin.py

```
from django.contrib import admin
from .models import Template, Certificate
from .utils import generate_certificate_from_template

class TemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    fieldsets = [
        (None, {'fields': ['name', 'type']}),
        ('Certificate Settings', {'fields': ['ca_name', 'duration', 'key_length', 'digest_algorithm'], 'classes': ['collapse']}),
    ]
    actions = ['generate_certificate']

    def generate_certificate(self, request, queryset):
        for template in queryset.filter(type='certificate'):
            cert_info = generate_certificate_from_template(template)
            Certificate.objects.create(template=template, **cert_info)
            self.message_user(request, f"Generated certificate for {template.name}")
```

- What It Does: Adds a custom admin interface to manage templates and generate certificates with one click.
- In OpenWISP: This will integrate with OpenWISP’s admin panel, making it easy for users to create and manage certificates.

views.py

```
from django.shortcuts import render, get_object_or_404
from .models import Certificate

def certificate_details(request, certificate_id):
    certificate = get_object_or_404(Certificate, id=certificate_id)
    config_snippet = f"certificate_uuid: {certificate.uuid}\npublic_key: {certificate.public_key}"
    return render(request, 'certificate_details.html', {'certificate': certificate, 'config_snippet': config_snippet})
```

- What It Does: Shows certificate details and a config snippet for use.
- In OpenWISP: This will expose keys and UUID as variables for OpenWISP’s configuration system, automating deployment.

