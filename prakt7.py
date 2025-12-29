def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except Exception as e:
        print(f"File {file_name} wasn't opened! Error: {e}")
        return None
    else:
        print(f"File {file_name} was opened!")
        return file

file1_name = "TF26_1.txt"
file2_name = "TF26_2.txt"

# a) Створення TF26_1.txt
file_1_w = Open(file1_name, "w")
if file_1_w is not None:
    lines = [
        "HELLO World",
        "Python PROGRAMMING",
        "FILE Handling EXAMPLE",
        "Text FILES in PYTHON",
        "DATA Processing"
    ]
    for line in lines:
        file_1_w.write(line + "\n")
    print(f"Information was successfully added to {file1_name}!")
    file_1_w.close()
    print(f"File {file1_name} was closed!")

# b) Читання TF26_1.txt, перетворення великих літер на малі і запис у TF26_2.txt
file_1_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_1_r is not None and file_2_w is not None:
    for line in file_1_r:
        file_2_w.write(line.lower())
    file_1_r.close()
    file_2_w.close()
    print(f"File {file2_name} was created with lowercase letters!")

# c) Читання TF26_2.txt і друк по рядках
file_2_r = Open(file2_name, "r")
if file_2_r is not None:
    print("\nContent of TF26_2.txt:")
    for line in file_2_r:
        print(line.strip())  # strip() прибирає символ переносу рядка
    file_2_r.close()
    print(f"File {file2_name} was closed!")