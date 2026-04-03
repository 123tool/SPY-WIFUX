#!/bin/bash
# ==========================================
# INSTALLER : SPY-WIFUX-PRO (NAGA-WIFUX)
# BRAND     : SPY-E & 123Tool
# ==========================================

GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m'

clear
echo -e "${CYAN}[*] Menginstall Dependensi NAGA-WIFUX (Premium)...${NC}"

if [[ -d /data/data/com.termux ]]; then
    # Jika di Termux
    pkg update && pkg upgrade -y
    pkg install python nmap tsu wireless-tools root-repo -y
    pkg install aircrack-ng reaver pixiewps -y
else
    # Jika di Linux (Kali/Ubuntu/Debian)
    sudo apt update
    sudo apt install -y python3 aircrack-ng reaver pixiewps wash wireless-tools
fi

chmod +x spy_wifux.py
echo -e "${GREEN}[+] Sukses! Jalankan dengan: sudo python3 spy_wifux.py${NC}"
