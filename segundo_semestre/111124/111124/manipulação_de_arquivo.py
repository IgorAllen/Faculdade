# manipulação de arquivos
# exemplos: .txt e .csv

# w (write): Abre um arquivo para escrita {subtitui o conteúdo que já existe no arquivo};

# a (append): Também modo de escrita, mas adiciona ao final do arquivo;

# r (read): Abre um arquivo no modo para leitura;

arquivo = open("nome.extensao", "modo")

arquivo.close #sempre que terminar de usar o arquivo, feche ele para o programa funcionar;

arq = open("notas.txt", "r")

#Lê uma linha por vez até encontrar o final do arquivo
conteudo = '--'
while conteudo!="":
conteudo = arq.readline() #lê uma linha por vez
print(conteudo)

#Lê e guarda cada linha em uma lista
conteudo = arq.readlines()
print(conteudo)#Veja que o \n fica na lista

###Nesse momento a posição corrente é o final do arquivo###

###E se eu quiser ler novamente??###

#Posiciona no início do arquivo
arq.seek(0)

#Lê tudo em uma String única
conteudo = arq.read()
print(conteudo)

#divide o conteúdo lido em uma lista
lista = conteudo.split("\n")
print(lista)

#imprime cada elemento da lista em uma linha
for linha in lista:
print(linha)

###Preciso ler só a partir da segunda linha, para desconsiderar o cabeçalho###

#posiciona no início da segunda linha
tamPri = len(arq.readline())
arq.seek(tamPri+1,0) #argumento 1: deslocamento em bytes – argumento 2: desloca a partir da posição 0
conteudo = arq.read()

#imprime cada elemento da lista em uma linha, a partir da segunda linha
conteudo = arq.read()
lista = conteudo.split("\n")
print(lista)

for linha in lista:
print(linha)

###E se eu quiser separar o nome das notas para calcular as médias?

#Separa os dados de cada elemento (linha/String) da lista
for linha in lista:
dados = linha.split(",")
nome = dados[0]
n1 = float(dados[1])
n2 = float(dados[2])
print("Média de", nome, "=", (n1+n2)/2)
arq.close()

###E se eu quiser guardar as médias em um novo arquivo de texto###
arq2 = open("medias.txt","w")
arq2.write("nome,média\n")
for linha in lista:
dados = linha.split(",")
nome = dados[0]
n1 = float(dados[1])
n2 = float(dados[2])
arq2.write(nome+','+str((n1+n2)/2)+"\n")

arq2.close()
