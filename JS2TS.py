import os
import threading
from queue import Queue
from utils.File import read_all_files
from utils.Converter import converter

def convert(q):
    while True:
        file_path = q.get()
        if file_path is None:
            break
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                text = converter(content) 
                try:
                    os.makedirs(f'./output/{os.path.dirname(file_path)}', exist_ok=True)
                    with open(f"./output/{file_path}".replace(".js", ".ts"), 'w') as file:
                        file.write(text)
                        print(f"Converted {file_path} to ./output/{file_path}")
                except IOError as e:
                    print(f"Error when save: {e}")
        except Exception as e:
            print(f"Error when process {file_path}")
        finally:
            q.task_done()

def main():
    input_directory = input("Input directory: ")

    if not os.path.exists(input_directory):
        print(f"{input_directory} doesn't exists!")
        return

    if not os.path.isdir(input_directory):
        print(f"'{input_directory}' is not directory")
        return
    
    files = read_all_files(input_directory)
    q = Queue()
    for file in files:
        q.put(file)

    threads = []
    for i in range(10):
        thread = threading.Thread(target=convert, args=(q,))
        threads.append(thread)
        thread.start()

    q.join()
    for i in range(10):
        q.put(None)
    for thread in threads:
        thread.join()

main()