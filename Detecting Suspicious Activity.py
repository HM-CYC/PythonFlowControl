#Write a Python program that monitors network traffic and detects suspicious activity using nested
# if statements to evaluate multiple conditions.

source_ip = "192.168.1.100"
destination_ip = "203.0.113.42"
protocol = "TCP"
port = 20

if source_ip == destination_ip:
    print("Suspicious activity detected: Source and destination IP addresses are the same.")
else:
    if protocol == "TCP":
        if port == 22:
            print("Suspicious activity detected: TCP traffic on port 22 (SSH).")
        elif port == 3389:
            print("Suspicious activity detected: TCP traffic on port 3389 (RDP).")
        else:
            print("No suspicious activity detected.")
    else:
        print("No suspicious activity detected.")

