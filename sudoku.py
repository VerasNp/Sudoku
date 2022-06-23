import os
import sys
if len(sys.argv) > 3:
    print("One or more arquive(s) inserted than needed")
    sys.exit()
if len(sys.argv) > 1:
    #Checando se tem um argumento e se ele termina em .txt
    if sys.argv[1].endswith(".txt"):
        print("It is .txt")
        #Procurando na pasta se o argumento está presente
        if os.path.isfile(sys.argv[1]):
            print(f"This file exists on the folder")
        else:
            print(f"This file does not exist on the folder")
            sys.exit()
    else:
        print("It isn't .txt")
        sys.exit()
    if len(sys.argv) == 3:
    #Checando se tem 2º argumento, se ele termina em .txt e se está na pasta
        if sys.argv[2].endswith(".txt"):
            print("It is .txt")
        #Procurando na pasta se o 2º argumento está presente
            if os.path.isfile(sys.argv[2]):
                print(f"This file exists on the folder")
            else:
                print(f"This file does not exist on the folder")
                sys.exit()
        else:
            print("It isn't .txt")
            sys.exit()
print("Working as the Founding Fathers intended")   
