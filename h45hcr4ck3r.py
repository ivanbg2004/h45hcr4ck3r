import hashlib

def crack_hash(hash_value, hash_type, wordlist):
    try:
        with open(wordlist, "r", encoding="utf-8", errors="ignore") as file:
            for password in file:
                password = password.strip()
                hashed_attempt = hashlib.new(hash_type, password.encode()).hexdigest()
                if hashed_attempt == hash_value:
                    print(f"[+] Password found: {password}")
                    return password
        print("[-] Password not found in wordlist.")
    except FileNotFoundError:
        print("[!] Wordlist file not found.")
    except Exception as e:
        print(f"[!] Error: {e}")
    return None

if __name__ == "__main__":
    hash_value = input("Enter the hash: ").strip()
    hash_type = input("Enter the hash type (md5, sha1, sha256, etc.): ").strip()
    wordlist = input("Enter path to wordlist: ").strip()
    
    crack_hash(hash_value, hash_type, wordlist)
