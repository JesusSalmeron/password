import random
from werkzeug.security import generate_password_hash

minus = "abcdefghijklmnopqrstuvvxyz"
mayus = minus.upper()
numeros="1234567890"
simbolos="!@·$%&/()=?¿"

base = minus + mayus + numeros + simbolos

longitud = 12

for _ in range(10):
    muestra = random.sample(base,longitud)
    password = "".join(muestra)
    password_encriptado = generate_password_hash(password)
    print("{} => {}".format(password, password_encriptado))


