import subprocess

def run_nslookup(query, query_type="A", dns_server=None):
    """Runs nslookup for a given query (domain or IP) and record type."""
    command = ["nslookup"]
    
    if query_type != "A":
        command.append(f"-type={query_type}")

    command.append(query)

    if dns_server:
        command.append(dns_server)
    
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def main():
    print("\n=== NSLOOKUP TOOL ===")
    print("1. Get IP address of a domain")
    print("2. Find domain from an IP address")
    print("3. Get all DNS records (ANY)")
    print("4. Get email server records (MX)")
    print("5. Get name servers (NS)")

    choice = input("\nEnter your choice: ")

    match choice:
        case "1":
            domain = input("Enter the domain: ")
            print(run_nslookup(domain))

        case "2":
            ip_address = input("Enter the IP address: ")
            print(run_nslookup(ip_address))

        case "3":
            domain = input("Enter the domain: ")
            print(run_nslookup(domain, "ANY"))

        case "4":
            domain = input("Enter the domain: ")
            print(run_nslookup(domain, "MX"))

        case "5":
            domain = input("Enter the domain: ")
            print(run_nslookup(domain, "NS"))

        case _:
            print("Invalid choice, please try again.")

    main()

if __name__ == "__main__":
    main()
