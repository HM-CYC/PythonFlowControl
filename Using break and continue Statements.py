#Write a Python program that iterates through a list of IP addresses and identifies the first private
# IP address encountered.
ip_addresses = ["192.168.1.1", "203.0.113.42", "172.16.0.1", "10.0.0.1"]
for ip in ip_addresses:
    if ip.startswith("192.168.") or ip.startswith("172.16.") or ip.startswith("10."):
        print("Private IP address found:", ip)
        break
    else:
        continue


