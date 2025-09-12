# Orospay Redirect QR

Pagina HTML e script Python per generare un QR code che reindirizza rapidamente su Android o iOS.

## Contenuto

- `index.html` : pagina con redirect immediato (timeout 0,01s)
- `generate_qr.py` : script Python per creare il QR code
- `orospay-redirect-qr.png` : QR code generato
- `LICENSE` : licenza MIT

## Uso

Apri `index.html` su GitHub Pages o altro server statico.  
Per rigenerare il QR code:
```bash
python generate_qr.py
