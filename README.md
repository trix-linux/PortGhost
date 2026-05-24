# Simple Python Nmap Port Scanner

Developed by **trix-linux**

A lightweight Python command-line utility built on top of `python-nmap` to quickly scan a target IP address for its top 1000 open ports. It provides structured, human-readable output mapping out the port, state, and associated service.

## Prerequisites

Before running this tool, you need to have **Nmap** installed on your system, as this Python script acts as a wrapper around the native application.

### 1. Install Nmap (System Dependent)
* **Linux (Debian/Ubuntu):**
```bash
  sudo apt update && sudo apt install nmap -y
```
macOS (using Homebrew):
```bash
  brew install nmap
```
**Windows: Download and run the installer from the official Nmap website.[(https://nmap.org/)]**

2. Install Python Dependencies
Install the required python-nmap library via pip:
```bash
  pip install python-nmap
```
**(Incase that didn't work on Linux try this method)**

## **Installation For Linux(Debian/Ubuntu/Kali)**
1. Install Nmap
```bash
  sudo apt update
  sudo apt install nmap -y
```
2. Install python-nmap (Recommended)
```bash 
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the library
pip install python-nmap
```
## **Usage**
1. Navigate to the project directory.
2. Run the script with sudo (required for stealth scan and OS detection):
```bash
  sudo venv/bin/python3 PortGhost.py
```
3. Enter the target IP address when prompted.

**Note: The script requires root privileges because it uses -sS (SYN scan) and -O (OS detection).
If you run it without sudo, you will get a "You requested a scan type which requires root privileges" error.**


## **How to Use**
1. Clone or download this repository to your local machine.

2. Open your terminal or command prompt and navigate to the project directory.

3. Run the script:
```bash
python scanner.py
```
4. Enter the target IP address when prompted (e.g. 192.168.1.1 or 127.0.0.1).

Note: Because Nmap sometimes requires elevated privileges for specific scan types, you may need to run the script with administrative privileges (sudo python scanner.py on Linux/macOS).

Example Output:
```bash
  enter the ip: 192.168.1.1

Scanning 192.168.1.1 on top 1000 ports
--------------------------------------------------
Nmap scan report for 192.168.1.1 (router.local)
Host is up
--------------------------------------------------

PORT      STATE    SERVICE
22/tcp    open     ssh
80/tcp    open     http
443/tcp   open     https

Scan finished.
```

Credits & License
Author: Trix-linux

GitHub: @trix-linux

**Disclaimer
This tool is intended strictly for educational purposes and authorized security testing on networks/hosts you own or have explicit permission to scan. Unauthorized scanning of third-party networks may be illegal. The author is not responsible for any misuse or damage caused by this utility.**
