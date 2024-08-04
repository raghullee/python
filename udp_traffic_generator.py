from scapy.all import Ether, IP, UDP, Raw, sendp
import time

# Define the destination IP address, MAC address, and port
dst_ip = "172.16.31.148"  # Replace with your target IP address
dst_mac = "08:00:27:00:26:00"  # Replace with your target MAC address
dst_port = 123  # Replace with your target port

# Create a payload of 1500 bytes
payload = b"A" * 1500

# Build the packet
packet = Ether(dst=dst_mac) / IP(dst=dst_ip, flags="DF") / UDP(dport=dst_port, sport=54321) / Raw(load=payload)

# Set the duration for sending packets
duration = 60  # seconds
end_time = time.time() + duration

# Send packets for the specified duration
while time.time() < end_time:
    sendp(packet)

print("Finished sending packets")



