from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('glenda', 7)
restaurante_praca.receber_avaliacao('rhany', 4)
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_mexicano.receber_avaliacao('glenda', 8)
restaurante_mexicano.receber_avaliacao('rhany', 9) 
restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_japones.receber_avaliacao('glenda', 7)
restaurante_japones.receber_avaliacao('rhany', 10)

restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__=='__main__':
    main()
