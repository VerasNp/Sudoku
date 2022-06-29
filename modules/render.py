def render_sudoku(mat):

    matrix_template = """
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

    formatted_matrix = matrix_template.format(
        mat[0][0]["number"], mat[0][1]["number"], mat[0][2]["number"], mat[0][3]["number"], mat[0][4]["number"], mat[0][5]["number"], mat[0][6]["number"], mat[0][7]["number"], mat[0][8]["number"],
        mat[1][0]["number"], mat[1][1]["number"], mat[1][2]["number"], mat[1][3]["number"], mat[1][4]["number"], mat[1][5]["number"], mat[1][6]["number"], mat[1][7]["number"], mat[1][8]["number"],
        mat[2][0]["number"], mat[2][1]["number"], mat[2][2]["number"], mat[2][3]["number"], mat[2][4]["number"], mat[2][5]["number"], mat[2][6]["number"], mat[2][7]["number"], mat[2][8]["number"],
        mat[3][0]["number"], mat[3][1]["number"], mat[3][2]["number"], mat[3][3]["number"], mat[3][4]["number"], mat[3][5]["number"], mat[3][6]["number"], mat[3][7]["number"], mat[3][8]["number"],
        mat[4][0]["number"], mat[4][1]["number"], mat[4][2]["number"], mat[4][3]["number"], mat[4][4]["number"], mat[4][5]["number"], mat[4][6]["number"], mat[4][7]["number"], mat[4][8]["number"],
        mat[5][0]["number"], mat[5][1]["number"], mat[5][2]["number"], mat[5][3]["number"], mat[5][4]["number"], mat[5][5]["number"], mat[5][6]["number"], mat[5][7]["number"], mat[5][8]["number"],
        mat[6][0]["number"], mat[6][1]["number"], mat[6][2]["number"], mat[6][3]["number"], mat[6][4]["number"], mat[6][5]["number"], mat[6][6]["number"], mat[6][7]["number"], mat[6][8]["number"],
        mat[7][0]["number"], mat[7][1]["number"], mat[7][2]["number"], mat[7][3]["number"], mat[7][4]["number"], mat[7][5]["number"], mat[7][6]["number"], mat[7][7]["number"], mat[7][8]["number"],
        mat[8][0]["number"], mat[8][1]["number"], mat[8][2]["number"], mat[8][3]["number"], mat[8][4]["number"], mat[8][5]["number"], mat[8][6]["number"], mat[8][7]["number"], mat[8][8]["number"]
    )

    print(formatted_matrix)
