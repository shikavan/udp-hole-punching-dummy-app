#sender:
import socket 

# Create UDP socket
c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c.bind(("", 0))  # Bind to random port assigned by OS

# Enter receiver (server) public IP and port manually
receiver_ip = input("Enter receiver IP: ")
receiver_port = int(input("Enter receiver port: "))
receiver = (receiver_ip, receiver_port)

# Send initial hole punch packets
for i in range(5):
    c.sendto(f"Punch {i}".encode(), receiver)

# Then send actual message
while True:
    msg = input("Your message: ")
    c.sendto(msg.encode(), receiver)
    data, addr = c.recvfrom(1024)
    print(f"Received from {addr}: {data.decode()}")
