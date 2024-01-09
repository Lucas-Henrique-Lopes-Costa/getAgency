from bs4 import BeautifulSoup
import re

def extrair_e_criar_links(arquivo_html, arquivo_saida):
    try:
        # Abrir e ler o arquivo HTML
        with open(arquivo_html, 'r', encoding='utf-8') as file:
            conteudo = file.read()

        # Parse do conteúdo HTML
        soup = BeautifulSoup(conteudo, 'html.parser')

        # Encontrar todos os links
        links = soup.find_all('a', href=True)

        # Filtrar os links do Facebook e extrair o nome
        nomes = set()
        for link in links:
            match = re.match(r'https://facebook.com/([^/?#]+)', link['href'])
            if match:
                nomes.add(match.group(1))

        # Escrever os nomes e os novos links em um arquivo de texto
        with open(arquivo_saida, 'w', encoding='utf-8') as file:
            for nome in nomes:
                file.write(f"O nome capturado foi esse: {nome}\n")
                file.write(f"https://facebook.com/{nome}\n")
                file.write(f"https://www.instagram.com/{nome}\n\n")

        print(
            f"Links extraídos e criados com sucesso, salvos em '{arquivo_saida}'")

    except Exception as e:
        print("Ocorreu um erro:", e)


# Exemplo de uso
arquivo_html = "index.html"  # Substitua pelo nome do arquivo HTML
arquivo_saida = "links_gerados.txt"  # Nome do arquivo de texto de saída
extrair_e_criar_links(arquivo_html, arquivo_saida)
