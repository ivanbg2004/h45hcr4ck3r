# Hash Cracker by OD&H

## Description
Hash Cracker is a lightweight Python tool developed by **OD&H** to crack hashed passwords using a dictionary attack. It supports multiple hashing algorithms like MD5, SHA1, SHA256, and more.

## Features
- Supports various hash algorithms (MD5, SHA1, SHA256, etc.)
- Uses a wordlist to attempt hash cracking
- Simple and efficient command-line interface

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/ivanbg2004/h45hcr4ck3r.git
   cd h45hcr4ck3r
   ```
2. Install Python (if not already installed):
   ```sh
   sudo apt install python3  # Linux
   brew install python3      # macOS
   ```

## Usage
Run the script and provide the necessary inputs:
```sh
python3 h45hcr4ck3r.py
```
Then enter:
- The hash value to crack
- The hash type (md5, sha1, sha256, etc.)
- Path to the wordlist file

## Example
```sh
Enter the hash: 5d41402abc4b2a76b9719d911017c592
Enter the hash type (md5, sha1, sha256, etc.): md5
Enter path to wordlist: rockyou.txt
[+] Password found: hello
```
Do you need a rockyou.txt? [Check this one!](https://github.com/ivanbg2004/zip-password-cracker/blob/main/wordlists/oblivion_wordlist.txt) 

## License
This tool is for educational and ethical hacking purposes only. Use it responsibly.

## Credits
Developed by **OD&H**.

