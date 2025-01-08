from Peria_Modulo_1 import Talpa_Europaea

# Creazione di un oggetto di tipo Talpa_Europaea()
talpa_1 = Talpa_Europaea('TCCCCATAGAAGATGGTATGCGAATTTTGTACTTGGCCACGGGTG', 'M', 0.7, 5, 7)
# Test del method show() che mostra un oggetto della classe Talpa_Europaea()
talpa_1.show()
# Test del method show_traits() che mostra i tratti espressi da un oggetto della classe Talpa_Europaea()
talpa_1.show_traits()

# ---------------------------------------------------------------------------------------

# Provare ad assegnare anche genomi non conformi
talpa_1 = Talpa_Europaea('TCCCCAT', 'M', 0.7, 10, 7) # --> triggera un ValueError: ERROR! Genome too short
talpa_1 = Talpa_Europaea('TCCCCATAGAAYATGGTATGCGAATTTTGTACTTGGCCACGGGTG', 'M', 0.7, 5, 7) # --> triggera un ValueError: ERROR! Genome base out of the alphabet
talpa_1 = Talpa_Europaea('TCCCCATAGAAYATGGTATGCGAATTTTGTACTTGGCCACGGGTGG', 'M', 0.7, 5, 7) # --> triggera un ValueError: ERROR! Genome length is not mutiple of 3

# Provare ad assegnare un sesso non conforme
talpa_1 = Talpa_Europaea('TCCCCATAGAAYATGGTATGCGAATTTTGTACTTGGCCACGGGTGG', 'Y', 0.7, 5, 7) # --> triggera un ValueError

# ---------------------------------------------------------------------------------------

# Creazione di due talpe che verranno successivamente accoppiate  che hanno genomi che codificano
talpa_1 = Talpa_Europaea('TCCCCATAGAAGATGGTATGCGAATTTTGTACTTGGCCACGGGTG', 'M', 0.8, 5, 7)
talpa_1.show()
talpa_1.show_traits()

talpa_2 = Talpa_Europaea('ATACCTGGGTCGATGCCTCGCGCTTTTCATTAGGATGCCCACAGC', 'F', 0.2, 5, 7)
talpa_2.show()
talpa_2.show_traits()


list_talpa_3 = talpa_1.reproduce(talpa_2)
print(f'{len(list_talpa_3)} talpe figlie create:')
for t in list_talpa_3:
    t.show()
    t.show_traits()



# Creazione di due talpe che verranno successivamente accoppiate  che hanno genomi che non codificano
talpa_1 = Talpa_Europaea('CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC', 'M', 0.8, 5, 7 )
talpa_1.show()
talpa_1.show_traits()

talpa_2 = Talpa_Europaea('GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG', 'F', 0.2, 5, 7)
talpa_2.show()
talpa_2.show_traits()

genome_talpa_3 = talpa_1.create_genome_child(talpa_2)
print(f'Genoma della talpa figlia: {genome_talpa_3}')

genome_talpa_3_mutant = talpa_1.mutation(talpa_2, genome_talpa_3)
print(f'Genoma della talpa figlia dopo mutazione: {genome_talpa_3_mutant}')

list_talpa_3 = talpa_1.reproduce(talpa_2)
print(f'{len(list_talpa_3)} talpe figlie create:')
for t in list_talpa_3:
    t.show()
    t.show_traits()


#esempi di utilizzo della classe Environment
genome_talpa_4 = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
genome_talpa_5 = 'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT'

talpa_4 = Talpa_Europaea (genome_talpa_4, "F", fertility= 0.8, age= 1, generation= 0)
talpa_5 = Talpa_Europaea (genome_talpa_5, "M", fertility= 0.9, age=1, generation= 0)

#creiamo environment
environment = Environment (organisms= [], generations= {}, epochs= 0)

#aggiungiamo alcuni organismi dalla classe rattus norvegicus alla classe environment
environment.add_organism(talpa_4)
environment.add_organism(talpa_5)

environment.oxygen_concentration= 0.05
environment.infant_mortality()

# Crea una lista di organismi e aggiungi all'ambiente
talpa_4 = Talpa_Europaea (genome_talpa_4, sex="F", fertility=0.8, age= 1, generation= 0)
talpa_5 = Talpa_Europaea (genome_talpa_5, sex="M", fertility=0.9, age= 1, generation= 0)
env = Environment(organisms=[talpa_4, talpa_5], generations={}, epochs=0)

# Simulazione per 3 epoche
for epoch in range(3):
    env.update_epoch()  # Aggiorna epoca e fattori ambientali
    env.simulate_epoch()  # Simula l'intera epoca (riproduzione, mortalità, invecchiamento)