# Diccionario de los colores por clase de token
colors = {
    "error": "red",
    "numeros": "blue",
    "operadores": "orange",
    "variables": "purple",
    "string": "green",
    "comentarios": "gray",
    "llaves_corchetes": "brown",
    "formato": "black"
}

# Diccionario con los colores de cada tipo de token
tipo_colores = {
    "ERROR": colors["error"],
    "INTEGER": colors["numeros"],
    "REAL": colors["numeros"],
    "ADDITION": colors["operadores"],
    "SUBTRACTION": colors["operadores"],
    "MULTIPLICATION": colors["operadores"],
    "DIVISION": colors["operadores"],
    "ASSIGNMENT": colors["operadores"],
    "MODULE": colors["operadores"],
    "INTEGER_DIVISION": colors["operadores"],
    "POWER": colors["operadores"],
    "RESERVED": colors["variables"],
    "STRING": colors["string"],
    "COMMENT": colors["comentarios"],
    "KEY": colors["llaves_corchetes"],
    "PUNCTUATION": colors["llaves_corchetes"],
    "LINE_JUMP": colors["formato"],
    "SPACE": colors["formato"],
    "TAB": colors["formato"]
}

# Función para generar la guía de colores en el HTML
def guiaColores(colors):
    guia_html = "<div><h2>Guía de Colores</h2><ul>"
    for tipo, color in colors.items():
        guia_html += f'<li><span style="color: {color};">{tipo.capitalize()}</span>: {tipo.capitalize()}</li>'
    guia_html += "</ul></div><hr>"
    return guia_html

# Función para generar el HTML
def generarHtml(results, tipo_colores):
    guia_html = guiaColores(colors)
    html_content = "<!DOCTYPE html>\n<html>\n<head>\n<title>Highlighted Code</title>\n</head>\n<body>\n"
    html_content += guia_html
    html_content += "<pre>\n"
    
    for text, tipo in results:
        color = tipo_colores.get(tipo, "black") 
        if tipo == "LINE_JUMP":
            html_content += "<br>"
        elif tipo == "SPACE":
            html_content += "&nbsp;"
        else:
            html_content += f'<span style="color: {color};">{text}</span>'
    
    html_content += "\n</pre></body>\n</html>"
    return html_content

# La matriz de matrices `results`
results = [
    ['\n', 'LINE_JUMP'],
    ['for', 'RESERVED'],
    ['&nbsp', 'SPACE'],
    ['i', 'VARIABLE'],
    ['&nbsp', 'SPACE'],
    ['in', 'RESERVED'],
    ['&nbsp', 'SPACE'],
    ['range', 'RESERVED'],
    ['(', 'KEY'],
    ['1', 'INTEGER'],
    [',', 'PUNCTUATION'],
    ['&nbsp', 'SPACE'],
    ['101', 'INTEGER'],
    [')', 'KEY'],
    [':', 'PUNCTUATION'],
    ['&nbsp', 'SPACE'],
    ['# se crea un for que va de 1 a 100', 'COMMENT'],
    ['\n', 'LINE_JUMP'],
    ['&nbsp', 'SPACE'],
    ['&nbsp', 'SPACE'],
    ['&nbsp', 'SPACE'],
    ['&nbsp', 'SPACE'],
    ['if', 'RESERVED'],
    ['&nbsp', 'SPACE'],
    ['i', 'VARIABLE'],
    ['&nbsp', 'SPACE'],
    ['%', 'MODULE'],
    ['&nbsp', 'SPACE'],
    ['2', 'INTEGER'],
    ['&nbsp', 'SPACE'],
    ['=', 'ASSIGNMENT'],
    ['=', 'ASSIGNMENT'],
    ['&nbsp', 'SPACE'],
    ['0', 'INTEGER'],
    [':', 'PUNCTUATION'],
    ['&nbsp', 'SPACE'],
    ['# se crea un if que verifica si el numero es par', 'COMMENT'],
    ['\n', 'LINE_JUMP'],
    ['&nbsp', 'SPACE'],
    ['&nbsp', 'SPACE'],
    ['&nbsp', 'SPACE'],
    ['&nbsp', 'SPACE'],
    ['&nbsp', 'SPACE'],
    ['&nbsp', 'SPACE'],
    ['&nbsp', 'SPACE'],
    ['&nbsp', 'SPACE'],
    ['print', 'RESERVED'],
    ['(', 'KEY'],
    ['i', 'VARIABLE'],
    [')', 'KEY'],
    ['&nbsp', 'SPACE'],
    ['# se imprime el numero par', 'COMMENT'],
    ['\n', 'LINE_JUMP'],
    ['\n', 'LINE_JUMP'],
    ['\n', 'LINE_JUMP'],
    ['&nbsp', 'SPACE'],
]

# Se genera el HTML
html_resultado = generarHtml(results, tipo_colores)

# Se guarda el HTML en un archivo
file_path = 'SintaxisHighlighter.html'
with open(file_path, 'w') as file:
    file.write(html_resultado)
