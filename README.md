
# ⚔️ Dungeon de Eldoria

  

Um jogo de RPG de texto em Python, onde você escolhe sua classe, explora uma dungeon cheia de perigos, enfrenta inimigos e tenta derrotar o temido **Rei Goblin**.

  

---

  

## 📖 Sobre o Jogo

  

Você chega à pequena vila de **Eldoria**, conhecida por suas dungeons cheias de tesouros… e perigos. Os moradores estão com medo — uma criatura misteriosa apareceu na dungeon principal. Com algumas moedas no bolso, você decide o que fazer a seguir.

  

---

  

## 🚀 Como Jogar

  

### Pré-requisitos

  

- Python 3.x instalado

  

### Executando o jogo

  

```bash

python  main.py

```

  

---

  

## 🧙 Classes Disponíveis

  

Ao iniciar o jogo, você escolhe uma das duas classes:

  

| Classe | Vida | Mana | Dano | Estilo de Jogo |
|--|--|--|--|--|
| Guerreiro | 50 | 10 | 15 | Resistente, usa magia defensiva (escudo) |
| Mago | 30 | 20 | 10 | Frágil, mas conjura bolas de fogo devastadoras |

  

---

  

## 🗺️ Estrutura do Jogo

  

### Vila de Eldoria (Menu Principal)

  

Na vila, você pode:

  

1.  **Ir à Loja** — Comprar itens antes de entrar na dungeon

2.  **Entrar na Dungeon** — Iniciar a aventura

3.  **Ver Status** — Checar seus atributos e inventário

  

### Loja

  

| Item | Efeito | Custo |
|--|--|--|
| Poção de Vida | +20 de vida | 50 moedas |
| Poção de Mana | +10 de mana | 25 moedas |
| Chave de Baú | Abre baús na dungeon | 100 moedas |

  

### Dungeon

  

A dungeon gera eventos aleatórios a cada andar:

  

- ⚔️ **Combate** — Enfrente um Goblin

- 📦 **Baú** — Encontre recompensas (ou um Mímico!)

- 😶 **Nada** — O corredor está vazio

Você precisa **derrotar 3 inimigos** para enfrentar o boss final.

  

---

  

## ⚔️ Sistema de Combate

  

Durante o combate, você tem 4 ações disponíveis:

  

1.  **Atacar** — Causa dano normal ao inimigo

2.  **Usar Magia**

-  *Guerreiro:* Levanta o escudo, reduzindo o próximo dano recebido em 50%

-  *Mago:* Conjura uma bola de fogo que causa o dobro do dano (custa 2 de mana)

3.  **Usar Poção** — Usa uma poção de vida ou mana do inventário

4.  **Fugir** — Tenta escapar do combate

> ⚠️ Atenção: Alguns inimigos **não permitem fuga**!

---

  

## 👾 Inimigos

| Inimigo | Vida | Dano | Onde aparece |
| -- | -- | -- | -- |
| Goblin | 30 | 10 |  Dungeon (evento aleatório) |
| Mímico | 70 | 15 |  Dentro de baús (30% de chance) |
| Rei Goblin | 120 | 20 |  Boss final |

  

---

  

## 🎁 Recompensas

  

### Após derrotar um Goblin (aleatório):

- 💰 Entre 20 e 50 moedas

- 🧪 1 Poção de vida ou de mana

  

### Dentro de baús (se não for Mímico):

- 🗡️ Arma especial (aumenta o dano permanentemente)

- 🧪 2 Poções de vida

- 🧪 2 Poções de mana

- 📦 Baú vazio

  

---

  

## 🏆 Condições de Vitória e Derrota

  

- ✅ **Vitória** — Derrote o Rei Goblin ao fim da dungeon

- ❌ **Derrota** — Sua vida chegar a zero em qualquer combate

  

---

  

## 📁 Estrutura do Código

  

```

main.py

├── Menu() # Exibe o menu inicial de seleção de classe

├── MenuLoja() # Exibe o menu da loja

├── checkStatus() # Exibe os atributos do personagem

├── escolhaLoop() # Lê e valida entradas do jogador

├── temDinheiro() # Verifica se o jogador tem saldo suficiente

├── loja() # Lógica completa da loja

├── combateMenu() # Exibe o menu de combate

├── atacar() # Executa um ataque físico

├── magia() # Executa a habilidade mágica da classe

├── beberPocao() # Usa uma poção do inventário

├── alvoMorto() # Verifica se um alvo foi derrotado

├── inimigo() # Loop principal de combate

├── bau() # Evento de baú (tesouro ou Mímico)

└── dungeon() # Loop principal da dungeon

```

  

---

## 🛠️ Possíveis Melhorias Futuras

- [ ] Mais classes (Arqueiro, Paladino...)

- [ ] Sistema de experiência e level up

- [ ] Mais tipos de inimigos e dungeons

- [ ] Salvar progresso entre sessões

- [ ] Interface gráfica (pygame ou tkinter)

## Licença
Este projeto está licenciado sob a Licença **MIT**. Veja o arquivo LICENSE para detalhes.

## Autor
Gabriel Makiyama Nakashima  
gabrielmnakashima2@gmail.com  
![](https://media1.tenor.com/m/LyyWKCKBahoAAAAd/cosmic-princess-kaguya-cpk.gif)
