def calcular_idade_em_anos_meses_dias(idade_em_dias):
    anos = idade_em_dias // 365
    meses = (idade_em_dias % 365) // 30
    dias = (idade_em_dias % 365) % 30

    return anos, meses, dias

def main():
    # Solicita a idade em dias
    idade_em_dias = int(input("Digite a idade em dias: "))

    # Calcula a idade em anos, meses e dias
    anos, meses, dias = calcular_idade_em_anos_meses_dias(idade_em_dias)

    # Exibe o resultado
    print(f"A idade é: {anos} anos, {meses} meses e {dias} dias.")

if __name__ == "__main__":
    main()
