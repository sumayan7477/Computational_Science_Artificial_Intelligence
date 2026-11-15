import json

def load_animals(filename):
    data=[]
    jsonfile = open(filename , "r")
    data = json.load(jsonfile)
    jsonfile.close()

    return data

def count_species(data):
    species_count = {}

    for animal in data:
        species = animal["species"]

        if species in species_count:
            species_count[species] = species_count[species]+1
        else:
            species_count[species] = 1
    return species_count

def average_age(data):
    if len(data) == 0:
        return 0.0
    else:
        total = 0

        for animal in data:
            total = total + animal["age_years"]

        return total/len(data)

def oldest_animal(data):
    if len(data) == 0:
        return None
    else:
        oldest_name = data[0]["name"]
        highest_age = data[0]["age_years"]

        for animal in data:
            if animal["age_years"]>highest_age:
                highest_age = animal["age_years"]
                oldest_name = animal["name"]
        return oldest_name

def vaccinated_percentage(data):
    if len(data)==0:
        return 0.0
    else:
        vaccinated_count =0
        for animal in data:
            if animal["vaccinated"]==True:
                vaccinated_count += 1
        return (vaccinated_count/len(data))*100

def main():
    animals = load_animals("animals.json")

    species = count_species(animals)
    print(f"Species counts:{species}")

    avg_age = average_age(animals)
    print(f"Average age is {avg_age:.1f} years")

    oldest = oldest_animal(animals)
    print(f"Oldest animal: {oldest}")

    vax_pct = vaccinated_percentage(animals)
    print(f"Vaccinated: {vax_pct:.0f}%")

#main()





















