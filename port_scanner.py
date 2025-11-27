#!/usr/bin/env python3
"""
Port Scanner - Ethical port scanning tool for cybersecurity learning.
Author: [Tu Nombre o NyxShade]
Version: 1.0.0
Usage: Only on authorized systems (own hacklabs).
"""
import socket
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

def scan_port(target, port):
    """Scan single port using TCP connect."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        sock.close()
        return port if result == 0 else None
    except:
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 port_scanner.py <target_ip>")
        sys.exit(1)
    
    target = sys.argv[1]
    ports = range(1, 1025)  # Common ports
    print(f"[+] Scanning {target} | {datetime.now().strftime('%Y-%m-%d %H:%M')}")

    open_ports = []
    with ThreadPoolExecutor(max_workers=200) as executor:
        results = executor.map(lambda p: scan_port(target, p), ports)
        open_ports = [p for p in results if p]

    print(f"[+] Open ports: {sorted(open_ports)}")
    print("[!] Use responsibly: ethical hacking only.")

if __name__ == "__main__":
    main()
