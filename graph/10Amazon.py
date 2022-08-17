from cmath import inf


def server(computes):
    prev = -inf
    computeAdded = 0
    for compute in computes:
        compute += computeAdded
        if compute < prev:
            computeAdded += (prev-compute)
    return computeAdded


if __name__ == '__main__':
    power = [3,4,1,6,2]
    print(server(power))