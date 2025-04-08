document.addEventListener('DOMContentLoaded', function() {
    const typeField = document.getElementById('id_type');
    const certSettings = document.querySelector('.field-ca_name, .field-duration, .field-key_length, .field-digest_algorithm');

    function toggleCertSettings() {
        certSettings.style.display = typeField.value === 'certificate' ? 'block' : 'none';
    }

    typeField.addEventListener('change', toggleCertSettings);
    toggleCertSettings();
});