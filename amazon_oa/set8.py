# https://www.desiqna.in/5061/amazon-oa-coding-questions-and-solutions-set-8-2022

# power: [1,2,6,7]
# armor: 5
def maximumHealth (power, armor):
    health = 0 
    armour_used = False
    for val in power:
        if val >= armor and not armour_used:
            health += val-armor
            armour_used = True
        else:
            health += val

    if not armour_used :
        maximum_power = max(power)
        health -= maximum_power
        armour_used = True

    return health + 1

if __name__ == '__main__':
    power = [1,2,6,7]
    armor = 5
    print(maximumHealth(power, armor))
