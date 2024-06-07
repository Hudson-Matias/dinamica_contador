# Validação do numero primo
def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Contador para o número
def contador_incremental(max_value=21):
    acumulado = 0
    click = 1

    while acumulado < max_value:
        acumulado += click
        print(f"Clique {click}: Acumulado = {acumulado}")
        if primo(acumulado):
            print(f"{acumulado} é um número primo!")
        click += 1

    while acumulado < max_value + 5:
        acumulado += 1
        print(f"Clique {click}: Acumulado = {acumulado}")
        if primo(acumulado):
            print(f"{acumulado} é um número primo!")
        click += 1

contador_incremental()
