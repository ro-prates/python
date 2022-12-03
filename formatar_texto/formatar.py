texto = open('entrada.txt', 'r', encoding="utf8")
final = ''
for linha in texto:
    final += linha

texto.close()

sim = final.replace('\n', ' ')
arquivo = open('saida.txt', 'w')
arquivo.write(sim)
arquivo.close()