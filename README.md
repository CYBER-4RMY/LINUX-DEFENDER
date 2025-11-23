# 🛡️ Linux-Defender.sh

**Author:** [CYBER-4RMY](https://github.com/CYBER-4RMY)  
**Purpose:** Harden your Linux system with one script — efficient, practical, and secure.  

---

## 📌 Overview

`Linux-Defender.sh` is a comprehensive Linux system hardening script built for security professionals, enthusiasts, and system admins.  
It automates the installation and configuration of key security tools across popular Linux distributions.

---

## 🚀 Features

- ✅ **Firewall setup** using `ufw`
- 🦠 **Malware & rootkit scanners**: `chkrootkit`, `rkhunter`, `clamav`
- 🔍 **Audit daemon** for system activity: `audit` / `auditd`
- 🌐 **TOR support** and optional **Anonsurf** for Kali
- **AI Implemented** now i added tgpt for ai support and your query solution
- ⚙️ Auto-detection of distro: Arch, Debian, Kali, Parrot
- 💣 Fail-safe: gives manual package install instructions on failure

---

## 🐧 Supported Distros

- Arch Linux
- Kali Linux
- Parrot OS
- Debian

---

## 📦 Tools Installed

| Category           | Tool(s)                                         |
|--------------------|--------------------------------------------------|
| Firewall           | `ufw`, `iptables`                                |
| Malware Protection | `chkrootkit`, `rkhunter`, `clamav`               |
| Monitoring         | `audit` / `auditd`, `inotify-tools`, `inxi`      |
| Anonymity (Kali)   | `tor`, [`kali-anonsurf`](https://github.com/Und3rf10w/kali-anonsurf) |
| Arch-only Tool     | `torctl`                                         |
| AI                 | `TGPT`                                           |

---

## ⚙️ Installation

```bash
git clone https://github.com/CYBER-4RMY/LINUX-DEFENDER.git
cd Linux-Defender
chmod +x setup.py
./setup.py
````

If setup fails, the script will suggest exact commands for manual installation based on your OS.

---

## 🧰 Running the Defender

Once dependencies are installed:

(RUN THIS SCRIPT IN ROOT USER)
```bash
chmod +x Linux-Defender.sh
sudo ./Linux-Defender.sh
```

This will initiate all hardening operations tailored for your Linux system.
--- 

## 🧾 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Built with care and cybersecurity principles by [CYBER-4RMY](https://github.com/CYBER-4RMY)
*“Secure it before someone else exploits it.”*

---

## ☕ Support & Contribution

For major changes, open an issue first to discuss what you would like to change.
If this project helps secure your systems, consider giving it a ⭐ on GitHub.
