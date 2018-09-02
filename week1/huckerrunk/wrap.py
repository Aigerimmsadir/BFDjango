import textwrap
def wrap(string, max_width):
    return textwrap.fill(string,max_width)
s=input();
w = int(input())
print(wrap(s,w))