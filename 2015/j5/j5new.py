# for i in range(1, 7):
#     for j in range(1, 7):
#         if j >= i and i + j == 6:
#             print(i, j)
        # for h in range(1, 9):
        #     for t in range(1, 9):
import itertools, sys
pieces = int(sys.stdin.readline())
people = int(sys.stdin.readline())

main = list(i for i in itertools.combinations_with_replacement(range(1, pieces - (people - 2)), people) if sum(i) == pieces)
count = 0


print(len(main))
