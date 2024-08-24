import socket

def is_port_open(target_ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        import ipdb;ipdb.set_trace()
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        return result == 0

def scan_ports(target_ip, port_range):
    open_ports = []
    print(f"Scanning {target_ip} for open ports in range {port_range}...")
    
    for port in port_range:
        if is_port_open(target_ip, port):
            print(f"Port {port} is open on {target_ip}.")
            open_ports.append(port)
    
    return open_ports

if __name__ == "__main__":
    target_ip = input("Selecione o IP do Alvo")
    port_range = range(1, 1025)  
    
    open_ports = scan_ports(target_ip, port_range)
    
    if open_ports:
        print(f"Open ports on {target_ip}: {open_ports}")
    else:
        print(f"No open ports found on {target_ip}.")
