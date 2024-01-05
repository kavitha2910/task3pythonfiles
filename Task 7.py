from datetime import datetime

def createtimestamp_file():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    print("Current date & time : ", current_datetime)
    str_current_datetime = str(current_datetime)
    file_name = str_current_datetime + ".txt"
    file = open(file_name, 'w')

    print("File created : ", file.name)
    file.close()
createtimestamp_file()