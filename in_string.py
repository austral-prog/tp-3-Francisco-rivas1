def check_vowels():
    if "a" in name:
        print("Contiene a: True")
    else:
        print(False)
    if "e" in name:
        print("Contiene e: True")
    else:
        print(False)
    if "i" in name:
        print("Contiene i: True")
    else:
        print(False)
    if "o" in name:
        print("Contiene o: True")
    else:
        print(False)
    if "u" in name:
        print("Contiene u: True")
    else:
        print(False)

name="Matias"
check_vowels()
nombre="Augusto"
name=nombre.lower()
check_vowels()
    # Código a implementar utilizando input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
