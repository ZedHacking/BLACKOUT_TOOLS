import socket
import os

def consultar_ip(site):
    try:
        ip = socket.gethostbyname(site)
        print(f"\n\u25B6 O IP do site {site} é: {ip}")
    except socket.gaierror:
        print(f"\n\u274C Não foi possível encontrar o IP do site {site}.")
    input("\nPressione Enter para continuar...")
    os.system("clear")

def verificar_portas(site):
    try:
        print(f"\n\u25B6 Verificando as 5 primeiras portas abertas do site {site}:")
        for porta in range(1, 6):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            resultado = sock.connect_ex((site, porta))
            if resultado == 0:
                print(f"\u2713 A porta {porta} está aberta.")
            else:
                print(f"\u2717 A porta {porta} está fechada.")
            sock.close()
    except socket.gaierror:
        print(f"\n\u274C Não foi possível verificar as portas do site {site}.")
    input("\nPressione Enter para continuar...")
    os.system("clear")

def consultar_protocolo(site):
    try:
        _, _, protocolo = socket.getaddrinfo(site, None)[0]
        if protocolo == socket.SOCK_STREAM:
            print(f"\n\u25B6 O site {site} utiliza o protocolo TCP.")
        elif protocolo == socket.SOCK_DGRAM:
            print(f"\n\u25B6 O site {site} utiliza o protocolo UDP.")
    except socket.gaierror:
        print(f"\n\u274C Não foi possível consultar o protocolo do site {site}.")
    input("\nPressione Enter para continuar...")
    os.system("clear")

def creditos():
    os.system("clear")
    print("=====================================")
    print("            \u2705 Créditos \u2705           ")
    print("=====================================")
    print("\nZed Hacking - Especialista em Segurança Digital")
    input("\nPressione Enter para voltar ao menu...")
    os.system("clear")

if __name__ == "__main__":
    while True:
        os.system("clear")
        print("=====================================")
        print("           \u2605 Menu Principal \u2605          ")
        print("=====================================")
        print("1. Consultar IP de um site")
        print("2. Verificar 5 portas abertas de um site")
        print("3. Consultar se o site é UDP ou TCP")
        print("4. Créditos")
        print("5. Sair")

        opcao = input("\nDigite o número da opção desejada: ")

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
            creditos()
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Digite novamente.")
            
