'''A linguagem python tem construções que nos permitem interagir com informação guardada na grande rede global
que é a web. Módulo urllib.request()

O conteúdo que é lido pode ser salvo localmente e guardado com extensão html.
'''

import urllib.request

meu_sitio = urllib.request.urlopen("https://github.com/fegastal/cap7-ficheiros")
meus_bytes = meu_sitio.read()
minha_cadeia = meus_bytes.decode("utf8")
meu_sitio.close()

novo_fich = open ('/Users/fernandagastal/urlteste.html', 'w')
nova_fich.write(minha_cadeia)
novo_fich.close()

