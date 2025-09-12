# OROSPay QR redirector

Questo repository permette di creare un QR code che reindirizza automaticamente l’utente su App Store o Google Play in base al dispositivo.

## Come funziona
- Carica `index.html` su GitHub Pages.
- Genera il QR code con `generate_qr.py`, puntando all’URL GitHub Pages.

## Passi rapidi
1. Carica i file su GitHub in un nuovo repository.
2. Abilita GitHub Pages dalla root.
3. Aggiorna `generate_qr.py` con l’URL pubblicato e rigenera il QR code.

Il QR code risultante aprirà direttamente il corretto store su iOS e Android senza mostrare pagine intermedie.
