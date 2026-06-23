#!/bin/bash

set -e

echo "Starting Venterra EC2 patching workflow..."

echo "Checking services before patching..."
ansible-playbook -i inventories/hosts.ini playbooks/check-services.yml

echo "Running rolling patching..."
ansible-playbook -i inventories/hosts.ini playbooks/rolling-patch.yml

echo "Checking services after patching..."
ansible-playbook -i inventories/hosts.ini playbooks/check-services.yml

echo "Patching completed successfully."
echo "Reports are available in the reports/ folder."
