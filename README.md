# didactic-couscous


## Overview

This Python script is designed to assist cybersecurity professionals and researchers in extracting domain names and IP addresses from various file types. It can process plain text files, as well as attempt to extract readable text from encrypted or compiled files. The script is especially useful for analyzing potentially malicious files, phishing emails, or network logs to identify domain-based threats and suspicious IP addresses.

## Features

- **Domain Extraction**: Identifies domain names in files, supporting both standard and duo-linked top-level domains (e.g., `.com`, `.co.uk`).
- **IP Address Detection**: Extracts IPv4 addresses.
- **Customizable TLDs**: Users can specify a list of top-level domains to scan for, enhancing the script's adaptability to different investigative needs.
- **File Type Versatility**: Designed to read plain text and extract strings from various file formats, including encrypted or compiled files (with limitations).

## Installation

No special installation is required. Ensure you have Python 3.x installed on your system.

## Usage

1. **Prepare the Domain Extensions File**: Create a text file listing the top-level domains (TLDs) you want to scan for. Include both standard and duo-linked TLDs, each on a new line. Example file contents:

   ```
   com
   net
   org
   co.uk
   gov.au
   ```

2. **Run the Script**: Execute the script with two arguments: the path to the file to be scanned and the path to the domain extensions file.

   ```bash
   python domain_ip_extractor.py <file_to_scan> <domain_extensions_file>
   ```

## Example

```bash
python domain_ip_extractor.py suspicious_email.txt tlds.txt
```

## Output

The script outputs lists of found IP addresses and domain names directly to the console.

## Limitations

- The ability to extract text from encrypted or compiled files depends on the nature of the encryption or compilation. This script may not work on strongly encrypted or obfuscated files.
- The script uses regular expressions for pattern matching, which might not cover all possible variations of domain names and IP addresses.

## Contribution

Contributions to enhance the script's capabilities, especially in extracting text from more complex file formats, are welcome.

## Disclaimer

This tool is intended for cybersecurity research and investigation purposes only. Users are responsible for complying with applicable laws and regulations.
