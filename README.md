# Orospay QR Redirect

Redirect invisibile su Android/iOS usando Vercel serverless function.

## Contenuto

- `index.html` : fallback desktop con loader
- `api/redirect.js` : redirect serverless
- `generate_qr.py` : script Python per generare QR code
- `orospay-redirect-qr.png` : QR code generato
- `.gitignore`

## Uso

1. Deploy del repository su Vercel
2. Aggiornare il link in `generate_qr.py` con l'URL Vercel
3. Eseguire `python generate_qr.py` per creare il QR code
