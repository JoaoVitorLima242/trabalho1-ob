from Desktop import Desktop
from Notebook import Notebook

d1 = Desktop("Mac", "Space Gray", 10000.00, '100hz')
n1 = Notebook("Lenovo t14", "Preto", 6000.00, '12h30min')

print('-------------')
d1.getInformacoes()
d1.cadastrar()
print('-------------')
n1.getInformacoes()
n1.cadastrar()
print('-------------')
