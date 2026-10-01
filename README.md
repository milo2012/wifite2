<pre align="center">
 ██████╗ ██╗  ██╗ ██████╗   ██████╗ ██████╗  ██████╗  ██╗  ██╗
██╔════╝ ╚██╗██╔╝ ██╔══██╗ ██╔════╝ ██╔══██╗ ██╔══██╗ ██║ ██╔╝
██║       ╚███╔╝  ██████╔╝ █████╗   ██████╔╝ ██║  ██║ █████╔╝
██║       ██╔██╗  ██╔══██╗ ██╔══╝   ██╔══██╗ ██║  ██║ ██╔═██╗
╚██████╗ ██╔╝ ██╗ ██████╔╝ ██████╗  ██║  ██║ ██████╔╝ ██║  ██╗
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚═╝  ╚═╝ ╚═════╝  ╚═╝  ╚═╝
</pre>

<h3 align="center">CyberDK - Automated Wireless Auditor</h3>
<p align="center">
  <strong>Created by</strong> @CyberDanish<br>
  <a href="https://github.com/CyberDanish/wifite2">https://github.com/CyberDanish/wifite2</a>
</p>

---

# Wifite2 - Automated Wireless Penetration Testing Tool

> **Fork differences (this repo vs upstream):** Enterprise networks are
> labeled separately from WPA-Personal, with observed outer EAP methods —
> powered by a patched airodump-ng ([milo2012/aircrack-ng](https://github.com/milo2012/aircrack-ng),
> `AUTH-EAP` column: `MGT`, `MGT+TEAP`, `MGT+PEAP`, …; the `Dockerfile`
> builds from that fork).
>
> ```text
> $ python3 Wifite2.py -i wlan1 --channel 6
>    NUM                      ESSID   CH  ENCR      POWER  WPS?  CLIENT
>    ---  -------------------------  ---  --------  -----  ----  ------
>      3                      test     6  WPE+TEAP   68db    no    1
> ```
>
> | ENCR | Meaning |
> |------|---------|
> | `WPA` | WPA-Personal (PSK) — handshake/PMKID attacks as before |
> | `WPE` | WPA-Enterprise, outer method not yet observed (stock airodump-ng, or no EAP exchange captured) |
> | `WPE+TLS` / `WPE+PEAP` / `WPE+TTLS` / `WPE+TEAP` | Enterprise with observed outer EAP method (patched airodump-ng) — pick tooling accordingly: EAP-TLS → hostapd-mana + portal (if validation is lax); PEAP/TTLS → eaphammer hash capture; TEAP → custom twin |
> | `WPE+T/P`, `WPE+2`, … | Mixed-method fleet on one SSID |
>
> Enterprise targets are display-only: wifite2 lists and filters them (kept
> under the `--wpa` filter) but launches no handshake attacks against them
> (`Unable to attack: no attacks available`, skipped).

[![License: GPL-2.0](https://img.shields.io/badge/License-GPL--2.0-blue.svg)](LICENSE)
[![Python 2.7+ / 3.x](https://img.shields.io/badge/Python-2.7%2B%20%7C%203.x-brightgreen.svg)](https://www.python.org/downloads/)
[![Kali Linux](https://img.shields.io/badge/Kali-Linux-268BEE.svg)](https://www.kali.org/)
[![Stars](https://img.shields.io/github/stars/CyberDanish/wifite2?style=social)](https://github.com/CyberDanish/wifite2/stargazers)

> **Wifite2** is a fast, automated wireless auditing tool for security researchers and authorized penetration testers. It streamlines **WEP/WPA/WPA2 handshake capture**, **WPS Pixie-Dust**, and **PMKID** workflows with a modular Python codebase, optimized scan and attack loops, and clean, readable output.

**Search Keywords:** `wifite2` `wireless-audit` `wifi-pentest` `wpa2-cracker` `wep-cracker` `wps-attack` `pmkid-capture` `kali-linux-tools` `python-security` `ethical-hacking` `penetration-testing`

---

## Key Features

| Feature | Description |
|---------|-------------|
| **WPA/WPA2** | Automated handshake capture and verification |
| **WPS Attack Suite** | Pixie-Dust offline + PIN brute-force (Reaver/Bully) |
| **PMKID Support** | Capture PMKID hashes without client deauth |
| **Fast Scanning** | Real-time target discovery with signal and channel filtering |
| **Modular Python** | Clean, extensible codebase for custom integrations |
| **Linux Focused** | Built for Kali and other penetration testing distros |
| **Clean Output** | Standard capture artifacts (pcap, csv, txt) for downstream tools |
| **Debug Mode** | Verbose logging for learning and troubleshooting |

---

## Requirements

### Hardware
- Wireless card supporting Monitor Mode and packet injection
- Compatible cards: http://www.aircrack-ng.org/doku.php?id=compatible_cards

### Software
**Required:**
- Python 2.7+ or 3.x
- Aircrack-ng suite (airmon-ng, airodump-ng, aireplay-ng, aircrack-ng, packetforge-ng)
- iw or iwconfig, ip or ifconfig

**Recommended:**
- tshark (Wireshark) for WPS detection
- reaver or bully for WPS attacks
- cowpatty or pyrit for handshake validation
- hashcat for PMKID cracking
- hcxdumptool and hcxpcaptool for PMKID capture

---

## Installation

### Quick Install (Recommended)
```bash
git clone https://github.com/CyberDanish/wifite2.git
cd wifite2
sudo python3 setup.py install
sudo wifite2
```

### Alternative Install
```bash
pip install .
```

---

## Usage

### Basic Usage
```bash
sudo wifite2
```

### Advanced Options
```bash
sudo wifite2 --help
```

### Common Commands
- Scan for WPS networks: `sudo wifite2 --wps`
- Target specific channel: `sudo wifite2 -c 6`
- Use PMKID only: `sudo wifite2 --pmkid`
- Crack existing handshake: `sudo wifite2 --crack`

---

## Attack Methods

1. WPS Pixie-Dust: Fast offline attack against vulnerable WPS implementations
2. WPS PIN Attack: Brute-force WPS PIN with optimized timing
3. PMKID Capture: Capture PMKID hashes for offline cracking
4. Handshake Capture: Deauthenticate clients to capture WPA handshakes
5. WEP Attacks: Fragmentation, chop-chop, and replay attacks

---

## Performance Optimizations

- Pixie-Dust timeout: 60 seconds (vs 300s)
- Failure thresholds reduced for faster failure detection
- Real-time target refresh every second
- Parallel attack validation

---

## Troubleshooting

- Ensure wireless card supports injection
- Run as root or sudo
- Update Aircrack-ng to the latest version
- Check dependencies with verbose mode: `wifite2 -v`

---

## Disclaimer

This tool is for educational and authorized security testing only. Use responsibly and in compliance with local laws.

---

## License

GNU GPLv2
