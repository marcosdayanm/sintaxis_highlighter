# Diccionario de los colores por clase de token
colors = {
        "error": "red",
        "numbers": "blue",
        "operators": "orange",
        "variables": "navy",
        "functions": "olive",
        "reserved": "purple",
        "string": "green",
        "comments": "silver",
        "keys_brackets_punctuation": "brown",
        "format": "black"
    }

    # Diccionario con los colores de cada type de token
color_types = {
        "ERROR": colors["error"],
        "INTEGER": colors["numbers"],
        "REAL": colors["numbers"],
        "ADDITION": colors["operators"],
        "SUBTRACTION": colors["operators"],
        "MULTIPLICATION": colors["operators"],
        "DIVISION": colors["operators"],
        "VARIABLE": colors["variables"],
        "FUNCTION": colors["functions"],
        "ASSIGNMENT": colors["operators"],
        "MODULE": colors["operators"],
        "GREATER": colors["operators"],
        "SMALLER": colors["operators"],
        "INTEGER_DIVISION": colors["operators"],
        "POWER": colors["operators"],
        "RESERVED": colors["reserved"],
        "STRING": colors["string"],
        "COMMENT": colors["comments"],
        "KEY": colors["keys_brackets_punctuation"],
        "PUNCTUATION": colors["keys_brackets_punctuation"],
        "LINE_JUMP": colors["format"],
        "SPACE": colors["format"],
        "TAB": colors["format"]
    }



# Función para generar la guía de colores en el HTML
def color_guide(colors):
    html_guide = "<div><h2>Guía de Colores</h2><ul>"
    for type, color in colors.items():
        html_guide += f'<li><span style="color: {color};">{type.capitalize()}</span></li>'
    html_guide += "</ul></div><hr>"
    return html_guide

# Función para generar el HTML
def html_generator(results, color_types, output_file):
    html_guide = color_guide(colors)
    html_content = "<!DOCTYPE html>\n<html>\n<head>\n<title>Highlighted Code</title>\n</head>\n<body>\n"
    html_content += html_guide
    html_content += "<pre>\n"
    
    for text, type in results:
        color = color_types.get(type, "black") 
        if type == "LINE_JUMP":
            html_content += "<br>"
        elif type == "SPACE":
            html_content += "&nbsp;"
        else:
            html_content += f'<span style="color: {color};">{text}</span>'
    
    html_content += "\n</pre></body>\n</html>"
    # return html_content


    # Se guarda el HTML en un archivo
    with open(output_file, 'w') as file:
        file.write(html_content)


def highlighter(results, file_path):
    html_generator(results, color_types, file_path)
