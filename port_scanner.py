import socket
import threading

# Lock to prevent thread print collisions
print_lock = threading.Lock()

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((host, port))
            if result == 0:
                with print_lock:
                    print(f"[+] Port {port} is open")
    except:
        pass

def main():
    target = input("Enter target IP or hostname: ")
    print(f"Scanning target: {target}")
    for port in range(20, 1025):
        t = threading.Thread(target=scan_port, args=(target, port))
        t.start()

if __name__ == "__main__":
    main()
