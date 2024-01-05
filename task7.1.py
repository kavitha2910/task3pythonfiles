def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("Content of", file_name, ":")
            print(content)
    except FileNotFoundError:
        print("File not found.")
file_name = 'data.txt'  
read_file(file_name)
