#receiver
import socket

# Create UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 12345))  # Bind to any interface, port 12345

print("Server (Receiver) started.")
print("Share this IP and port with sender (Client):")
print("Public IP should be shared if behind NAT.")

while True:
    data, addr = s.recvfrom(1024)
    print(f"Received from {addr}: {data.decode()}")

    msg = input("Reply message: ")
    s.sendto(msg.encode(), addr)
