import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))

    for i in range(dump):
        box[box.index(max(box))] -= 1
        box[box.index(min(box))] += 1

    box = sorted(box)
    print('#{} {}'.format(tc, box[-1]-box[0]))
