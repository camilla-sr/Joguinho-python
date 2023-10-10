#--------------- ITENS DO TUTORIAL ---------------
chave_chavosa = False

#--------------- INÍCIO DO JOGO ------------------
def inicio():
    print('''
                                Bem-vindo a Dylendious
''')
    print('''
    Você acordou caído em um lugar fechado
''')
    resposta_1 = input("   >> ")
    while(resposta_1.upper() != 'LEVANTAR'):
        resposta_1 = input(" >> ")
    else:
        comodo()

def comodo():
        print('''
    É um cômodo é pequeno.
    À sua ESQUERDA há uma escrivaninha velha
    DIREITA, uma caixa, e à FRENTE uma porta.
''')
        caminho = ['ESQUERDA', 'DIREITA', 'FRENTE']
        decisao_1 = input("   >> ")
        while(decisao_1.upper() not in caminho):
            decisao_1 = input("   >> ")
        else:
            if decisao_1.upper() == caminho[1]:
                caminhoDireita()
            elif decisao_1.upper() == caminho[0]:
                caminhoEsquerda()
            elif decisao_1.upper() == caminho[2]:
                caminhoFrente()

#--------------- CAMINHO DA DIREITA --------------
def caminhoDireita():
        print('''
    Você encontrou uma caixa de madeira simples sem cadeados.
    Do lado de dentro da tampa, você nota um desenho estranho.
    Dentro da caixa está uma pequena chave.
''')
        escolha_caixa = ['PEGAR', 'VOLTAR']
        caixa = input("   >> ")
        while(caixa.upper() not in escolha_caixa):
            caixa = input("   >> ")
        else:
            global chave_chavosa
            if caixa.upper() == escolha_caixa[0]:
                chave_chavosa = True
                print('''
   Você pegou a chave uma chave simples
''')
                chavosa = input("   >> ")
                while(chavosa.upper() != 'VOLTAR'):
                    chavosa = input("   >> ")
                else:
                    comodo()
            if caixa.upper() == escolha_caixa[1]:
                comodo()
            
#--------------- CAMINHO DA ESQUERDA -------------
def caminhoEsquerda():
    print('''
    Essa escrivaninha parece ter sido muito usada,
    mas não há nada sobre ela além de inscrições talhadas no tampo.
    Talvez alguém tenha feito isso com as próprias unhas.
    Na parte da frente, existe uma gaveta. No meio dela há uma abertura.
''')
    escolha_mesa = ['VOLTAR', 'LER', 'ABRIR COM CHAVE']
    mesa = input("   >> ")
    while(mesa.upper() not in escolha_mesa):
        mesa = input("   >> ")
    else:
        if mesa.upper() == escolha_mesa[0]:
            comodo()
        elif mesa.upper() == escolha_mesa[1]:
            print('''
    Os arranhões formam números fora de uma sequencia lógica
            14 1 15   3 15 14 6 9 5   14 5 12 5 19
''')
            tampo = input("   >> ")
            while(tampo.upper() != 'VOLTAR'):
                tampo = input("   >> ")
            else:
                caminhoEsquerda()
        elif mesa.upper() == escolha_mesa[2]:
            if chave_chavosa == True:
                print('''
    A gaveta está vazia, mas o fundo dela está marcado
    com algo que você espera ser tinta vermelha
                    18 21 13 15
''')
                chavinha = input("   >> ")
                while(chavinha.upper() != 'VOLTAR'):
                    chavinha = input("   >> ")
                else:
                    caminhoEsquerda()
            elif chave_chavosa == False:
                print("Você não pode abrir a gaveta apenas com os dedos")
            while(mesa.upper() != 'VOLTAR'):
                mesa = input("   >> ")
            else:
                caminhoEsquerda()

#--------------- CAMINHO DA FRENTE ----------------
def caminhoFrente():
    print('''
    A porta não abre. Há uma tranca eletrônica pedindo
    por uma senha de quatro caracteres.
''')
    escolha_porta = ['VOLTAR', 'RUMO']
    porta = input("   >> ")
    while(porta.upper() not in escolha_porta):
        porta = input("   >> ")
    else:
        if porta.upper() == escolha_porta[0]:
            comodo()
        if porta.upper() == escolha_porta[1]:
            print('''
                    Obrigado por jogar o tutorial!
''')
            
if __name__ == "__main__":
    inicio()