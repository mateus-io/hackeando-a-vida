NUMBER_OF_REPETITIONS_SUPER_EASY_LEVEL = 15
NUMBER_OF_REPETITIONS_EASY_LEVEL = 12
NUMBER_OF_REPETITIONS_MEDIUM_LEVEL = 10
NUMBER_OF_REPETITIONS_HARD_LEVEL = 8
NUMBER_OF_REPETITIONS_SUPER_HARD_LEVEL = 6

def descansar():
    print("\n\nDescansando ----------------------------------\n\n")

def elevacao_lateral_maquina(starting_weight):
    print("\nExercício - Elevação Lateral Máquina\n")
    weight = starting_weight
    repetitions_levels = [NUMBER_OF_REPETITIONS_SUPER_EASY_LEVEL, NUMBER_OF_REPETITIONS_EASY_LEVEL, NUMBER_OF_REPETITIONS_MEDIUM_LEVEL, NUMBER_OF_REPETITIONS_HARD_LEVEL]
    for serie in range(4):
        number_of_repetitions = repetitions_levels[serie]
        print(f"Executando {serie + 1}ª série de elevação lateral máquina com {weight}kg de peso e {number_of_repetitions} repetições!")
        weight += 5
        descansar()

def elevacao_lateral_halter(starting_weight):
    print("\nExercício - Elevação Lateral Halter\n")
    weight = starting_weight
    number_of_repetitions = NUMBER_OF_REPETITIONS_MEDIUM_LEVEL

    for serie in range(4):
        micro_serie = 1
        if serie % 2 == 0:
            for micro_serie in range(3):
                print(f"Executando {serie + 1}ª/{micro_serie + 1} série de elevação lateral halter com {weight}kg de peso e {number_of_repetitions} repetições!")
                weight += 2
        else:
            for micro_serie in range(3):
                weight -= 2
                print(f"Executando {serie + 1}ª/{micro_serie + 1} série de elevação lateral halter com {weight}kg de peso e {number_of_repetitions} repetições!")
        descansar()

def desenvolvimento_maquina(starting_weight):
    print("\nExercício - Desenvolvimento Máquina\n")
    weight = starting_weight
    repetitions_levels = [NUMBER_OF_REPETITIONS_EASY_LEVEL, NUMBER_OF_REPETITIONS_MEDIUM_LEVEL, NUMBER_OF_REPETITIONS_HARD_LEVEL, NUMBER_OF_REPETITIONS_SUPER_HARD_LEVEL]
    for serie in range(4):
        number_of_repetitions = repetitions_levels[serie]
        print(f"Executando {serie + 1}ª série de desenvolvimento máquina com {weight}kg de peso e {number_of_repetitions} repetições!")
        weight += 5
        descansar()

def elevacao_frontal(starting_weight):
    print("\nExercício - Elevação Frontal\n")
    weight = starting_weight
    repetitions_levels = [NUMBER_OF_REPETITIONS_SUPER_EASY_LEVEL, NUMBER_OF_REPETITIONS_MEDIUM_LEVEL, NUMBER_OF_REPETITIONS_MEDIUM_LEVEL, NUMBER_OF_REPETITIONS_MEDIUM_LEVEL]
    for serie in range(4):
        number_of_repetitions = repetitions_levels[serie]
        print(f"Executando {serie + 1}ª série de elevação frontal com {weight}kg de peso e {number_of_repetitions} repetições!")
        
        if serie == 0:
            weight += 4
        descansar()

def crucifixo_inverso(starting_weight):
    print("\nExercício - Crucifixo Inverso \n")
    weight = starting_weight
    repetitions_levels = [NUMBER_OF_REPETITIONS_EASY_LEVEL, NUMBER_OF_REPETITIONS_EASY_LEVEL, NUMBER_OF_REPETITIONS_EASY_LEVEL, NUMBER_OF_REPETITIONS_EASY_LEVEL]
    for serie in range(4):
        number_of_repetitions = repetitions_levels[serie]
        print(f"Executando {serie + 1}ª série de crucifixo inverso com {weight}kg de peso e {number_of_repetitions} repetições!")
        descansar()

def treino_de_ombro():
    elevacao_lateral_maquina(10)
    elevacao_lateral_halter(6)
    desenvolvimento_maquina(15)
    elevacao_frontal(10)
    crucifixo_inverso(6)

treino_de_ombro()