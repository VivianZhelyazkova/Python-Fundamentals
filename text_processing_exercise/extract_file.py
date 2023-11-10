string = input().split("\\")
file = string[-1]
name, extension = file.split(".")
print(f"File name: {name}\n"
      f"File extension: {extension}")
