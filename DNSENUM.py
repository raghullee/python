# python3 dnsenum.py google.com ns ( insteed of google.com give any domain whatever you want.


import argparse
import dns.resolver

def ns_lookup(domain):
    try:
        # Perform NS record lookup
        result = dns.resolver.resolve(domain, 'NS')
        # Print the nameservers
        print(f"Name Servers for {domain}:")
        for server in result:
            print(server.to_text())
    except dns.resolver.NoAnswer:
        print("No NS record found.")
    except dns.resolver.NXDOMAIN:
        print("Domain does not exist.")
    except dns.exception.Timeout:
        print("DNS query timed out.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="DNS Enumeration Tool")
    parser.add_argument("domain", help="Domain name to query")
    parser.add_argument("record_type", help="Type of DNS record to query (e.g., ns, a, mx, etc.)")
    
    # Parse arguments
    args = parser.parse_args()

    # Check for NS query
    if args.record_type.lower() == "ns":
        ns_lookup(args.domain)
    else:
        print(f"Record type '{args.record_type}' not supported in this script.")

if __name__ == "__main__":
    main()
