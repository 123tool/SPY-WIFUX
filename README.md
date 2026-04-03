# 📡 SPY WIFUX
> **Advanced WPS Exploit & Wireless Auditing Framework for Android & Linux**

![Platform](https://img.shields.io/badge/Platform-Termux%20(Root)%20%7C%20Linux-red.svg)
![Version](https://img.shields.io/badge/Version-2.0--Premium-gold.svg)
![Brand](https://img.shields.io/badge/Brand-SPY--E%20%26%20123Tool-blue.svg)

**SPY WIFUX** adalah tool automasi audit keamanan WiFi yang menggabungkan teknik serangan Pixie-Dust dan Brute-Force PIN WPS. Dirancang untuk efisiensi maksimal pada perangkat mobile dan terminal Linux.

## ⚡ Fitur Utama (Full Pro)
- **Auto-Pixie Dust:** Mencari kunci enkripsi dalam hitungan detik pada router rentan.
- **WPS Lock Detection:** Mendeteksi otomatis jika router target sedang terkunci.
- **Multi-Tool Integration:** Menggabungkan kekuatan `Reaver`, `Pixiewps`, dan `Bully`.
- **Smart Recon:** Scanning SSID dengan indikator kekuatan sinyal (RSSI) yang akurat.
- **One-Click Install:** Script instalasi otomatis untuk semua dependensi.

## 📥 Instalasi

### 📱 Termux (Root Required)
*Pastikan HP sudah Root dan support Monitor Mode.*
```bash
pkg install python git tsu -y
git clone https://github.com/123tool/SPY-WIFUX.git
cd SPY-WIFUX
chmod +x install.sh
sudo ./install.sh
```
## 🐧 Linux (Kali/Ubuntu/Parrot)
```bash
git clone https://github.com/123tool/SPY-WIFUX.git
cd SPY-WIFUX
sudo chmod +x install.sh
sudo ./install.sh
```
## 🚀 Cara Penggunaan
​Jalankan tool: sudo python3 spy_wifux.py
​Pilih Interface (Contoh: wlan0 atau wlan0mon).
​Pilih mode "Auto-Scan WPS".
​Pilih target nomor SSID.
​Gass! Tool akan mencoba Pixie-Dust attack secara otomatis.

## Kelebihan :

​**Fokus Pixie-Dust** : 
Beda sama cara manual yang ribet, script ini langsung mengarahkan ke serangan Pixie-Dust (-K 1) yang bisa bobol WiFi dalam hitungan detik tanpa nunggu berjam-jam.

**​Optimasi Wash** : 
Saya pakai wash untuk scanning, karena wash jauh lebih akurat buat mendeteksi apakah WPS router itu Locked atau Unlocked.

**​Tips** : 
Harus punya Wifi Adapter External (seperti TP-Link TL-WN722N v1 atau Alfa AWUS) kalau main di laptop/PC, karena kartu wifi bawaan jarang ada yang support packet injection.

​⚠️ Disclaimer
> **​Tool ini dibuat untuk tujuan Edukasi dan Audit Penetrasi Resmi. Penyalahgunaan alat ini untuk tindakan ilegal sepenuhnya tanggung jawab pengguna. SPY-E & 123Tool mendukung keamanan siber yang bertanggung jawab.**
