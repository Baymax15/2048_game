line = '-' * 30

board = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]]
size = 3

matrix = [ [ x[i] for x in board ] for i in range(size)]

print(matrix)


# matrix = []
# for i in range(len(board[0])):
#   temp = []
#   for x in board:
#     temp.append(x)
#   matrix.append(temp)

## here, since its a square matrix, and we know the size,
## we use size instead of len(board[0]), which is column count or width of the matrix

print(line)
# for i in range(10):
#   print(i)

## is same as

[print(i) for i in range(10)]

## but it also returns a list, which we ignore, this is a hack of list comprehension

## [expression for item in list if condition]
print(line)

x = [i for i in range(10) if i%2==0]
## [0, 2, 4, 6, 8]

name = 'united states of america'
cap = [w[0].upper() for w in name.split() if w not in ['in', 'of']]
print(cap)
## ['U', 'S', 'A']

## this may seem complicated but all it does is..
## for w in name.split()
##    splits the name into words, itrates with variable as w
## if w not in [...]
##    condition to avoid 'in' and 'of' or such words
## w[0].upper()
##    takes first character and gets uppercase of it
## ...and wraps all results into a list.

# cap = []
# for w in name.split():
#   if w not in ['in', 'of']:
#     cap.append(w[0].upper())
#     # or cap += w[0].upper() if cap is string

## ps:'.'.join(cap) to make it into string.