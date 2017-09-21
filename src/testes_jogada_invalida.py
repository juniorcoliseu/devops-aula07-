import jogovelha
import sys

erro = False
lin = 1
col = 1
jogador = 'X'
jogovelha.inicializar()
jogovelha.jogar(jogador, lin, col)

try:
    jogovelha.jogar(jogador, lin, col)
except:
    erro = True

if erro:
  print('Erro!')
  sys.exit(1)
else:
  sys.exit(0)