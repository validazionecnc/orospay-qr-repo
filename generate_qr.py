#!/usr/bin/env python3
"""
Genera un QR code PNG che punta alla pagina di redirect.
Requisiti: pip install qrcode[pil]
"""
import qrcode

# Inserisci qui l'URL GitHub Pages una volta pubblicato index.html
redirector_url = 'https://tuoutente.github.io/orospay-qr-repo/'

if not redirector_url:
    raise SystemExit('Imposta redirector_url nel file generate_qr.py')

img = qrcode.make(redirector_url)
output_file = 'orospay-redirect-qr.png'
img.save(output_file)
print(f'QR generato in: {output_file}\nContenuto QR: {redirector_url}')