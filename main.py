import requests

# URL of the JSON file in your GitHub repository
GITHUB_JSON_URL = 'https://raw.githubusercontent.com/skittally/betterweb/domain/domain.json'

def fetch_mappings():
    try:
        response = requests.get(GITHUB_JSON_URL)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()        # Return the JSON data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching mappings: {e}")
        return {}

def lookup_domain(domain):
    mappings = fetch_mappings()
    ip_address = mappings.get(domain)
    
    if ip_address:
        print(f"IP Address for {domain}: {ip_address}")
    else:
        print(f"Domain {domain} not found.")

if __name__ == "__main__":
    domain_to_lookup = input("Enter the domain to look up: ")
    lookup_domain(domain_to_lookup)
