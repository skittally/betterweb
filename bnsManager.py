import requests
import json
import os

def load_github_url():
    config_path = 'bns-conf/bns.json'
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = json.load(f)
            return config.get("github_url")
    else:
        print("Configuration file not found.")
        return None

def fetch_mappings(github_url):
    try:
        response = requests.get(github_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching mappings: {e}")
        return {}
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
        return {}

def lookup_domain(domain, github_url):
    mappings = fetch_mappings(github_url)
    ip_address = mappings.get(domain)
    
    if ip_address:
        return ip_address
    else:
        print(f"Domain {domain} not found.")

def lookup(domain_to_lookup):
    github_url = load_github_url()
    if github_url:
        lookup_domain(domain_to_lookup, github_url)
        return ip_address

#if __name__ == "__main__":
#    lookup(domain_to_lookup)