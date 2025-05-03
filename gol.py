import random
elenco = ['centroavante','ponta-esquerda', 'ponta-direita','meia-atacante','meia-central','volante','lateral-esquerdo','lateral-direito','zagueiro-esquerda','zagueiro-direita','goleiro']
quem_fez_gol = [0.4, 0.25,0.25,0.2,0.1,0.05,0.05,0.05,0.02,0.02,0.001]

placar1 = 0 # Placares dos respectivos times 
placar2 = 0

for _ in range(11): # Repetir por Onze vezes se tando a escolha do time mandante e visitante  forem verdadeiras. Se sim os valores dos seus respectivos placares iram mudar, se não ira terminar o looping e mostrar o placar final

    teve_gol2 = random.choices([True, False], weights=[0.5,0.5], k=1)[0]
    teve_gol_ad = random.choices([True, False], weights=[0.5,0.5], k=1)[0]
    if teve_gol2:
        jogador_gol = random.choices(elenco, weights=quem_fez_gol, k=1)[0]
        placar1 += 1
        print(random.choices(elenco, weights=quem_fez_gol, k=1)[0])
    if teve_gol_ad:
        jogador_gol = random.choices(elenco, weights=quem_fez_gol, k=1)[0]
        placar2 += 1
        print(random.choices(elenco, weights=quem_fez_gol, k=1)[0])

print(f'Placar final: {placar1}x{placar2}')
            




    
