from modules.batch_mode import start_batch_mode
from modules.interactive_mode import start_interactive_mode
from modules.matrix import init_sudoku_matrix


def start_game(params: list) -> None:
	# TODO: Geração de matrix genérica!
	matrix = init_sudoku_matrix()

	if len(params) > 1:
		start_batch_mode(
			init_matrix=matrix,
			files=params)
	else:
		start_interactive_mode(
			init_matrix=matrix,
			files=params)


def helper():
	print("""
	USAGE: python sudoku.py <config_file> <play_file>
	
	  Nosso jogo consta com dois modos de escolhidos através da quantidade de arquivos        
      passados como parâmetro!                                                                
                                                                                              
     1- Modo Interativo:                                                                      
                                                                                              
        Nesse modo você deve passar como parâmetro um arquivo de configuração contendo        
        todas as dicas que o jogo terá. Lembrando, o arquivo deve ter a extensao .txt         
         para que sejam validas as configuracoes e deve possuir de 1 a 80 dicas!              
                                                                                              
        A partir daí será necessário informar cada jogada sendo possível ser feitas 2         
        tipos: adicao e remocao.                                                              
                                                                                              
        Na adicao será adicionado na coordenada especificada o número informado na jogada.    
        Se desejar substituir uma jogada ja executada basta informar a mesma coordenada de     
        onde se deseja fazer a substituicao e o novo numero a ser inserido no lugar. Dicas    
        nao podem ser alteradas! O formato da jogada de adicao sera <COLUNA>,<LINHA>:<NUMERO> 
                                                                                              
        Na remocao sera removido um numero inserido, lembrando, que assim como na adicao,     
        dicas nao podem ser removidas! O formato da jogada de remocao será D<COLUNA>,<LINHA>  
                                                                                              
     2- Modo Batch:                                                                           
                                                                                              
        Nesse modo você deve passar como parâmetro 2 arquivos, um arquivo de configuração     
        contendo as dicas e um arquivo contendo as jogadas. Lembrando, o arquivo deve ter     
        a extensao .txt para que sejam validas as configuracoes e as jogadas!                 
                                                                                              
        Primeiro será validado o arquivo de pistas. Pistas repetidas serão ignoradas e        
        caso haja pistas ferindo as regras, será exibida uma mensagem de erro.                
                                                                                              
        Em seguida será lido o arquivo de jogadas, as jogadas inválidas serão informadas.     
        Também será informado se as jogadas preenchem ou não a grade.                     
	
	
	""")
