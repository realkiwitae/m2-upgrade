upgradeData = {}

def getData():
    # Load the upgrade data from the file offical_chance_upgrade_fr.txt
    # each lines are in format '{name}+{digit} {chance}'
    # where {name} is the name of the upgrade, {digit} is the digit of the upgrade, and {chance} is the chance of the upgrade
    # return the list of the upgrade data as a dictionary with list of chances floats chance/100
    
    with open("./upgrade/official_chance_upgrade_fr.txt", "r", encoding='utf-8') as file:
        for line in file:
            name, chance = line.split("+")
            name = name.lower()
            chance = chance.split()[1]
            if name not in upgradeData:
                upgradeData[name] = []
            upgradeData[name] += [float(chance) / 100]
    return upgradeData

upgradeData = getData()