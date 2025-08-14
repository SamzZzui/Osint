import whois

def lookup(domain):
    try:
        domain_info = whois.whois(domain)
        print(f"Domain: {domain_info.domain_name}")
        print(f"Registrar: {domain_info.registrar}")
        print(f"Creation Date: {domain_info.creation_date}")
        print(f"Expiration Date: {domain_info.expiration_date}")
        print(f"Name Servers: {domain_info.name_servers}")
    except Exception as e:
        print(f"Error retrieving domain info: {e}")