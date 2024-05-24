Projeto JOGO DA VELHA EM PYTHON

Integrantes:

Mateus Gomes Vieira de Andrade (RGM: 39094570)
Gabriel Delano Lima Gomes Monteiro (RGM: 37766988)
Fellipe Abrantes Soares (RGM: 38208938)

1. Resumo do Jogo:
O código consiste no clássico jogo da velha, utilizando como linguagem, o Python. Dois jogadores disputam preenchendo um tabuleiro 3x3 com 'X' ou 'O' um de cada vez. O jogo termina quando um jogador completa uma linha, coluna ou diagonal com seus símbolos (Três consecutivos), ou quando todos os espaços do tabuleiro são preenchidos sem nenhum vencedor.

2. Funções:

- A função tela() exibe o tabuleiro atualizado após cada jogada;

- As funções jogador1() e jogador2() permitem que os jogadores façam suas jogadas, verificando se os índices inseridos (linha e coluna) estão dentro dos espaços em branco do tabuleiro. Após uma jogada válida, a função atualiza a grade com o símbolo correspondente.

- A função verificarVitoria() verifica se houve um vencedor, verificando todas as linhas, colunas e diagonais. Se um jogador vencer, a função retorna True e armazena o símbolo do vencedor na variável vit. Se houver um empate, vit é definido como 'E'. Esta função também retorna True quando todas as jogadas possíveis foram feitas sem nenhum vencedor.

- A função redefinir() redefine as variáveis para reiniciar o jogo quando necessário.

- O loop principal do jogo permite que os jogadores façam suas jogadas alternadamente até que haja um vencedor ou um empate.

3. Dificuldades:

- Nossa principal dificuldade foi a lógica final das funções, a de verificar vitória e interromper o jogo assim que alguém vencesse por exemplo.
