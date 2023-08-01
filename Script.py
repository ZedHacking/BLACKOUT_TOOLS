import socket

# Obtém o nome do site
site_name = input("Digite o nome do site: ")

# Obtém o IP do site
site_ip = socket.gethostbyname(site_name)

# Verifica as portas abertas no site
open_ports = []
for port in range(1, 65535):
    try:
        socket.create_connection((site_ip, port), 2)
        open_ports.append(port)
    except socket.error:
        pass

# Exibe as 5 primeiras portas abertas
if len(open_ports) <= 5:
    print("Portas abertas:", open_ports)
else:
    print("Portas abertas:", open_ports[:5])

# Identifica se o site usa TCP ou UDP
if socket.getservbyport(80, "tcp") == site_ip:
    print(f"O site usa TCP.")
else:
    print(f"O site usa UDP.")
