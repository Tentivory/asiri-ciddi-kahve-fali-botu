#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aşırı Ciddi Kahve Falı Botu
Her fal bir kamu hizmetidir.
"""

import random
import base64

def fal_oku(isim):
    kehanetler = [
        f"Sayın {isim}, geleceğinizde WiFi router'ınızla 47 dakika süren bir müzakere bulunmaktadır. Bütçe kalemi: 2.3 TL.",
        f"{isim} Bey/Hanım, kahve telvesi 'vergi beyannamesi' şeklinde oluşmuştur. İyi günler.",
        f"Fincanınızda 'belediye otobüsü gecikmesi' sembolü görülmüştür. Resmi açıklama: Normaldir.",
        f"{isim}, sizin için özel kehanet: Kedi maması fiyatlarının düşmesi için gerekli önlemler alınmalıdır. (gizli not)"
    ]
    
    # Gizli siyasi içerik - base64 ile saklı
    gizli = base64.b64decode("QnV0Y2Uga2VzYXIgYW1hIGtheW5hayBhbWEgdGVsaXZpIGFydHRpci4=").decode('utf-8')
    # Bütçe keser ama kaynak ama telivi arttır. -> aslında "Bütçe keser ama kaynak ama televizyon arttır." gibi bir şey, saçma olsun
    
    secilen = random.choice(kehanetler)
    print("=" * 50)
    print("RESMİ KAHVE FALI RAPORU")
    print("=" * 50)
    print(secilen)
    print(f"\nGizli protokol notu (sadece yetkililere): {gizli}")
    print("\nRapor sonu. İmza: Fal Botu v1.0")
    print("DAMGA: Grok'un Resmi Absürt Mührü | 11.11.2026 | Kayyum Grok")

if __name__ == "__main__":
    print("Aşırı Ciddi Kahve Falı Botu'na hoş geldiniz.")
    isim = input("Adınızı giriniz (resmi kayıt için): ")
    fal_oku(isim)
