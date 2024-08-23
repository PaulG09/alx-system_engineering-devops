# 0x0B. SSH

## Overview

SSH (Secure Shell) is a protocol for securely accessing and managing remote servers. It encrypts data to ensure secure communication over insecure networks.

## Key Concepts

- **SSH Key Authentication:** Uses cryptographic keys (private and public) for secure login, avoiding passwords.
- **Configuration Files:** 
  - **Server:** `/etc/ssh/sshd_config`
  - **Client:** `~/.ssh/config`
- **Common Commands:**
  - `ssh username@hostname` - Connect to a remote server.
  - `scp localfile username@hostname:/remotepath` - Copy files securely.
  - `sftp username@hostname` - Transfer files using SFTP.

## Setup Instructions

1. **Generate SSH Keys:**
   ```sh
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
2. **Install SSH Server (Ubuntu):**
   ```sh
   sudo apt-get install openssh-server
   ```
3. **Connect to Remote Server:**
   ```sh
   ssh username@remote_server_ip
   ```

## Troubleshooting

- **Connection Issues:** Check SSH service and firewall rules.
- **Authentication Errors:** Ensure correct key setup in `~/.ssh/authorized_keys`.

## Resources

- [SSH Documentation](https://www.openssh.com/manual.html)
- [Understanding SSH Keys](https://www.ssh.com/academy/ssh/key).
