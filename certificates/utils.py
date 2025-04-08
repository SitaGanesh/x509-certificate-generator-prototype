import uuid
from .models import Template

def generate_certificate_from_template(template):
    if template.type != 'certificate':
        raise ValueError("Not a certificate template")
    
    # Simulate key generation based on key_length and digest_algorithm
    key_length = template.key_length or 2048
    digest = template.digest_algorithm or 'sha256'
    cert_name = f"Cert_{template.name}_{uuid.uuid4().hex[:8]}"
    
    # Simulated keys (placeholders, not cryptographic, but formatted realistically)
    public_key = f"-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA\n(Simulated {key_length}-bit public key for {template.name})\n-----END PUBLIC KEY-----"
    private_key = f"-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC\n(Simulated {key_length}-bit private key for {template.name})\n-----END PRIVATE KEY-----"
    
    cert_info = {
        'name': cert_name,
        'public_key': public_key,
        'private_key': private_key,
        'uuid': str(uuid.uuid4()),
    }
    return cert_info