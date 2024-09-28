
# Exemplo de vetor de faturamento diário (pode conter zeros em finais de semana/feriados)
faturamento = [0, 220.5, 180.3, 0, 340.0, 250.0, 0, 0, 430.0, 0, 0, 310.0, 400.5, 0, 0, 190.0, 100.0, 0]

def calcular_faturamento(faturamento):
    # Filtrar os dias sem faturamento (ignorar zeros)
    dias_com_faturamento = [valor for valor in faturamento if valor > 0]

    # Se não houver dias com faturamento, retorna como nulo
    if not dias_com_faturamento:
        return None, None, 0

    # Cálculo do menor e maior faturamento
    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)

    # Cálculo da média anual (ignorando dias sem faturamento)
    media_anual = sum(dias_com_faturamento) / len(dias_com_faturamento)

    # Contar o número de dias com faturamento acima da média
    dias_acima_da_media = sum(1 for valor in dias_com_faturamento if valor > media_anual)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Chamada da função e exibição dos resultados
menor, maior, dias_acima_media = calcular_faturamento(faturamento)
print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
