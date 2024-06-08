import os, time, multiprocessing
from concurrent.futures import ThreadPoolExecutor
from lexer import lexer
from LexerToHTML import highlighter


# Éste método itera sobre el path relativo al propio archivo de python que se le es pasado, y cada vez que encuentra un archivo .py, lo añade a una lista, pero cada vez que encuentra un folder, se vuelve a llamar recursivamente con el path del folder, para en cunato ya no encunetre mas folders y se hayan acabado de registrar todos los folders de las llamadas recursivas
def list_py_files(directory):
    files = []
    for name in os.listdir(directory):
        full_path = os.path.join(directory, name)
        if name.endswith(".py") == False and os.path.isdir(full_path) == False:
            continue

        if os.path.isfile(full_path):
            files.append(full_path)
        elif os.path.isdir(full_path):
            files.extend(list_py_files(full_path)) 
    return files


# función que maneja el flujo de hacer el lexing de un archivo, luego pasar los resultados a la fnción que genera el html y crear el path del archivo para que se guarde el archivo html, si es que no existe el folder, se crea
def lexing_process(file):
    results = lexer(file)
    output = file.replace("input", "output").replace(".py", ".html")
    os.makedirs(os.path.dirname(output), exist_ok=True)
    highlighter(results, output)


# Ésta fdunción simplemente hace un for loop sobre la lista de rutas de archivos .py y en cada uno ejecuta la función del flujo del lexer
def linear_lexing(files_list):
    ti = time.time()
    for file in files_list:
        lexing_process(file)
    tf = time.time()

    return tf - ti


# Ésta función usa un pool de procesos de la librería multiprocessing, como funciona es que se le pasa el número de cores que tiene la computadora y en base a ella, va generando procesos para ejecutar la función que se le pasa, y ésta función va administrando sola cuando se liberan los procesos y la asignación de nuevos procesos

# Docs: https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.pool
def parallel_lexing(files_list):
    ti = time.time()
    
    num_cores = multiprocessing.cpu_count()
    with multiprocessing.Pool(num_cores) as pool:
        pool.map(lexing_process, files_list)

    tf = time.time()
    return tf - ti


# Ésta función usa un pool de hilos de la librería concurrent.futures, como funciona es que se le pasa el número de hilos que se quieren usar y en base a ella, va generando hilos para ejecutar la función que se le pasa, y ésta función va administrando sola cuando se liberan los hilos y la asignación de nuevos hilos
def threads_lexing(files_list):
    ti = time.time()

    with ThreadPoolExecutor(max_workers=40) as executor:
        executor.map(lexing_process, files_list)

    tf = time.time()
    return tf - ti





def main():
    files_list = list_py_files("input")
    print("Total files:", len(files_list))
    linear_lexing_time = linear_lexing(files_list)
    print(f"Linear lexing time: {linear_lexing_time}")

    parallel_lexing_time = parallel_lexing(files_list)
    print(f"Parallel lexing time: {parallel_lexing_time}")

    threads_lexing_time = threads_lexing(files_list)
    print(f"Threads lexing time: {threads_lexing_time}")


if __name__ == "__main__":
    main()