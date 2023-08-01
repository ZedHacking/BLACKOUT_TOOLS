import os
import requests

# ... Resto das funções ...

def expo_brechas_dados(site):
    try:
        print(f"\n\u25B6 Verificando exposição de {site} em bases de dados de brechas de dados...")
        # Código para verificar exposição de dados usando a API Have I Been Pwned

        # ...

    except Exception as e:
        print(f"\u274C Ocorreu um erro durante a verificação de exposição de dados: {e}")

    input("\nPressione Enter para continuar...")
    os.system("clear")

# Função para exibir os créditos
def creditos():
    print("\n=====================================")
    print("           \u2605 Créditos \u2605          ")
    print("=====================================")
    print("Desenvolvido por: Zed Hacking")
    print("Telegram: @Zedhacking")
    print("=====================================\n")

    input("Pressione Enter para voltar ao menu...")
    os.system("clear")

# Função para exibir o grupo do Telegram
def grupo_telegram():
    print("\n=====================================")
    print("        \u2605 Grupo do Telegram \u2605       ")
    print("=====================================")
    print("Junte-se ao nosso grupo do Telegram:")
    print("Link: https://t.me/BlackoutTeamOfc")
    print("=====================================\n")

    input("Pressione Enter para voltar ao menu...")
    os.system("clear")

# ... Resto do código ...

if __name__ == "__main__":
    while True:
        os.system("clear")
        print("=====================================")
        print("           \u2605 Menu Principal \u2605          ")
        print("=====================================")
        print("1. Consultar IP")
        print("2. Verificar portas")
        print("3. Verificar SSL/TLS")
        print("4. Verificar protocolo (UDP/TCP)")
        print("5. Verificar site online por Proxys")
        print("6. Identificar vulnerabilidades SQL")
        print("7. Consultar informações WHOIS")
        print("8. Buscar subdomínios")
        print("9. Simular teste de força bruta")
        print("10. Expo. em bases de dados de brechas de dados")
        print("11. Créditos")
        print("12. Grupo do Telegram")
        print("13. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            site = input("Digite o nome do site: ")
            consultar_ip(site)
        elif opcao == "2":
            site = input("Digite o nome do site: ")
            verificar_portas(site)
        elif opcao == "3":
            site = input("Digite o nome do site: ")
            verificar_seguranca_ssl(site)
        elif opcao == "4":
            site = input("Digite o nome do site: ")
            verificar_protocolo(site)
        elif opcao == "5":
            site = input("Digite o nome do site: ")
            verificar_site_proxy(site)
        elif opcao == "6":
            site = input("Digite o nome do site: ")
            identificar_vulnerabilidades_sql(site)
        elif opcao == "7":
            site = input("Digite o nome do site: ")
            consultar_whois(site)
        elif opcao == "8":
            site = input("Digite o nome do site: ")
            buscar_subdominios(site)
        elif opcao == "9":
            site = input("Digite o nome do site: ")
            usuario = input("Digite o usuário alvo: ")
            simular_teste_forca_bruta(site, usuario)
        elif opcao == "10":
            site = input("Digite o nome do site: ")
            expo_brechas_dados(site)
        elif opcao == "11":
            creditos()
        elif opcao == "12":
            grupo_telegram()
        elif opcao == "13":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Digite novamente.")
            
