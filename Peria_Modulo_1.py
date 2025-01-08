import random
from abc import ABC, abstractmethod

class Species(ABC):
    
    # Costruttore della classe Species() definito su 2 attributi: genome e reproduction
    def __init__(self, genome: str, sex: str, fertility: float, age: int, generation: int):
        self.genome = genome
        self.sex = sex
        self.fertility = fertility
        self.age = age
        self.generation = generation

    
    @abstractmethod
    def reproduce(self, mate, environment: dict) -> list:
        pass
    
    @abstractmethod
    def show(self):
        pass      


class Talpa_Europaea(Species):
    
    def __init__(self, genome: str, sex: str, fertility: float, age: int, generation: int):
        # Controllo e assegnazione del genoma. Il controllo viene eseguito sul valore che
        # verrà successivamente assegnato all'attributo self.genome
        self.check_genome(genome)
        # Controllo e assegnazione del sesso. Il controllo viene eseguito sul valore che
        # verrà successivamente assegnato all'attributo self.sex
        self.check_sex(sex)
        super().__init__(genome, sex, fertility, age, generation)
    
    # Definisco adesso l'attributo traits = {} che è condiviso tra tutte le istanze della classe
    # Talpa_Europaea() e che essendo condiviso, non è importante che sia definito in fase di 
    # inizializzazione e quindi non viene messo all'interno dell' __init__()
    traits = {
        'hair': {
            'position': 15, 
            'length': 3, 
            'features': {
                'black': {'genome_fragment': 'AAA', 'dominance': 0.4}, 
                'brown': {'genome_fragment': 'CCT', 'dominance': 0.35},
                'white': {'genome_fragment': 'GTA', 'dominance': 0.25}
            }
        },
        'nose': {
            'position': 25, 
            'length': 2,
            'features': {
                'simple': {'genome_fragment': 'GA', 'dominance': 0.65},
                'starred': {'genome_fragment': 'TT', 'dominance': 0.35}
            }
        }
    }
    
    
    #Definisco adesso l'attributo traits = {} che è condiviso tra tutte le istanze della classe
    # Talpa_Europaea() e che essendo condiviso, non è importante che sia definito in fase di 
    # inizializzazione e quindi non viene messo all'interno dell' __init__()
    environment = {'oxygen': 8}
    
    
    def show(self):
        """Metodo che serve per rappresentare un oggetto della classe Talpa_Europaea()"""
        
        print('='*55)
        print(
            'Object of class Talpa_Europaea()\n',
            f'Genome: {self.genome}\n',
            f'Sex: {self.sex}\n',
            f'Fertility: {self.fertility}'
            )
        print('='*55)
        
    
    def show_traits(self):
        
        """Metodo che serve per stampare i tratti espressi da un oggetto della classe Talpa_Europaea()"""
        print('='*55)
        for key, value in self.traits.items():
            
            pos = value['position']
            l = value['length']
            
            fragment = self.genome[pos:pos+l]
            features = value['features']
            
            showed_feature = '-'*l
            dominance = 0
            for feat in features:
                if features[feat]['genome_fragment'] == fragment:
                    showed_feature = feat
                    dominance = features[feat]['dominance'] 
             
            print(
            f'Trait: {key}\n',
            f'Position in genome: {pos}\n',
            f'Length of trait: {l}\n',
            f'Fragment: {fragment}\n',
            f'Expresses feature: {showed_feature}\n',
            f'Dominance of feature: {dominance}\n',
            )
        print('='*55)
            
        
    def check_genome(self, genome):
        list_valid_bases = ['A', 'C', 'G', 'T', '-']
        for base in genome:
            if base not in list_valid_bases:
                raise ValueError('ERROR! Genome base out of the alphabet')
            if len(genome) < 30:
                raise ValueError('ERROR! Genome too short')
            if len(genome)%3 != 0:
                raise ValueError('ERROR! Genome length is not mutiple of 3')



    def check_sex(self, sex):
        if sex not in ['M', 'F']:
            raise ValueError('ERROR! Sex should be M or F')
        
    
    
    def get_k(self, mate) -> int:
        """
        Calcola il numero di figli k al variare dei fattori ambientali e della fertilità dei genitori
        che sono self e mate, ovvero due oggetti di tipo Talpa_Europaea()
        """
        # Qui non controllo che mate sia un oggetto della classe Talpa_Europaea() ma 
        # solo perché nella mia idea questo metodo get_k() la richiamo solo da dentro
        # il metodo sottostante reproduce(), che all'inizio ha già il controllo che 
        # mate sia un oggetto della classe Talpa_Europaea()
        
        # Determino k a seconda delle condizioni ambientali
        if self.environment['oxygen'] < 5:
            k_result = random.randint(1, 5)
        elif self.environment['oxygen'] < 8:
            k_result = random.randint(2, 7)
        else:
            k_result = random.randint(3, 10) 
        
        
        # Modifico il k appena degterminato alla luce della fertilità dei genitori
        # Basta che uno dei due genitori non sia fertile per azzerare il numero dei figli
        if (self.fertility == 0) or (mate.fertility == 0):
            k_result = 0
        else: # Se entrambi i genitori sono fertili, allora k si amplifica o si smorza a seconda dei valori di fertilità
            k_result = int(k_result*(self.fertility + mate.fertility)) # è come scrivere k *= (self.fertility + mate.fertility) 
        return k_result
    

    def get_random_genome(self):
        """
        Metodo che serve per creare un genoma randomico conforme alle specifiche da usare
        durante la fase di riproduzione
        """
        # Alfabeto di basi su cui creare un genoma randomico
        bases_alphabet = ['A', 'C', 'T', 'G']
        target_len_genome = 45
        random_genome = " " # Inizialmente il genome è una stringa vuota che deve essere estesa

        # Fino a che la lunghezza del random_genome è
        while len(random_genome) < target_len_genome:
            base = random.choice(bases_alphabet)
            random_genome = random_genome + base
        return random_genome


    
    def create_genome_child(self, mate) -> str:
        # Qui non controllo che mate sia un oggetto della classe Talpa_Europaea() ma 
        # solo perché nella mia idea questo metodo get_k() la richiamo solo da dentro
        # il metodo sottostante reproduce(), che all'inizio ha già il controllo che 
        # mate sia un oggetto della classe Talpa_Europaea()
        
        # La nuova generazione ha, base per base, un genoma randomico che non dipende dai genitori
        genome_result =  self.get_random_genome()

        # Fanno eccezione alcune porzioni contigue del genoma, che codificano dei tratti della specie.
        for key, value in self.traits.items():
            
            # Per ogni tratto definisco la posizione e la lunghezza del frammento che lo codifica
            pos = value['position']
            l = value['length']
            # Questi sono i valori che assume un tratto, ad esempio per il tratto "pelo",
            #  queste fetures assumono valore "bianco", "nero" o "marrone"
            features = value['features'] 
            
            # Per il tratto in questa iterazione, cerco la sequenza che codifica ognuna delle features che il 
            # tratto può assumere all'interno del genoma del parent_1 e del genoma del parent_2. Dopo assegno al figlio
            # un genoma nel valore del tratto in questione ha una sequenza di lunghezza l:
            # > ereditatata da parent_1 con probabilità fragment_parent_1
            # > ereditatata da parent_2 con probabilità fragment_parent_2
            # La dominanza è inizializzata a un numero molto piccolo, come 0.001 e il tratto è inizializzato a '-'
            dominance_parent_1, dominance_parent_2 = 0.001, 0.001
            fragment_parent_1, fragment_parent_2 = '-'*l, '-'*l
            
            for feat in features:
                
                if features[feat]['genome_fragment'] == self.genome[pos:pos+l]:
                    dominance_parent_1 = features[feat]['dominance']
                    fragment_parent_1 = features[feat]['genome_fragment']
                    
                elif features[feat]['genome_fragment'] == mate.genome[pos:pos+l]:
                    dominance_parent_2 = features[feat]['dominance']
                    fragment_parent_2 = features[feat]['genome_fragment']
            
            # Se almeno nel parent_1 o nel parent_2 ho trovato il frammento di genoma che codifica per una feature, allora 
            # assegno il frammento al figlio sulla base delle probabilità date dalle dominanze.
            # N.B. Per scelta personale, se il parent_1 ha un frammento che NON codifica per nessuna feature e il parent_2 invece 
            # ha un frammento che codifica per una certa feature, al figlio viene preferibilmente trasferita la feature del parent_2,  
            # ovviamente vale il viceversa. Ecco perché l'inizializzazione di dominance_parent_1 e dominance_parent_2 ha un valore molto basso
            if fragment_parent_1 != '-' or fragment_parent_2 != '-':
                fragment_child = random.choices( [fragment_parent_1, fragment_parent_2], weights = [dominance_parent_1, dominance_parent_2], k = 1 )[0]
            #Se sia il padre hanno dei frammenti che non codificano per nessun feature allora anche il figlio non codificherà
            else:
                fragment_child = fragment_parent_1
            
            # Per ogni tratto vado a modificare la relativa posizione e lunghezza del genoma del child
            genome_result = genome_result[:pos] + fragment_child + genome_result[pos+l:]
            
        return genome_result

    def mutation(self, mate, genome_child) -> str:
        pass
        return genome_child

    # Reproduce è un metodo che chiamo su un oggetto di tipo Talpa_Europaea() e quindi ci metto
    # come primo argomento self.
    # Siccome la riproduzione avviene con un mate, che un'altro oggetto di tipo Talpa_Europaea(),
    # allora mate è il mio secondo parametro.
    # Il terzo parametro è il dizionario con le variabili ambientali.
    # Fuori dalla classe la chiamo con la sintassi: talpa_1.reproduce(talpa_2, dict_environment)
    def reproduce(self, mate) -> list: # il valore di ritorno è una lista di oggetti Talpa_Europaea()
        """
        Questo metodo serve per modellare il meccanismo di riproduzione.
        params: 
        > self --> serve per indicare che reproduce è un metodo di questa classe, ovvero Talpa_Europaea()
        > mate --> deve essere un oggetto della classe Talpa_Europaea(), ha gli stessi attributi di self
        > environment --> per semplicità è solo la concentrazione di ossigeno, come scritto nella traccia. 
                          Quindi ad esempio environment = {'oxygen': 2}
        """
        
        # Controlliamo che mate sia a sua volta un oggetto della classe Talpa_Europaea()
        if not isinstance(mate, Talpa_Europaea):
            raise ValueError('ERROR! You are trying to mate animals of different species')
        
        if self.sex == mate.sex:
            raise ValueError('ERROR! You are trying to mate animals of the same gender')
        
        # Avendo appurato che mate è un oggetto della classe Talpa_Europaea(), posso calcolare
        # quanti figli nasceranno dalla riproduzione di self e mate
        k = self.get_k(mate)
        
        # Inizialmente la lista dei figlioli è vuota, la riempio con un ciclo for e ad ogni iterazione
        # appendo alla lista un nuovo oggetto di tipo Talpa_Europaea()
        list_children = []

        generation_child = max(self.generation, mate.generation) + 1

        for i in range(k):

            # FASE 1: creazione del genoma del figlio
            genome_child = self.create_genome_child(mate)
            
            # FASE 2: mutazione del genoma del figlio
            genome_child = self.mutation(mate, genome_child)
            
            # Il sesso del child è random 50%-50%
            sex_child = random.choice(['M', 'F'])
            
            # La fertilità del child è random compresa tra 0 e 1
            fertility_child = random.random()

            # Età = 0 per i nuovi organismi
            age_child=0

            # Creo child, che è l'oggetto Talpa_Europaea() generato dalla riproduzione
            child = Talpa_Europaea(genome_child, sex_child, fertility_child, age_child, generation_child)
            
            # Appendo la talpa così generata alla lista dei figli
            list_children.append(child)
            
        return list_children


# ===========================================================================================================================
# Classe che rappresenta l'ambiente
class Environment:
    def __init__(self, organisms: list, generations: dict, epochs: int):
        self.organisms = []  # Lista degli organismi
        self.generations = {}  # Dizionario per mappare gli organismi alle loro generazioni
        self.generations_counter = 0 # Contatore delle generaziomi
        self.epochs = 0 # Conta il numero di epoche


    def is_previous_generation(self, organism_a, organism_b):
        """Verifica se l'organismo A appartiene a una generazione precedente a B"""
        return organism_a.generation < organism_b.generation

    def add_organism(self, organism):
        """Aggiunge un organismo all'ambiente e ne traccia la generazione."""
        self.organisms.append(organism)
        print(f"Organism {organism} added to the environment.")


    def update_epoch(self):
        """Aggiorna l'epoca e i fattori ambientali per l'epoca successiva"""
        self.epochs += 1
        self.update_environment_factors()
        self.generations_counter += 1

    def update_environment_factors(self):
        """Aggiorna i fattori ambientali per l'epoca corrente"""
        # Esempio di distribuzioni per i fattori ambientali
        # 1. Concentrazione di ossigeno (distribuzione normale)
        self.oxygen_concentration = random.gauss(0.22, 0.02)
        # 2. Pressione atmosferica (distribuzione esponenziale)
        self.pressure = random.expovariate(1/1013)  # pressione in hPa
        # 3. Temperatura (distribuzione beta)
        self.temperature = random.betavariate(2, 5) * 40 + 270  # temperatura in Kelvin

        print(f"\nEpoca {self.epochs} - Fattori ambientali aggiornati:")
        print(f"Ossigeno: {self.oxygen_concentration: f}")
        print(f"Pressione: {self.pressure: f} hPa")
        print(f"Temperatura: {self.temperature: f} K")

    def simulate_epoch(self):
        """Simula l'intera epoca: riproduzione, mortalità e invecchiamento"""
        print(f"\nSimulazione Epoca {self.epochs}:")
        # 1. Riproduzione
        self.reproduction()
        # 2. Mortalità infantile
        self.infant_mortality()
        # 3. Effetto vecchiaia
        self.aging()

    def reproduction(self):
        """Simula la riproduzione degli organismi in un'epoca."""
        print("Reproduction Phase")
        list_children = []

        random.shuffle(self.organisms)  # Mischia gli organismi per randomizzare le coppie

        # Monogamia: Ogni organismo si accoppia al massimo con un altro
        for i in range(0, len(self.organisms), 2):
            if i + 1 < len(self.organisms):  # Assicura che ci siano due organismi per coppia
                parent_1 = self.organisms[i]
                parent_2 = self.organisms[i+1]

                # Se i due genitori sono di sesso diverso, possono riprodursi
                if parent_1.sex != parent_2.sex:
                    new_children = parent_1.reproduce(parent_2)
                    list_children.extend(new_children)

        # Aggiungi i nuovi figli all'elenco degli organismi
        self.organisms.extend(list_children)
        print(f"{len(list_children)} new organisms born.\n")


    def infant_mortality(self):
        """Gestisce la mortalità infantile in base ai fattori ambientali estremi"""
        if self.oxygen_concentration < 0.1:  # Se l'ossigeno scende sotto il 10%
            death_rate = 0.05  # Probabilità di morte del 5%
            num_infant_deaths = int(len(self.organisms) * death_rate)
            print(f"Mortalità infantile: {num_infant_deaths} organismi morti a causa di basso ossigeno.")
            self.organisms = self.organisms[:-num_infant_deaths]  # Rimuovi gli organismi morti

    def aging(self):
        """Gestisce l'effetto vecchiaia sugli organismi"""
        max_age = 5  # Età massima definita per l'invecchiamento
        self.organisms = [org for org in self.organisms if org.age < max_age]
        for organism in self.organisms:
            organism.age += 1
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