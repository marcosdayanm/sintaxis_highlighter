import csv

def num_lexer(string, white, digits, scientific, operators, punctuation_num, close_keys):

    table = [   
    #    n . e - op otro
        [1,2,9,9,9,9],
        [1,2,3,6,6,9],
        [2,9,3,7,7,9],
        [2,9,9,4,9,9],
        [5,9,9,9,9,9],
        [5,9,9,9,8,9],
    ]

    # flags
    state = 0
    lexeme = ''

    # for c in string:
    for i in range(len(string)):
        c = string[i]

    # Definir qué tipo de dato es cada char analizado
        if c in digits:
            col = 0
        elif c == '.':
            col = 1
        elif c in scientific:
            col = 2
        elif c == '-':
            col = 3
        elif c in operators or c in white or c in punctuation_num or c in close_keys:
            col = 4
        else:
            col = 5

        state = table[state][col]

        if state == 6:
            return [string[i:], lexeme, 'INTEGER']
        elif state in [7,8]:
            return [string[i:], lexeme, 'REAL']
        elif state == 9:
            lexeme += c
            return [string[i+1:], lexeme, 'ERROR']

        if state != 0:
            lexeme += c

    return [string[i:], lexeme, 'ERROR']




def op_lexer(string, white, operators):

    # table = [   
    # #    / op \n esp !\n otro
    #     [1, 3, 5, 5, 5, 5],
    #     [2, 5, 5, 3, 5, 5],
    #     [2, 2, 4, 2, 2, 5],
    # ]


    table = [   
    #    *  /  # op !\n \n otro
        [3,2,1,7,8,8,8],
        [1,1,1,1,1,4,1],
        [8,5,8,8,8,7,8],
        [6,8,8,8,8,7,8]
    ]

    symbols = {
        '+': 'ADDITION',
        '-': 'SUBTRACTION',
        '*': 'MULTIPLICATION',
        '/': 'DIVISION',
        '=': 'ASSIGNMENT',
        '%': 'MODULE',
    }
        
    # flags
    state = 0
    lexeme = ''

    # definiciones


    for i in range(len(string)):
        c = string[i]

        if c == "*":
            col = 0
        elif c in "/":
            col = 1
        elif c == "#":
            col = 2
        elif c in operators:
            col = 3
        elif c != "\n":
            col = 4
        elif c == "\n":
            col = 5
        else:
            col = 6


        state = table[state][col]

        if state == 4:
            return [string[i:], lexeme, 'COMMENT']
        elif state == 5:
            lexeme += c
            return [string[i+1:], lexeme, 'INTEGER_DIVISION']
        elif state == 6:
            lexeme += c
            return [string[i+1:], lexeme, 'POWER']
        elif state == 7:
            lexeme += c
            return [string[i+1:], lexeme, symbols[lexeme[0]]]
        elif state == 8:
            lexeme += c
            return [string[i+1:], lexeme, 'ERROR']

        if state != 0:
            lexeme += c

    return [string[i:], lexeme, 'ERROR']



def var_lexer(string, letters, digits, white, keys, operators, reserved):
    table = [   
    #  lett _ 0-9 = esp otro
        [1, 3, 3, 3, 3, 3],
        [1, 1, 1, 2, 2, 3]
    ]

    state = 0
    lexeme = ''

    for i in range(len(string)):
        c = string[i]

        if c in letters:
            col = 0
        elif c == "_":
            col = 1
        elif c in digits:
            col = 2
        elif c == "=":
            col = 3
        elif c in white or c in keys or c in operators:
        # elif c in white:
            col = 4
        else:
            col = 5

        state = table[state][col]

        if state == 2:
            if lexeme in reserved:
                return [string[i:], lexeme, 'RESERVED']
            return [string[i:], lexeme, 'VARIABLE']
        elif state == 3:
            lexeme += c
            return [string[i+1:], lexeme, 'ERROR']

        if state != 0:
            lexeme += c

    return [string[i:], lexeme, 'ERROR']



def string_lexer(string, white, operators):

    table = [
      #  "  '  \n  otro    
        [1, 2, 4, 4],
        [3, 1, 4, 1],
        [2, 3, 4, 2],
    ]

    for i in range(len(string)):
        c = string[i]

        if c == '\"':
            col = 0
        elif c == "\'":
            col = 1
        elif c == "\n":
            col = 2
        elif c == "=":
            col = 3
        else:
            col = 4

        state = table[state][col]

        if state == 3:
            return [string[i:], lexeme, 'STRING']
        elif state == 4:
            lexeme += c
            return [string[i+1:], lexeme, 'ERROR']

        if state != 0:
            lexeme += c

    return [string[i:], lexeme, 'ERROR']




def output_results_csv(filepath, results):
    with open(filepath, 'w') as file:
        writer = csv.writer(file)
        for r in results:
            writer.writerow(r)



def lexer(file_relative_path):

    string = ""
    with open(file_relative_path, 'r') as file:
        string = file.read()
    string += '\n '

    # print(string)


    # definiciones
    operators = "+-*/=<>%"
    punctuation_num = ",;:"
    open_keys = "([{"
    close_keys = ")]}"
    keys = open_keys + close_keys
    white = [" ", "\n", "\t"]
    digits = "1234567890"
    scientific = "eE"
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    reserved = [
                "False", "None", "True", "and", "as",
                "assert", "async", "await", "break", "class",
                "continue", "def", "del", "elif", "else",
                "except", "finally", "for", "from", "global",
                "if", "import", "in", "is", "lambda",
                "nonlocal", "not", "or", "pass", "raise", "range",
                "return", "try", "while", "with", "yield",
                "__init__", "__del__", "__repr__", "__str__", "__bytes__",
                "__format__", "__lt__", "__le__", "__eq__", "__ne__",
                "__gt__", "__ge__", "__hash__", "__bool__", "__getattr__",
                "__setattr__", "__delattr__", "__dir__", "__getattribute__", "__getitem__",
                "__setitem__", "__delitem__", "__iter__", "__next__", "__call__",
                "__enter__", "__exit__", "__copy__", "__deepcopy__", "__get__",
                "__set__", "__delete__", "__new__", "__reduce__", "__reduce_ex__",
                "BaseException", "Exception", "ArithmeticError", "BufferError", "LookupError",
                "EnvironmentError", "AssertionError", "AttributeError", "EOFError", "FloatingPointError",
                "GeneratorExit", "ImportError", "ModuleNotFoundError", "IndexError", "KeyError",
                "KeyboardInterrupt", "MemoryError", "NameError", "NotImplementedError", "OSError",
                "OverflowError", "ReferenceError", "RuntimeError", "StopIteration", "StopAsyncIteration",
                "SyntaxError", "IndentationError", "TabError", "SystemError", "SystemExit",
                "TypeError", "UnboundLocalError", "UnicodeError", "UnicodeEncodeError", "UnicodeDecodeError",
                "UnicodeTranslateError", "ValueError", "ZeroDivisionError"
                ]


    # flags
    results = []
    while(len(string) > 0):
        if string[0] == " ":
            results.append(["&nbsp", "SPACE"])
            string = string[1:]

        elif string[0] == "\t":
            results.append(["&nbsp"*3, "TAB"])
            string = string[1:]

        elif string[0] == "\n":
            results.append(["\n", "LINE_JUMP"])
            string = string[1:]

        elif string[0] in punctuation_num:
            results.append([string[0], "PUNCTUATION"])
            string = string[1:]
            

        elif string[0] in keys:
            results.append([string[0], "KEY"])
            string = string[1:]

        
        elif string[0] in operators or string[0] == "#":
            restante, lexeme, denom = op_lexer(string, white, operators)
            results.append([lexeme, denom])
            # print(lexeme, denom)
            string = restante

        elif string[0] in letters:
            restante, lexeme, denom = var_lexer(string, letters, digits, white, keys, operators, reserved)
            results.append([lexeme, denom])
            # print(lexeme, denom)
            string = restante

        else:
            restante, lexeme, denom = num_lexer(string, white, digits, scientific, operators, punctuation_num, close_keys)
            results.append([lexeme, denom])
            # print(lexeme, denom)
            string = restante
    
    print("results = [")
    for r in results:
        print(f"{r},")

    print("]")
    


def main():
    # num_prueba = "-123+4903.456 23490/202 = 444 \n asign = -123.456e-789 \t 3456 // esto es un comentario \n 333"

    lexer("file.py")





if __name__ == '__main__':
    main()

