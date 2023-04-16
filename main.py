

def split(number):
    ##################################################
    # Code your program here
    ##################################################
    pivot = number[len(number)-1]
    left = [v for v in number if v < pivot]
    right = [v for v in number if v > pivot]

    for i, v in enumerate(left):
        number[i] = v
    pidx = i+1
    number[pidx] = pivot
    for i, v in enumerate(right):
        number[pidx+i+1] = v


def main():
    number = list(map(int, input().split()))
    split(number)
    print(number)


if __name__ == '__main__':
    main()
