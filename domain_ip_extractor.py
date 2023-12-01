import re
import sys

def read_domain_extensions(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def extract_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""

def find_domains_and_ips(text, extensions):
    # Split extensions into single and duo TLDs
    single_tlds = [ext for ext in extensions if '.' not in ext]
    duo_tlds = [ext for ext in extensions if '.' in ext]

    # Regex for IPs and domains
    ip_regex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    single_domain_regex = r'\b(?:[\w-]+\.)+({})\b'.format('|'.join(single_tlds))
    duo_domain_regex = r'\b(?:[\w-]+\.)+({})\b'.format('|'.join(duo_tlds))

    ips = re.findall(ip_regex, text)
    single_domains = re.findall(single_domain_regex, text)
    duo_domains = re.findall(duo_domain_regex, text)

    return ips, single_domains + duo_domains

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <file_to_scan> <domain_extensions_file>")
        sys.exit(1)

    file_to_scan = sys.argv[1]
    domain_extensions_file = sys.argv[2]

    extensions = read_domain_extensions(domain_extensions_file)
    text = extract_text_from_file(file_to_scan)
    ips, domains = find_domains_and_ips(text, extensions)

    print("Found IPs:", ips)
    print("Found Domains:", domains)

if __name__ == "__main__":
    main()
