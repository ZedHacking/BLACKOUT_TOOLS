import socket
import os
import requests
import subprocess

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
        print(f"\n\u25B6 Procurando por portas abertas no site {site}...")
        for porta in range(1, 65536):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            resultado = sock.connect_ex((site, porta))
            if resultado == 0:
                print(f"\u2713 A porta {porta} está aberta.")
                break
            sock.close()
        else:
            print(f"\u274C Nenhuma porta aberta encontrada no site {site}.")
    except socket.gaierror:
        print(f"\n\u274C Não foi possível verificar as portas do site {site}.")
    input("\nPressione Enter para continuar...")
    os.system("clear")

def consultar_protocolo(site):
    try:
        protocolo = socket.getaddrinfo(site, None)
        if protocolo:
            protocolo = protocolo[0][1]
            if protocolo == socket.SOCK_STREAM:
                print(f"\n\u25B6 O site {site} utiliza o protocolo TCP.")
            elif protocolo == socket.SOCK_DGRAM:
                print(f"\n\u25B6 O site {site} utiliza o protocolo UDP.")
        else:
            print(f"\n\u274C Não foi possível consultar o protocolo do site {site}.")
    except socket.gaierror:
        print(f"\n\u274C Não foi possível consultar o protocolo do site {site}.")
    input("\nPressione Enter para continuar...")
    os.system("clear")

def verificar_site_proxy(site):
    proxies = {
        "http": "http://proxy.example.com:8080",
        "https": "https://proxy.example.com:8080"
    }
    try:
        response = requests.get(f"http://{site}", proxies=proxies, timeout=10)
        if response.status_code == 200:
            print(f"\n\u2713 O site {site} está online.")
        else:
            print(f"\u274C O site {site} está fora do ar.")
    except requests.exceptions.RequestException:
        print(f"\u274C O site {site} está fora do ar.")
    input("\nPressione Enter para continuar...")
    os.system("clear")

def identificar_vulnerabilidades_sql(site):
    try:
        subprocess.run(["sqlmap", "-u", f"http://{site}"])
    except FileNotFoundError:
        print("\u274C O sqlmap não está instalado ou não está disponível no sistema.")
    input("\nPressione Enter para continuar...")
    os.system("clear")

def creditos():
    os.system("clear")
    print("=====================================")
    print("            \u2705 Créditos \u2705           ")
    print("=====================================")
    print("\nZed Hacking - Kiba não putinha")
    input("\nPressione Enter para voltar ao menu...")
    os.system("clear")

def grupo_telegram():
    os.system("clear")
    print("=====================================")
    print("        \u2605 Grupo do Telegram \u2605      ")
    print("=====================================")
    print("\nJunte-se ao nosso grupo do Telegram para receber atualizações, dicas e discussões sobre segurança digital e hacking:")
    print("Link do grupo: https://t.me/BlackoutTeamOfc")
    input("\nPressione Enter para voltar ao menu...")
    os.system("clear")

if __name__ == "__main__":
    while True:
        os.system("clear")
        print("=====================================")
        print("           \u2605 Menu Principal \u2605          ")
        print("=====================================")
        print("1. Consultar IP de um site")
        print("2. Verificar portas abertas de um site")
        print("3. Consultar se o site é UDP ou TCP")
        print("4. Verificar se o site está fora do ar por meio de Proxys")
        print("5. Identificar vulnerabilidades SQL")
        print("6. Créditos")
        print("7. Grupo do Telegram")
        print("8. Sair")

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
            site = input("Digite o nome do site: ")
            verificar_site_proxy(site)
        elif opcao == "5":
            site = input("Digite o nome do site: ")
            identificar_vulnerabilidades_sql(site)
        elif opcao == "6":
            creditos()
        elif opcao == "7":
            grupo_telegram()
        elif opcao == "8":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Digite novamente.")
            
