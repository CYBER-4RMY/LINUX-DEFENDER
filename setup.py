#!/usr/bin/env python3

import os
import shutil
import stat
import subprocess
import sys

SCRIPT_NAME = "defender.sh"
INSTALL_NAME = "defender"
INSTALL_PATH = "/usr/local/bin"

arch_packages = [
    "tor", "chkrootkit", "clamav", "audit", "iptables",
    "ufw", "inotify-tools", "rkhunter", "inxi", "xterm"
]

debian_packages = [
    "tor", "chkrootkit", "clamav", "auditd", "iptables",
    "ufw", "inotify-tools", "rkhunter", "inxi", "xterm"
]

# ──────────────────────────────────────────────────────────────

def run_cmd(command):
    subprocess.run(command, shell=True, check=True)

def get_distro():
    if os.path.exists("/etc/os-release"):
        with open("/etc/os-release") as f:
            data = f.read().lower()
            if "arch" in data:
                return "arch"
            elif "garuda" in data:
                return "garuda"
            elif "kali" in data:
                return "kali"
            elif "parrot" in data:
                return "parrot"
            elif "debian" in data:
                return "debian"
            elif "ubuntu" in data:
                return "ubuntu"
    return "unknown"

# ──────────────────────────────────────────────────────────────

def install_packages(distro):
    try:
        if distro == "arch", "garuda":
            run_cmd("sudo pacman -Syu --noconfirm")
            run_cmd("sudo pacman -S --noconfirm " + " ".join(arch_packages))

        elif distro in ["debian", "kali", "parrot", "ubuntu"]:
            run_cmd("sudo apt update && sudo apt upgrade -y")
            run_cmd("sudo apt install -y " + " ".join(debian_packages))

            if distro == "kali", "ubuntu":
                print("[INFO] Installing kali-anonsurf...")
                if not os.path.isdir("kali-anonsurf"):
                    run_cmd("git clone https://github.com/Und3rf10w/kali-anonsurf.git")
                run_cmd("cd kali-anonsurf && sudo ./installer.sh")

        else:
            print("[ERROR] Unsupported distro.")
            sys.exit(1)

    except subprocess.CalledProcessError:
        print("[ERROR] Dependency installation failed.")
        sys.exit(1)

# ──────────────────────────────────────────────────────────────

def validate_script():
    if not os.path.isfile(SCRIPT_NAME):
        print(f"[ERROR] {SCRIPT_NAME} not found in current directory.")
        sys.exit(1)

    os.chmod(SCRIPT_NAME, os.stat(SCRIPT_NAME).st_mode | stat.S_IEXEC)

# ──────────────────────────────────────────────────────────────

def system_wide_install():
    choice = input("➡️  Install system-wide as command 'defender'? [y/N]: ").strip().lower()

    if choice != "y":
        print("[INFO] Skipped system-wide installation.")
        print("[INFO] Run manually using: ./defender.sh")
        return

    if os.geteuid() != 0:
        print("[ERROR] System-wide installation requires root privileges.")
        print("        Re-run with: sudo python3 setup.py")
        sys.exit(1)

    src = os.path.abspath(SCRIPT_NAME)
    dst = os.path.join(INSTALL_PATH, INSTALL_NAME)

    try:
        shutil.copy(src, dst)
        os.chmod(dst, os.stat(dst).st_mode | stat.S_IEXEC)
        print(f"[SUCCESS] Installed successfully: {dst}")
        print(f"[INFO] You can now run it using: {INSTALL_NAME}")
    except Exception as e:
        print(f"[ERROR] Installation failed: {e}")
        sys.exit(1)

# ──────────────────────────────────────────────────────────────

def main():
    distro = get_distro()
    print(f"[INFO] Detected Linux distribution: {distro}")

    install_packages(distro)
    validate_script()
    system_wide_install()

    print("\n✅ Setup complete. Stay secure.")

# ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
