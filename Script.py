import socket

# Obtém o nome do site
site_name = input("Digite o nome do site: ")

# Obtém o IP do site
site_ip = socket.gethostbyname(site_name)

# Verifica as portas abertas no site
for port in range(1, 65535):
    try:
        socket.create_connection((site_ip, port), 2)
        print(f"A porta {port} está aberta.")
    except socket.error:
        pass

# Verifica se o site usa UDP ou TCP
if socket.getservbyport(80, "tcp") == site_ip:
    print(f"O site usa TCP.")
else:
    print(f"O site usa UDP.")
