string = "Olá! você vem sempre aqui?"
nova_string = ' '.join(filter(str.isalnum, string))
print(nova_string)