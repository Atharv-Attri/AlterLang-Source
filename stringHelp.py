
def count(item, group) -> int:
    count = 0
    for i in group:
        if i == item:
            count += 1
    return count

def position(item, group) -> list:
    positions = []
    for x, i in enumerate(group):
        if i == item:
            positions.append(x)
    return positions