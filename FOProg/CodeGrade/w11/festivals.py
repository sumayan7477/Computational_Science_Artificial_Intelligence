import numpy as np

def read_performances():
    performances = []
    while True:
        try:
            count = int(input("How many performances? "))
            if count <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter an integer.")

    for i in range(count):
        print(f"\n Performance {i+1}")
        artist = input("Artist: ").strip()
        stage = input("Stage: ").strip()

        performance = (artist.title(), stage)
        performances.append(performance)

    return performances

def analyze_performances(performances):
    artists =set()
    stages = set()

    main_stage = set()
    acoustic_stage =set()

    for performance in performances:
        artists.add(performance[0])
        stages.add(performance[1])

        if performance[1] == "Main Stage":
            main_stage.add(performance[0])
        if performance[1]== "Acoustic Stage":
            acoustic_stage.add(performance[0])
    return artists ,stages, main_stage, acoustic_stage


def create_stage_array(stages):
    stage_tuple = tuple(sorted(stages))
    stage_array = np.array(stage_tuple)
    return stage_tuple , stage_array

def print_report(performances , artists , stages, stage_tuple, stage_array, main_stage, acoustic_stage):
    both = main_stage & acoustic_stage
    print()
    print("="*45)
    print("MUSIC FESTIVAL REPORT")
    print("=" * 45)
    
    print("\n Unique artists")
    print(artists)

    print("\n Unique stages")
    print(stages)
    
    print("\n Sorted stage tuple")
    print(stage_tuple)

    print("\n Stage NumPy array")
    print(stage_array)

    print("\n Artists performing on both stages")
    print(both)

    print("\n statistics")
    print(f"Performances : {len(performances)}")
    print(f"Artists      : {len(artists)}")
    print(f"Stages       : {len(stages)}")

def main():
    performances = read_performances()
    artists , stages , main_stage , acoustic_stage = analyze_performances(performances)
    stage_tuple, stage_array = create_stage_array(stages)
    print_report(performances, artists, stages, stage_tuple, stage_array, main_stage, acoustic_stage,)

    
    



























    
