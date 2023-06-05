Implementação do método ship-based para resolver um puzzle Bimaru utilizando inteligência artificial. Realizado por Tiago Deane e Artur Krystopchuk


## Formato do input:

As instâncias do problema Bimaru são constituídas por 3 partes:

1. A primeira linha é iniciada com a palavra ROW e contém informação relativa à contagem de posições ocupadas em cada linha da grelha.
2. A segunda linha é iniciada com a palavra COLUMN e contém informação relativa à contagem de posições ocupadas em cada coluna da grelha.
3. A terceira linha contém um inteiro que corresponde ao número de dicas.
4. As linhas seguintes são iniciadas com a palavra HINT e contêm as dicas correspondentes às posições pré-preenchidas.

Formalmente, cada uma das 4 partes acima descritas tem a seguinte formatação:

1. ROW <count-0> ... <count-9>
2. COLUMN <count-0> ... <count-9>
3. <hint total>
4. HINT <row> <column> <hint value>

Os valores possíveis para <row> e <column> são os números inteiros entre 0 e 9. O canto superior esquerdo da grelha correponde às coordenadas (0,0).
Os valores possíveis para <hint value> são: W (water), C (circle), T (top), M (middle), B (bottom), L (left) e R (right).
Palavras na mesma linha são divididas por \t.


## Formato do output:

O output do programa deve descrever uma solução para o problema de Bimaru descrito no ficheiro de input, i.e., uma grelha completamente preenchida que respeite as regras previamente enunciadas. O output deve seguir o seguinte formato:

• 10 linhas, onde cada linha indica o conteúdo da respetiva linha da grelha.
• Nas posições pré-preenchidas (correspondentes a dicas) é colocada a respetiva letra maiúscula.
• Nas outras posições são colocadas as respetivas letras, mas minúsculas, com exceção das posições de água que, por questões de legibilidade, são representadas por um ponto.
• Todas as linhas, incluindo a última, são terminadas pelo carater newline, i.e. \n


## Exemplo:

Input:
ROW\t2\t3\t2\t2\t3\t0\t1\t3\t2\t2\n
COLUMN\t6\t0\t1\t0\t2\t1\t3\t1\t2\t4\n
6\n
HINT\t0\t0\tT\n
HINT\t1\t6\tM\n
HINT\t3\t2\tC\n
HINT\t6\t0\tW\n
HINT\t8\t8\tB\n
HINT\t9\t5\tC\n

Output:
T.....t...\n
b.....M..t\n
......b..m\n
..C......m\n
c......c.b\n
..........\n
W...t.....\n
t...b...t.\n
m.......B.\n
b....C....\n