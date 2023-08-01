import socket

def consultar_ip(site):
    try:
        ip = socket.gethostbyname(site)
        print(f"O IP do site {site} é: {ip}")
    except socket.gaierror:
        print(f"Não foi possível encontrar o IP do site {site}.")

def verificar_portas(site):
    try:
        for porta in range(1, 6):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            resultado = sock.connect_ex((site, porta))
            if resultado == 0:
                print(f"A porta {porta} do site {site} está aberta.")
            else:
                print(f"A porta {porta} do site {site} está fechada.")
            sock.close()
    except socket.gaierror:
        print(f"Não foi possível verificar as portas do site {site}.")

def consultar_protocolo(site):
    try:
        _, _, protocolo = socket.getaddrinfo(site, None)[0]
        if protocolo == socket.SOCK_STREAM:
            print(f"O site {site} utiliza o protocolo TCP.")
        elif protocolo == socket.SOCK_DGRAM:
            print(f"O site {site} utiliza o protocolo UDP.")
    except socket.gaierror:
        print(f"Não foi possível consultar o protocolo do site {site}.")

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Consultar IP de um site")
        print("2. Verificar 5 portas abertas de um site")
        print("3. Consultar se o site é UDP ou TCP")
        print("4. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            site = input("Digite o nome do site: ")
            consultar_ip(site)
        elif opcao == "2":
            site = input("Digite o nome do site: ")
            verificar_portas(site)
        elif opcao == "3":
            site = input("Digite o nome do site: ")
            consultar_protocolo(site)
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Digite novamente.")
