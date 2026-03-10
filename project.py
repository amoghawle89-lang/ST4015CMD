import time
import random
from datetime import datetime


sent_packets = 0
received_packets = 0
error_packets = 0

total_data_sent = 0
total_data_received = 0

start_time = time.time()
duration = 30



packet_types = [
    "HTTP Request", "HTTP Response", "DNS Query", "DNS Response", 
    "Ping", "Pong", "File Transfer", "Streaming Data", 
    "Email", "Chat Message", "ARP Request", "ARP Reply", 
    "DHCP Discover", "DHCP Offer", "DHCP Request", "DHCP ACK"
]


log_file = open("network_log.txt", "w")
log_file.write("NETWORK ANALYZER LOG\n")
log_file.write("--------------------\n")

print("AUTOMATIC NETWORK ANALYZER")
print("Monitoring network traffic...\n")

while time.time() - start_time < duration:

    event = random.choice(["send", "receive", "error"])
    timestamp = datetime.now()

    if event == "send":
        size = random.randint(64, 1500)
        protocol = random.choice(["TCP", "UDP", "ICMP"])
        packet_type = random.choice(packet_types)

        sent_packets += 1
        total_data_sent += size

        message = f"[{timestamp}] SENT {protocol} packet ({size} bytes) - Type: {packet_type}"
        print(message)
        log_file.write(message + "\n")

    elif event == "receive":
        size = random.randint(64, 1500)
        protocol = random.choice(["TCP", "UDP", "ICMP"])
        packet_type = random.choice(packet_types)

        received_packets += 1
        total_data_received += size

        message = f"[{timestamp}] RECEIVED {protocol} packet ({size} bytes) - Type: {packet_type}"
        print(message)
        log_file.write(message + "\n")

    else:
        error_packets += 1
        message = f"[{timestamp}] PACKET TRANSMISSION ERROR"
        print(message)
        log_file.write(message + "\n")

    time.sleep(1)

elapsed_time = time.time() - start_time
if elapsed_time <= 0:
    elapsed_time = 1

send_throughput = total_data_sent / elapsed_time
receive_throughput = total_data_received / elapsed_time
packet_loss = sent_packets - received_packets

summary = f"""
----- FINAL NETWORK STATISTICS -----
Monitoring Time: {round(elapsed_time, 2)} seconds
Sent Packets: {sent_packets}
Received Packets: {received_packets}
Error Packets: {error_packets}
Packet Loss: {packet_loss}
Total Data Sent: {total_data_sent} bytes
Total Data Received: {total_data_received} bytes
Send Throughput: {round(send_throughput, 2)} bytes/sec
Receive Throughput: {round(receive_throughput, 2)} bytes/sec
"""

print(summary)
log_file.write(summary)
log_file.close()

