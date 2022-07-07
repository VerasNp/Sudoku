from modules.batch_mode import start_batch_mode
from modules.interactive_mode import start_interactive_mode
from modules.matrix import init_matrix


def start_game(data: list) -> None:
	"""
	Based in the quantity of args selects the game mode
	:param data:
	:return:
	"""
	# TODO: Geração de matrix genérica!
	matrix = init_matrix(9, 9, {"number": ' ', "hint": None})
	if len(data) > 1:
		start_batch_mode(matrix, data)
	else:
		start_interactive_mode(matrix, data)


def helper():
	print("""
 ______      # __  __      # ______      # ______      # ___   ___     # __  __      #
/_____/\     #/_/\/_/\     #/_____/\     #/_____/\     #/___/\/__/\    #/_/\/_/\     #
\::::_\/_    #\:\ \:\ \    #\:::_ \ \    #\:::_ \ \    #\::.\ \\ \ \   #\:\ \:\ \    #
 \:\/___/\   # \:\ \:\ \   # \:\ \ \ \   # \:\ \ \ \   # \:: \/_) \ \  # \:\ \:\ \   #
  \_::._\:\  #  \:\ \:\ \  #  \:\ \ \ \  #  \:\ \ \ \  #  \:. __  ( (  #  \:\ \:\ \  #
    /____\:\ #   \:\_\:\ \ #   \:\/.:| | #   \:\_\ \ \ #   \: \ )  \ \ #   \:\_\:\ \ #
    \_____\/ #    \_____\/ #    \____/_/ #    \_____\/ #    \__\/\__\/ #    \_____\/ #
             ##             ##             ##             ##               ##             ##
             
######################################!!BEM VINDO!!#########################################
	Nosso jogo consta com dois modos de escolhidos através da quantidade de arquivos 
	passados como parâmetro!

	1- Modo Interativo:
		Nesse modo você deve passar como parâmetro um arquivo de configuração contendo 
	todas as dicas que o jogo terá. Lembrando, o arquivo deve ter a extensao .txt para 
	que sejam validas as configuracoes!
		A partir daí será necessário informar cada jogada sendo possível ser feitas 2
	tipos: adicao e remocao.
		Na adicao sera adicionado na coordenada especificada o número informado na jogada. 
	Se desejar substituir uma jogada ja executada basta informar a mesma coordenada de onde
	se deseja fazer a substituicao e o novo numero a ser inserido no lugar. Dicas nao podem 
	ser alteradas! O formato da jogada de adicao sera <COLUNA>,<LINHA>:<NUMERO>
		Na remocao sera removido um numero inserido, lembrando, que assim como na adicao,
	dicas nao podem ser removidas! O formato da ogada de remocao será D<COLUNA>,<LINHA>
	2- Modo Batch
	
	
	""")
