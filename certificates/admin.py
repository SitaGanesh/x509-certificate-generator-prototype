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
            Certificate.objects.create(
                template=template,
                name=cert_info['name'],
                public_key=cert_info['public_key'],
                private_key=cert_info['private_key'],
                uuid=cert_info['uuid']
            )
            self.message_user(request, f"Generated and saved certificate for {template.name}: {cert_info['name']}")

    class Media:
        js = ('js/template_admin.js',)

admin.site.register(Template, TemplateAdmin)
admin.site.register(Certificate)