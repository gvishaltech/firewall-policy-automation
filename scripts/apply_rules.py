import json
import os
from datetime import datetime

def load_rules(file_path):
    with open(file_path) as f:
        return json.load(f)

def backup_config(config_data):
    backup_dir = "backup"
    os.makedirs(backup_dir, exist_ok=True)
    filename = f"{backup_dir}/backup_config_{datetime.now().strftime('%Y_%m_%d')}.txt"
    with open(filename, "w") as f:
        f.write(config_data)

def apply_firewall_rules(rules):
    for rule in rules:
        print(f"Applying rule: {rule['action'].upper()} {rule['service']} "
              f"from {rule['source']} to {rule['destination']}:{rule['port']}")
        # Add actual firewall CLI/API integration here

if __name__ == "__main__":
    rule_file = "data/firewall_rules.json"
    rules = load_rules(rule_file)

    # Optional: backup existing config
    backup_config("Sample backup config from firewall")

    # Apply rules
    apply_firewall_rules(rules)
