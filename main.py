import random

#funcoes
def Menu():
    print("Boas vindas!!")
    print("Escolha sua classe: ")
    print("1) Guerreiro (+ resistente, - dano e magia defensiva)")
    print("2) Mago (- resistente, + dano e magia poderosa)")

def MenuLoja(personagem):
    print("Boas vindas a loja!")
    print("Digite o que deseja comprar")
    print(f"Seu dinheiro: {personagem['dinheiro']}")
    print("1) Pocao de vida (20 de vida) - 50 moedas")
    print("2) Pocao de mana (10 de mana) - 25 moedas")
    print("3) Chave de bau - 100 moedas")
    print("4) Sair da loja")

def checkStatus(personagem):
    print(f"Vida: {personagem['vida']}")
    print(f"Dano: {personagem['dano']}")
    print(f"Mana: {personagem['mana']}")
    print(f"Dinheiro: {personagem['dinheiro']}")
    print(f"Chave: {personagem['chave']}")
    print(f"Pocao de vida: {personagem['pVida']}")
    print(f"Pocao de mana: {personagem['pMana']}")

def escolhaLoop(opcoesValida):
    while True:
        try:
            escolha = int(input("Digite sua escolha: "))
            if (escolha in opcoesValida):
                return escolha
            print("Opção inválida! Digite novamente.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")

def temDinheiro(personagem, valor):
    if(personagem["dinheiro"] >= valor):
        print("Compra sucedida")
        return True
    else:
        print("Voce nao tem dinheiro suficiente")
        return False

def loja(personagem):
    while True:
        MenuLoja(personagem)
        compra = escolhaLoop([1, 2, 3, 4])
        if(compra == 1):
            if temDinheiro(personagem, 50):
                personagem["dinheiro"] -= 50
                personagem["pVida"] += 1
                print("Voce comprou uma pocao de vida!")
                print(f"Dinheiro restante: {personagem['dinheiro']}")
        elif(compra == 2):
            if temDinheiro(personagem, 25):
                personagem["dinheiro"] -= 25
                personagem["pMana"] += 1
                print("Voce comprou uma pocao de mana!")
                print(f"Dinheiro restante: {personagem['dinheiro']}")
        elif(compra == 3):
            if temDinheiro(personagem, 100):
                personagem["dinheiro"] -= 100
                personagem["chave"] += 1
                print("Voce comprou uma chave!")
                print(f"Dinheiro restante: {personagem['dinheiro']}")
        else:
            break

    print("Boa aventura!")

def combateMenu(personagem, oponente):
    print("1) Atacar")
    print("2) Usar magia")
    print("3) Usar pocao")
    print("4) Fugir")
    print("------------------------------")
    print(f"Sua vida: {personagem['vida'] }")
    print(f"Vida do oponente: {oponente['vida'] }")
    print("------------------------------")

def atacar(atacante, alvo):
    if(alvo["defendendo"] == True):
        alvo["vida"] -= int(atacante["dano"] * 0.5)
        alvo["defendendo"] = False
        print(f"{atacante['nome']} causou {int(atacante['dano'] * 0.5)} a {alvo['nome']}")
    else:
        alvo["vida"] -= atacante["dano"]
        print(f"{atacante['nome']} causou {atacante['dano']} a {alvo['nome']}")
    
    
    if(alvo["vida"] < 0):
        alvo["vida"] = 0

    print(f"Vida de {alvo['nome']}: {alvo['vida']}")
    
def magia(atacante, alvo):
    if(atacante["mana"] < 2):
            print("Voce nao tem mana suficiente!")
            return
    else:
        if(atacante["classe"] == 1):
            if atacante["defendendo"]:
                print("Você já está defendendo!")
            else:
                print(f"Você levanta seu escudo! O próximo ataque sofrido terá o dano reduzido em 50%.")
                atacante['mana'] -= 2
                atacante["defendendo"] = True
        else:
            print(f"Voce conjura uma bola de fogo, causando {atacante['dano'] * 2} de dano")
            alvo["vida"] -= atacante["dano"] * 2
            atacante['mana'] -= 2
            if(alvo["vida"] < 0):
                alvo["vida"] = 0
            print(f"{atacante['nome']} causou {atacante['dano'] * 2} a {alvo['nome']}")
            print(f"Vida de {alvo['nome']}: {alvo['vida']}")

#50 e 30
def beberPocao(personagem):
    print("Voce possui:")
    print(f"{personagem['pVida']} pocoes de vida")
    print(f"{personagem['pMana']} pocoes de mana")
    print("Qual voce deseja usar:")
    print("1) Pocao de vida")
    print("2) Pocao de mana")

    escolha = escolhaLoop([1, 2])

    if escolha == 1:
        if personagem["pVida"] <= 0:
            print("Voce nao possui pocoes de vida!")
            return

        personagem["pVida"] -= 1
        personagem["vida"] += 20

        if personagem["vida"] > personagem["vidaMax"]:
            personagem["vida"] = personagem["vidaMax"]

        print("Voce bebe uma pocao de vida!")
        print(f"Sua vida: {personagem['vida']}")

    else:
        if personagem["pMana"] <= 0:
            print("Voce nao possui pocoes de mana!")
            return

        personagem["pMana"] -= 1
        personagem["mana"] += 10

        if personagem["mana"] > personagem["manaMax"]:
            personagem["mana"] = personagem["manaMax"]

        print("Voce bebe uma pocao de mana!")
        print(f"Sua mana: {personagem['mana']}")



def alvoMorto(alvo):
    if(alvo["vida"] == 0):
        return True
    else:
        return False
    


def inimigo(personagem, oponente):
    
    print(f"Um {oponente['nome']} Apareceu!!!")

    while True:
        combateMenu(personagem, oponente)
        print("Seu turno!")
        escolha = escolhaLoop([1, 2, 3, 4])
        
        if(escolha == 1):
            atacar(personagem, oponente)
            if alvoMorto(oponente):
                print(f"Voce derrotou o {oponente['nome']}")
                return "vitoria"
        elif(escolha == 2):
            magia(personagem, oponente)
            if alvoMorto(oponente):
                print(f"Voce derrotou o {oponente['nome']}")
                return "vitoria"
        elif(escolha == 3):
            beberPocao(personagem)
        elif(escolha == 4):
            if(oponente["fuga"] == True):
                fuga = random.randint(1, 100)
                if(fuga >= 70):
                    print("Voce consegue escapar")
                    return "fuga"
                else:
                    print("Voce nao conseguiu escapar")
            else:
                print("Voce nao pode escapar dele...")

        print("Turno do oponente!")
        atacar(oponente, personagem)
        if alvoMorto(personagem):
                print("Voce foi derrotado...")
                return "derrota"

def bau(personagem):
    print("Voce encontrou um bau!")
    if(personagem["chave"] == 0):
        print("Infelizmente voce nao possui nenhuma chave!")
        return

    print("Deseja abrir?")
    print("1) Sim")
    print("2) Nao")
    bauEscolha = escolhaLoop([1, 2])
    if(bauEscolha == 1):
        print("Voce utilizou uma chave.")
        personagem["chave"] -= 1
        mimicoC = random.randint(1, 100)
        if(mimicoC <=30):
            mimico = {
                "nome": "Mimico",
                "vida": 70,
                "dano": 15,
                "fuga": False,
                "defendendo": False
            }
            print("O bau se transformou em um mimico!")
            inimigo(personagem, mimico)
        else:
            loot = random.randint(1, 4)
            if(loot == 1):
                if(personagem["classe"] == 1):
                    print(f"Voce encontrou a espada sagrada. Seu dano aumentou de {personagem['dano']} para 30!")
                    personagem["dano"] = 30
                else:
                    print(f"Voce encontrou o cajado. Seu dano aumentou de {personagem['dano']} para 20!")
                    personagem["dano"] = 20
            elif(loot == 2):
                print("Voce encontrou 2 pocoes de vida!")
                personagem["pVida"] += 2
            elif(loot == 3):
                print("Voce encontrou 2 pocoes de mana!")
                personagem["pMana"] += 2
            else:
                print("O bau estava vazio...")  
    else:
        print("Voce decidiu nao abrir o bau...")
        return
    
    

def dungeon(personagem):
    totalcombateV = 0
    while totalcombateV < 3:
        evento = random.randint(1, 3)

        print(f"Inimigos derrotados: {totalcombateV}/3")

        oponente = {
            "nome": "Goblin",
            "vida": 30,
            "dano": 10,
            "fuga": False,
            "defendendo": False
        }
        
        if(evento == 1):
            resultado = inimigo(personagem, oponente)
            if(resultado == "vitoria"):
                loot = random.randint(1, 2)
                if(loot == 1):
                    dinheiroloot = random.randint(20, 50)
                    print(f"O goblin dropou {dinheiroloot} moedas!")
                    personagem["dinheiro"] += dinheiroloot
                else:
                    pocaoloot = random.choice(["vida", "mana"])
                    if(pocaoloot == "vida"):
                        print(f"O goblin dropou 1 pocao de vida")
                        personagem["pVida"] += 1
                    else:
                        print(f"O goblin dropou 1 pocao de mana!")
                        personagem["pMana"] += 1
                totalcombateV += 1
            elif(resultado == "fuga"):
                if(personagem["dinheiro"] >= 10):
                    print("Mas deixou algumas moedas para tras...")
                    personagem["dinheiro"] -= 10
            else:
                print("Sua historia infelizmente termina aqui...")
                return "morte"
        elif(evento == 2):
            bau(personagem)
        else:
            print("Nada aconteceu por enquanto...")
    
    print("PARABÉNS! Você limpou a dungeon!")
    print("Mas algo estranho acontece... Voce encontra finalmente o boss!!!")

    boss = {
            "nome": "Rei Goblin",
            "vida": 120,
            "dano": 20,
            "defendendo": False,
            "fuga": False
        }
    resultado = inimigo(personagem, boss)
    if(resultado == "vitoria"):
        print("Parabens, voce derrotou o Rei Goblin e completou a dungeon!")
        return "vitoria"
    else:
        print("Sua historia infelizmente termina aqui...")
        return "morte"


        


#----------------------------------------
Menu()
persona = escolhaLoop([1, 2])


if (persona == 1):
    personagem = {
        "nome": "voce",
        "classe": 1,
        "defendendo": False,
        "vidaMax": 50,
        "manaMax": 10,
        "vida": 50,
        "dano": 15,
        "mana": 10,
        "dinheiro": 200,
        "chave": 0,
        "pVida": 1,
        "pMana": 1
    }
else:
    personagem = {
        "nome": "voce",
        "classe": 2,
        "defendendo": False,
        "vidaMax": 30,
        "manaMax": 20,
        "vida": 30,
        "dano": 10,
        "mana": 20,
        "dinheiro": 200,
        "chave": 0,
        "pVida": 1,
        "pMana": 1
    }

while True:
    print("Você chega à pequena vila de Eldoria, conhecida por suas dungeons cheias de tesouros… e perigos. Os moradores estão com medo — uma criatura misteriosa apareceu na dungeon principal. Com algumas moedas no bolso, você precisa decidir seu próximo passo.")

    escolha = escolhaLoop([1, 2, 3])
    if (escolha == 1):
        print("Voce decide se equipar.")
        loja(personagem)
    elif(escolha == 3):
        checkStatus(personagem)
    else:
        print("Voce decide entrar na dungeon...")
        resultado = dungeon(personagem)
        if(resultado == "vitoria"):
            print("Voce retorna a sua casa com a gloria!")
            break
        else:
            print("infelizmente voce sucumbiu a dungeon...")
            break

