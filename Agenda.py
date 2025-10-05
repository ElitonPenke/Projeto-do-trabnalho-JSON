#importa a biblioteca json para manipular arquivo   
import json

#associa a variavel ARQUIVO ao arquivo json que vai se chamar contatos
ARQUIVO = 'Minha agenda.json'

#função para puxar o que tem dentro do arquivo json e tranformar em um dicionario py para manipular
def carregar_contatos():
    try:
        with open(ARQUIVO, 'r') as Arquivo_temporario:
            return json.load(Arquivo_temporario)
    except:
        return []  

#função para pegar a variavel em py e sobrescrever no arquivo JSON

def salvar_contatos(contatos):   # PRECISA DE PARAMETRO PARA A FUNÇÃO SABER O QUE É PARA GUARDAR 
    with open(ARQUIVO, 'w') as Arquivo_temporario:
        json.dump(contatos, Arquivo_temporario, indent=4)


#é feito uma class para ser feita de molde os cadasdtro no arquivo JSON
class Agenda:
    def __init__(self): #construtor da class
        self.contatos = carregar_contatos()  #aqui ele associa a variavel contatos(lista) a um atributo da class
    
    #essa função vai adicionar novo contato na variavel py
    def adicionar_contato(self):
        nome = input('NOME: ')
        telefone = input('TELEFONE: ')
        email = input('EMAIL: ')
        endereco = input('ENDEREÇO: ')
        aniversario = input('ANIVERSÁRIO: ')
        id = len(self.contatos) + 1  #aqui é toda vez é criado uym novo id com base nos contatos ja salvos
        
        #uma variavel local para armazenar tudo de uma vez o que vai ser armazenado
        novo = {
            'id': id,
            'nome': nome.title(),
            'telefone': telefone,
            'email': email.lower(),
            'endereco': endereco,
            'aniversario': aniversario
        }
        #aqui ele vai adicionar a varivel (novo) a lista (contatos)
        self.contatos.append(novo)

        #aqui ele chama a def salvar_contatos para colocar a varial em py(a contatos) para dentro do arquivo JSON
        salvar_contatos(self.contatos)
        print('\nCONTATO ADICIONADO COM SUCESSO!\n')

    #def o qual vai retornar todos os contatos
    def listar_contatos(self):
        for contato in self.contatos:  # um laço de vai buscar cada contato na lista cointatos e vai trazer os itens abaixo
            print(f"\nID: {contato['id']}")  #ele diz de onde é para buscar e o que
            print(f"NOME: {contato['nome']}")
            print(f"TELEFONE: {contato['telefone']}")
            print(f"EMAIL: {contato['email']}")
            print(f"ENDEREÇO: {contato['endereco']}")
            print(f"ANIVERSÁRIO: {contato['aniversario']}")
            print("=========================================")

    def atualizar_contato(self):
        id = int(input("Me diga o 'ID' do contato que você quer atualizar: "))
        dado_atualizado = input("O que você quer atualizar? (nome, telefone, email, endereco, aniversario): ").lower()
        novo_valor = input(f"Qual o novo valor para {dado_atualizado}? ")
        for contato in self.contatos:
               contato[dado_atualizado] = novo_valor
               salvar_contatos(self.contatos)  # ai ele chama a def para salvar a variavel em py para dentro do arquivo JSON
        print(f"\nContato com ID {id} atualizado com sucesso!\n")
               

    def deletar_contato(self):
        escolha_deletar = int(input("Me diga o 'ID' do contato que você quer deletar: "))
        #Aqui ele faz uma nova lista com todos os contatos menos o que tem o id igual ao que o usuario escolheu, assim deletando o contato do arquivo
        self.contatos = [contato for contato in self.contatos if contato['id'] != escolha_deletar]
        salvar_contatos(self.contatos)  # ai ele chama a def para salvar a variavel em py para dentro do arquivo JSON
        print(f"Contato com ID {escolha_deletar} deletado com sucesso!\n")

#cria o objeto da class Agenda para chamar as funções as quais são estaticas
agenda_principal = Agenda()


#um loop infinito para fazaer de menu
while True:
    print('\n|--------1-CADASTRAR NOVO CONTATO-------|')
    print('|--------2-LISTAR MEUS CONTATOS-----------|')
    print('|--------3-EDITAR CONTATO-----------------|')
    print('|--------4-DELETAR CONTATO----------------|')
    print('|--------5-SAIR---------------------------|\n')
    opcao=int(input('DIGITE A OPÇÃO DESEJADA: \n'))

    match opcao:
        case 1:
            agenda_principal.adicionar_contato()
        case 2:
            agenda_principal.listar_contatos()
        case 3:
            agenda_principal.atualizar_contato()
        case 4:
            agenda_principal.deletar_contato()
        case 5:
            print('SAINDO DO PROGRAMA...')
            break