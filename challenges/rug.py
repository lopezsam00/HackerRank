# Enter your code here. Read input from STDIN. Print output to STDOUT
# n, m = input().split()
n=7
m=27
height = int(n)
width = int(m)
t = ".|."
o = "-"
half_height = int((height-1)/2)
ts = 1
for i in range(half_height):
    t_length = (ts)*3
    dashes = width-t_length
    one_side_dash = int(dashes/2)
    print(f'{o*one_side_dash}{t*(ts)}{o*one_side_dash}')
    ts+=2
one_welcome = int((width-len("WELCOME"))/2)
print(f'{o*one_welcome}WELCOME{o*one_welcome}')
for i in range(half_height):
    ts-=2
    t_length = (ts)*3
    dashes = width-t_length
    one_side_dash = int(dashes/2)
    print(f'{o*one_side_dash}{t*(ts)}{o*one_side_dash}')