def matrix_function(user_string):
    #Criar matriz
    def matrix(lins, cols, val_inic):
        m = [[val_inic] * cols for _ in range(lins)]
        return m
    mat = matrix(9, 9, " ")

    #REMOVER "," E ":" DA STRING DOS VALORES DA MATRIZ// A,3:5 -->  A35
    c_remove = ",:"
    for i in range(0,len(c_remove)):
        user_string =user_string.replace(c_remove[i],"")
    #SEPARAR OS ELEMENTOS DA STRING// A35 --> (A)   (3)    (5) 
    col_string = user_string[0]
    line_string = user_string[1]
    value_string = user_string[2]
    # Converter letra minúscula em maiúscula
    col_string = col_string.upper()
    # COVERTER line_string E value_string, EM INT
    line_value = int(line_string) - 1
    value_value = int(value_string)
    #converter a letra da coluna em um valor
    list = [
        'A','B','C',
        'D','E','F',
        'G','H','I'   
    ]
    col_value = 0
    for i in range(len(list)):
        if col_string == list[i]:
            break
        col_value += 1

    #atribuir valores à matriz
    mat[line_value][col_value] = value_value
    matriz = """
        A   B   C    D   E   F    G   H   I
    ++---+---+---++---+---+---++---+---+---++             
    1|| {0} | {1} | {2} || {3} | {4} | {5} || {6} | {7} | {8} ||      
    ++---+---+---++---+---+---++---+---+---++    
    2|| {9} | {10} | {11} || {12} | {13} | {14} || {15} | {16} | {17} ||         
    ++---+---+---++---+---+---++---+---+---++        
    3|| {18} | {19} | {20} || {21} | {22} | {23} || {24} | {25} | {26} ||
    ++===+===+===++===+===+===++===+===+===++            
    4|| {27} | {28} | {29} || {30} | {31} | {32} || {33} | {34} | {35} ||      
    ++---+---+---++---+---+---++---+---+---++    
    5|| {36} | {37} | {38} || {39} | {40} | {41} || {42} | {43} | {44} ||         
    ++---+---+---++---+---+---++---+---+---++        
    6|| {45} | {46} | {47} || {48} | {49} | {50} || {51} | {52} | {53} ||
    ++===+===+===++===+===+===++===+===+===++             
    7|| {54} | {55} | {56} || {57} | {58} | {59} || {60} | {61} | {62} ||      
    ++---+---+---++---+---+---++---+---+---++    
    8|| {63} | {64} | {65} || {66} | {67} | {68} || {69} | {70} | {71} ||         
    ++---+---+---++---+---+---++---+---+---++        
    9|| {72} | {73} | {74} || {75} | {76} | {77} || {78} | {79} | {80} ||
    ++===+===+===++===+===+===++===+===+===++
    """

    matriz = matriz.format(
        mat[0][0], mat[0][1], mat[0][2], mat[0][3], mat[0][4],mat[0][5], mat[0][6],mat[0][7], mat[0][8],
        mat[1][0], mat[1][1], mat[1][2], mat[1][3], mat[1][4],mat[1][5], mat[1][6],mat[1][7], mat[1][8],
        mat[2][0], mat[2][1], mat[2][2], mat[2][3], mat[2][4],mat[2][5], mat[2][6],mat[2][7], mat[2][8],
        mat[3][0], mat[3][1], mat[3][2], mat[3][3], mat[3][4],mat[3][5], mat[3][6],mat[3][7], mat[3][8],
        mat[4][0], mat[4][1], mat[4][2], mat[4][3], mat[4][4],mat[4][5], mat[4][6],mat[4][7], mat[4][8],
        mat[5][0], mat[5][1], mat[5][2], mat[5][3], mat[5][4],mat[5][5], mat[5][6],mat[5][7], mat[5][8],
        mat[6][0], mat[6][1], mat[6][2], mat[6][3], mat[6][4],mat[6][5], mat[6][6],mat[6][7], mat[6][8],
        mat[7][0], mat[7][1], mat[7][2], mat[7][3], mat[7][4],mat[7][5], mat[7][6],mat[7][7], mat[7][8],
        mat[8][0], mat[8][1], mat[8][2], mat[8][3], mat[8][4],mat[8][5], mat[8][6],mat[8][7], mat[8][8]
    )

    print(matriz)

matrix_function(input("Insira os valores da matriz: "))