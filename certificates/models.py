from django.db import models

class Template(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=16, choices=[
        ('generic', 'Generic'),
        ('certificate', 'Certificate'),
    ])
    ca_name = models.CharField(max_length=100, blank=True, null=True, help_text="Certificate Authority name")
    duration = models.IntegerField(blank=True, null=True, help_text="Duration in days")
    key_length = models.IntegerField(blank=True, null=True, choices=[(2048, '2048'), (4096, '4096')])
    digest_algorithm = models.CharField(max_length=8, blank=True, null=True, choices=[('sha256', 'SHA-256'), ('sha512', 'SHA-512')])

    def __str__(self):
        return self.name

class Certificate(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    public_key = models.TextField()
    private_key = models.TextField()
    uuid = models.CharField(max_length=36)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name