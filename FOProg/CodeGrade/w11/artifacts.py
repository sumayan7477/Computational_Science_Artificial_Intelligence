def create_artifact(name , year , country):
    artifact = (name , year , country)
    return artifact

def describe_artifact(artifact):
    name = artifact[0]
    year = artifact[1]
    country = artifact[2]

    return f"The {name} was discovered in {year} in {country}"

def find_oldest_artifact(artifacts):
    if len(artifacts)==0:
        return None
    else:
        oldest = artifacts[0]

        for artifact in artifacts:
            if artifact[1] < oldest[1]:
                oldest = artifact
        return oldest

def main():
    artifacts = [
        ("Rosetta Stone", 1799, "Egypt"),
        ("Terracotta Army", 1974, "China"),
        ("Dead Sea Scrolls", -300, "Israel"),
        ("Mona Lisa", 1503, "Italy"),
        create_artifact("Great Wall", -700, "China"),
    ]

    for artifact in artifacts:
        print(describe_artifact(artifact))

    oldest = find_oldest_artifact(artifacts)
    print("\nOldest artifact:")
    print(describe_artifact(oldest))

main()