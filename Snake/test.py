from curses import *
import time
from collections import deque
from random import randrange as R
N, W, S, E = z = 119, 97, 115, 100
t = tuple
u = 0, 0


def m(s):
    a = lambda coords, window, char: window.addch(coords[0], coords[1], char)
    q = lambda: (R(L-2), R(C-2))
    L, C = s.getmaxyx()
    curs_set(0)
    s.nodelay(1)
    s.border()
    s.refresh()
    r = newwin(L-2, C-2, 1, 1)
    n = deque()
    y, x = [L-2, 0]
    d = N
    n.append(u)
    c = N
    p = q()
    a(p, r, N)
    a(u, s, 48)
    while 1:
        if c in z:
            d = c
        if d == N:
            y -= 1
        if d == S:
            y += 1
        if d == W:
            x -= 1
        if d == E:
            x += 1
        l = n.pop()
        if (y, x) in n:
            return
        if (y, x) == p:
            p = q()
            a(p, r, N)
            n.append(l)
            s.addstr(0, 0, str(len(n)))
        n.appendleft((y, x))
        a((y, x), r, S)
        a(l, r, 32)
        r.refresh()
        time.sleep(.2)
        c = s.getch()


wrapper(m)
