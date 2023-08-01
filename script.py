import os
import requests
import socket
import whois
from bs4 import BeautifulSoup

# Função para consultar o IP de um site
def consultar_ip(site):
    try:
        print(f"\nConsultando o IP de {site}...")
        ip = socket.gethostbyname(site)
        print(f"O IP de {site} é: {ip}")
    except socket.gaierror:
        print(f"Não foi possível encontrar o IP de {site}")

    input("\nPressione Enter para continuar...")
    os.system("clear")

# Função para verificar as portas abertas de um site
def verificar_portas(site):
    try:
        print(f"\nVerificando as 5 primeiras portas abertas de {site}...")
        count_portas_abertas = 0  # Variável para contar as portas abertas

        for porta in range(1, 6):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            resultado = sock.connect_ex((site, porta))
            if resultado == 0:
                print(f"A porta {porta} está aberta.")
                count_portas_abertas += 1
                if count_portas_abertas >= 2:  # Para aqui se encontrar pelo menos 2 portas abertas
                    break
            else:
                print(f"A porta {porta} está fechada.")

        if count_portas_abertas == 0:
            print("Nenhuma porta aberta encontrada.")
        elif count_portas_abertas == 1:
            print("Apenas uma porta aberta encontrada.")
        else:
            print(f"Total de {count_portas_abertas} portas abertas encontradas.")

    except socket.gaierror:
        print(f"Não foi possível verificar as portas de {site}")

    input("\nPressione Enter para continuar...")
    os.system("clear")

# Função para verificar se o site possui SSL/TLS habilitado
def verificar_seguranca_ssl(site):
    try:
        print(f"\nVerificando se o site {site} possui SSL/TLS habilitado...")
        resposta = requests.get(f"https://{site}", verify=True)
        if resposta.status_code == 200:
            print(f"{site} possui SSL/TLS habilitado.")
        else:
            print(f"{site} não possui SSL/TLS habilitado.")

    except requests.exceptions.SSLError:
        print(f"{site} não possui SSL/TLS habilitado.")

    except requests.exceptions.RequestException:
        print(f"Não foi possível verificar a segurança de {site}")

    input("\nPressione Enter para continuar...")
    os.system("clear")

# Função para verificar se o site está online
def verificar_site_online(site):
    try:
        print(f"\nVerificando se {site} está online...")
        resposta = requests.get(f"https://{site}", timeout=5)
        if resposta.status_code == 200:
            print(f"{site} está online.")
        else:
            print(f"{site} está fora do ar.")

    except requests.exceptions.RequestException:
        print(f"{site} está fora do ar.")

    input("\nPressione Enter para continuar...")
    os.system("clear")

# Função para identificar vulnerabilidades SQL em um site
def identificar_vulnerabilidades_sql(site):
    try:
        print(f"\nIdentificando vulnerabilidades SQL em {site}...")
        # Código para identificar vulnerabilidades SQL em um site
        # Exemplo simples:
        parametros = {"username": "admin' OR '1'='1", "password": "123"}
        resposta = requests.post(f"https://{site}/login", data=parametros)
        if "Usuário ou senha incorretos" not in resposta.text:
            print("Possível vulnerabilidade SQL identificada.")
        else:
            print("Nenhuma vulnerabilidade SQL identificada.")

    except Exception as e:
        print(f"Ocorreu um erro durante a identificação de vulnerabilidades SQL: {e}")

    input("\nPressione Enter para continuar...")
    os.system("clear")

# Função para consultar informações WHOIS de um site
def consultar_whois(site):
    try:
        print(f"\nConsultando informações WHOIS de {site}...")
        info_whois = whois.whois(site)
        print(info_whois)

    except Exception as e:
        print(f"Ocorreu um erro durante a consulta WHOIS: {e}")

    input("\nPressione Enter para continuar...")
    os.system("clear")

# Função para simular teste de força bruta em formulários de login
def simular_teste_forca_bruta(site, usuario):
    try:
        print(f"\nSimulando teste de força bruta no formulário de login de {site}...")
        # Código para simular teste de força bruta em formulários de login
        # Exemplo simples:
        for senha in ["123456", "password", "1234", "qwerty"]:
            parametros = {"username": usuario, "password": senha}
            resposta = requests.post(f"https://{site}/login", data=parametros)
            if "Usuário ou senha incorretos" not in resposta.text:
                print(f"Senha encontrada: {senha}")
                break
        else:
            print("Nenhuma senha encontrada.")

    except Exception as e:
        print(f"Ocorreu um erro durante o teste de força bruta: {e}")

    input("\nPressione Enter para continuar...")
    os.system("clear")

# Função para verificar exposição em bases de dados de brechas
def verificar_exposicao_brechas_dados(site):
    try:
        print(f"\nVerificando se {site} está listado em bases de dados públicas de brechas de dados...")
        # Código para verificar a exposição de dados em bases públicas
        # Exemplo simples:
        resposta = requests.get(f"https://breachdatabase.com/search?q={site}")
        if "Nenhum resultado encontrado" not in resposta.text:
            print(f"{site} está listado em bases de dados de brechas de dados.")
        else:
            print(f"{site} não está listado em bases de dados de brechas de dados.")

    except Exception as e:
        print(f"Ocorreu um erro durante a verificação de exposição de dados: {e}")

    input("\nPressione Enter para continuar...")
    os.system("clear")

# Função para consultar subdomínios de um site
def consultar_subdominios(site):
    try:
        print(f"\nConsultando subdomínios de {site}...")
        resposta = requests.get(f"https://www.pagesinventory.com/search/?s={site}&filter_domain=&filter_ip=&offset=1")
        soup = BeautifulSoup(resposta.content, "html.parser")
        subdominios = set()

        for resultado in soup.find_all("div", class_="domain"):
            subdominio = resultado.text.strip()
            subdominios.add(subdominio)

        if subdominios:
            print("Subdomínios encontrados:")
            for subdominio in subdominios:
                print(subdominio)
        else:
            print("Nenhum subdomínio encontrado.")

    except Exception as e:
        print(f"Ocorreu um erro durante a consulta de subdomínios: {e}")

    input("\nPressione Enter para continuar...")
    os.system("clear")

import socket

# Função para verificar se o site utiliza UDP ou TCP
def verificar_udp_tcp(site):
    try:
        print(f"\nVerificando se o site {site} utiliza UDP ou TCP...")
        
        # Verificando o protocolo utilizado pelas portas 80 (HTTP) e 443 (HTTPS)
        http_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        http_socket.settimeout(2)
        http_resultado = http_socket.connect_ex((site, 80))

        https_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        https_socket.settimeout(2)
        https_resultado = https_socket.connect_ex((site, 443))

        if http_resultado == 0 and https_resultado == 0:
            print(f"O site {site} pode utilizar tanto UDP quanto TCP.")
        elif http_resultado == 0:
            print(f"O site {site} utiliza o protocolo TCP (HTTP).")
        elif https_resultado == 0:
            print(f"O site {site} utiliza o protocolo TCP (HTTPS).")
        else:
            print(f"Não foi possível determinar se o site {site} utiliza UDP ou TCP.")

    except Exception as e:
        print(f"Ocorreu um erro durante a verificação de UDP/TCP: {e}")

    input("\nPressione Enter para continuar...")
    os.system("clear")

# Função para encontrar painéis de administração em um site
def encontrar_painel_administracao(site):
    try:
        print(f"\nProcurando painel de administração em {site}...")

        # Lista com possíveis URLs de painéis de administração
        paineis_administracao = [
            "admin", "adm", "login", "wp-admin", "administrator",
            "admin/login", "admin_area", "admin-login", "adminlogin",
            "panel-administracion", "admin1", "admin2", "admin3",
        ]

        for painel in paineis_administracao:
            url = f"https://{site}/{painel}/"
            resposta = requests.get(url)

            if resposta.status_code == 200:
                print(f"Painel de administração encontrado: {url}")
                break
        else:
            print("Nenhum painel de administração encontrado.")

    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro durante a busca por painéis de administração: {e}")

    input("\nPressione Enter para continuar...")
    os.system("clear")

# Função para exibir o grupo do Telegram
def grupo_telegram():
    print("\n=====================================")
    print("        ★ Grupo do Telegram ★       ")
    print("=====================================")
    print("Junte-se ao nosso grupo do Telegram:")
    print("Link: https://t.me/BlackoutTeamOfc")
    print("=====================================\n")

    input("Pressione Enter para voltar ao menu...")
    os.system("clear")

# Função para exibir os créditos
def creditos():
    print("\n=====================================")
    print("           ★ Créditos ★          ")
    print("=====================================")
    print("Desenvolvido por: Zed Hacking")
    print("Telegram: @ZedHacking")
    print("=====================================\n")

    input("Pressione Enter para voltar ao menu...")
    os.system("clear")

# Função para exibir o menu
def exibir_menu():
    while True:
        os.system("clear")
        print("=====================================")
        print("     ★ BLACKOUT SECURITY ★          ")
        print("=====================================")
        print("1. Consultar IP de um site")
        print("2. Verificar portas abertas de um site")
        print("3. Verificar segurança SSL/TLS do site")
        print("4. Verificar se o site está online")
        print("5. Identificar vulnerabilidades SQL em um site")
        print("6. Consultar informações WHOIS de um site")
        print("7. Verificar exposição em bases de dados de brechas")
        print("8. Consultar subdomínios de um site")
        print("9. Verificar se o site utiliza UDP ou TCP")
        print("10. Grupo do Telegram")
        print("11. Créditos")
        print("12. Encontrar painel de administração de um site")
        print("0. Sair")
        print("=====================================")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            site = input("Digite o site para consultar o IP: ")
            consultar_ip(site)

        elif opcao == "2":
            site = input("Digite o site para verificar as portas abertas: ")
            verificar_portas(site)

        elif opcao == "3":
            site = input("Digite o site para verificar a segurança SSL/TLS: ")
            verificar_seguranca_ssl(site)

        elif opcao == "4":
            site = input("Digite o site para verificar se está online: ")
            verificar_site_online(site)

        elif opcao == "5":
            site = input("Digite o site para identificar vulnerabilidades SQL: ")
            identificar_vulnerabilidades_sql(site)

        elif opcao == "6":
            site = input("Digite o site para consultar informações WHOIS: ")
            consultar_whois(site)

        elif opcao == "7":
            site = input("Digite o site para verificar exposição em bases de dados de brechas: ")
            verificar_exposicao_brechas_dados(site)

        elif opcao == "8":
            site = input("Digite o site para consultar subdomínios: ")
            consultar_subdominios(site)

        elif opcao == "9":
            site = input("Digite o site para verificar se utiliza UDP ou TCP: ")
            verificar_udp_tcp(site)

        elif opcao == "10":
            grupo_telegram()

        elif opcao == "11":
            creditos()

        elif opcao == "12":
            site = input("Digite o site para encontrar o painel de administração: ")
            encontrar_painel_administracao(site)

        elif opcao == "0":
            print("Saindo do menu...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    exibir_menu()
    
