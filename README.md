# AWS EC2 Ansible Patching Project

This project automates patching for Linux and Windows EC2 instances using Ansible.

## Project Overview

The environment includes:

- Linux EC2 running Dockerized Flask API behind Nginx
- Windows EC2 running IIS Resident Portal
- Ansible control node for automation
- Jenkins pipeline for scheduled patching
- Patch reports generated after execution

## Tools Used:

- AWS EC2
- Ansible
- Linux
- Windows Server
- WinRM
- SSH
- Docker
- Nginx
- IIS
- Jenkins
- GitHub

## Workflow

1. Validate services before patching
2. Patch Linux EC2 servers
3. Patch Windows EC2 servers
4. Reboot servers when required
5. Validate Nginx and IIS after patching
6. Generate patch reports
7. Archive reports in Jenkins

## Run Manually

```bash
./scripts/run-patching.sh
