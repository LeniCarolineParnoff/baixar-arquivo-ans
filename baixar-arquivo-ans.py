import requests

def baixar_arquivo (url, nome_do_arquivo):
    #faz requisicao ao servidor
    print('fazendo a requisicao ao servidor')

    url_arquivo = url + nome_do_arquivo
    #concatenando o site da ANS com o nome da versão mais recente do arquivo

    resposta_http = requests.get(url_arquivo)     #fazendo uma requisição http get para pegar o arquivo
    print('código de resposta http: ' + str(resposta_http.status_code)) #buscando a resposta http do servidor  
    
    if resposta_http.status_code == requests.codes.OK: #ok = 200
        with open(nome_do_arquivo, 'wb') as novo_arquivo:
                #modo  de  abertura: 'wb', porque vai ser aberto para escrita dos bytes.

            novo_arquivo.write(resposta_http.content)
                #posso escrever neste novo_arquivo o que tiver como conteudo na nossa resposta.       
    else:
        print('Arquivo não encontrado: ' + nome_do_arquivo)
        print('código de resposta http: ' + str(resposta_http.status_code)) #Para poder concatenar com outra string, foi realizada a conversao de um tipo int para string

print('Iniciando o programa.')

baixar_arquivo(
    'https://www.gov.br/ans/pt-br/arquivos/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-tiss/padrao-tiss/', 
    'padrao-tiss_componente-organizacional_202111.pdf')
