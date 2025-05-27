precocapalivro = 24.95
precocapalivrodesconto = precocapalivro - (precocapalivro*0.40)
custofreteprimeiroexemplar = precocapalivrodesconto + 3.00
custofreterestanteexemplares = precocapalivrodesconto + 0.75
custototalatacado = custofreteprimeiroexemplar + (custofreterestanteexemplares * 59)

print(f"o preço total de atacado para 60 exemplares é de: ", custototalatacado)