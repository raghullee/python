from scapy.all import ICMP, IP, sr1

def send_icmp_requests(target_ip, count=4):
    for i in range(count):
        print(f"Sending ICMP request {i+1} to {target_ip}...")
        
       
        ip_packet = IP(dst=target_ip)
        
      
        icmp_packet = ICMP()

        
        packet = ip_packet/icmp_packet

        
        response = sr1(packet, timeout=1, verbose=False)

        if response:
            print(f"Received ICMP response from {target_ip}:")
            print(response.summary())
        else:
            print(f"No response from {target_ip}")

        print("-" * 40)  


if __name__ == "__main__":
    target_ip = "8.8.8.8"  # Replace with the target IP address
    send_icmp_requests(target_ip, count=400)  # Adjust 'count' as needed
