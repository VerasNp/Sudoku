# UFC - CK0211 | Sudoku

## The game

-   Objective: Insert numbers 1 to 9 on each empty cell of a 9x9 matrix, made of 3x3 sub matrixes called region. The matrix initiates with some data (hints). Each column, line, and region must have one number from 1 to 9 appearing only once.

-   Solution: The 9x9 matrix must be filled with numbers from 1 to 9 that will appear once in a determined way (column or line) or region.

## Instructions

Develop a Python program to Sudoku with 2 different modes:

### 1. Interactive mode

The program must be executed with a configuration file with the initial hint data of game (from 1 to 80 hint). The hint must have the format:

```
<COL>,<LIN>: <NUMBER>
```

-   `<COL>`: Represents the matrix column with uppercase letters from "A" to "I";
-   `<LIN>`: Represents the matrix line (from 1 to 9);
-   `<NUMBER>`: Represents a number from 1 to 9 that will be added as an initial data (hint)

The configuration file must be passed as a parameter to run the program like:

```
python3 sudoku.py arg_01_ctf.txt
```

After, the program must show the matrix filled with the data inserted on configuration data:

```
A,3:5
F,1:3
D,8:7
H,6:5
```

Equals to:

![](/docs/img/matrix-generated-interactive-mode.png)

This functionality:

-   Requires hint data validation;
-   User will input the data with line and column of entry;
    -   The data input must be validated in different entrances like: "a, 4: 8", "C,2: 8", all those acceptable and validate not valid data like "K,3:8", "A,3:12" and ask the user for a new data.
-   After the data is validated the matrix must be updated with the new data. The insertion of data on a cell already full must have its value updated. If the user tries to insert a number already positioned on the matrix should be an invalid data;

The user should be able to delete data with the command:

```
D<COL><LIN>
```

This functionality:

-   Only removes data if exists something to remove;
-   An hint cannot be deleted.

### 2. Batch mode

This mode must receive 2 files as parameter.

1. List of hints;
2. File with data to be insert.

```
python3 sudoku.py arq_01_cfg.txt arq_01_jog.txt
```

-   Initially, the program must validate the hint file.
    -   If occurs repeated hints, the program must ignore them.
    -   If occurs hints that violate the rules, the program must show an error message: **"Configuracao de dicas invalida."**.
-   With the hint files validated, the program now validates the data file and prints only the invalid data
    ![](/docs/img/data-insert-bach-mode.png)
    ![](/docs/img/data-insert-bach-mode2.png)
-   Do not use any type of special character or punctuation.
