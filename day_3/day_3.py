def process_data(sample: str) -> list:
    result = []
    items = [s for s in sample.strip().split("\n")]
    for i in items:
        first_compartment, second_compartement = i[:len(i)//2], i[len(i)//2:]
        result.append([first_compartment, second_compartement])

    return result
