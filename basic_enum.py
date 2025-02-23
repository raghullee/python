import socket
import ipaddress

def check_port(ip, port):
    """Check if a specific port on an IP address is open."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            return result == 0  # return True if the port is open, False otherwise
    except socket.error:
        return False

def enumerate_ports(ip, start_port, end_port):
    """Enumerate open ports on the given IP address."""
    print(f"Scanning IP {ip} for open ports from {start_port} to {end_port}...")
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        if check_port(ip, port):
            print(f"Port {port} is open!")
            open_ports.append(port)
        else:
            print(f"Port {port} is closed.")
    
    if open_ports:
        print(f"\nOpen ports found: {open_ports}")
    else:
        print("\nNo open ports found.")

def main():
    ip_input = input("Enter IP address to scan (e.g., 192.168.1.1): ")
    try:
        # Validate IP address format
        ipaddress.ip_address(ip_input)
    except ValueError:
        print("Invalid IP address format!")
        return
    
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))
    
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Invalid port range. Ports should be between 1 and 65535, and the start port should not be greater than the end port.")
        return
    
    enumerate_ports(ip_input, start_port, end_port)

if __name__ == "__main__":
    main()
