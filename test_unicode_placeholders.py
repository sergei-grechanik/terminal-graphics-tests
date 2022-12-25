#!/usr/bin/env python3

import os
import sys
import base64
import urllib.request

rowcolumn_diacritics = ['\U00000305', '\U0000030d', '\U0000030e', '\U00000310',
                        '\U00000312', '\U0000033d', '\U0000033e', '\U0000033f',
                        '\U00000346', '\U0000034a', '\U0000034b', '\U0000034c',
                        '\U00000350', '\U00000351', '\U00000352', '\U00000357',
                        '\U0000035b', '\U00000363', '\U00000364', '\U00000365',
                        '\U00000366', '\U00000367', '\U00000368', '\U00000369',
                        '\U0000036a', '\U0000036b', '\U0000036c', '\U0000036d',
                        '\U0000036e', '\U0000036f', '\U00000483', '\U00000484',
                        '\U00000485', '\U00000486', '\U00000487', '\U00000592',
                        '\U00000593', '\U00000594', '\U00000595', '\U00000597',
                        '\U00000598', '\U00000599', '\U0000059c', '\U0000059d',
                        '\U0000059e', '\U0000059f', '\U000005a0', '\U000005a1',
                        '\U000005a8', '\U000005a9', '\U000005ab', '\U000005ac',
                        '\U000005af', '\U000005c4', '\U00000610', '\U00000611',
                        '\U00000612', '\U00000613', '\U00000614', '\U00000615',
                        '\U00000616', '\U00000617', '\U00000657', '\U00000658',
                        '\U00000659', '\U0000065a', '\U0000065b', '\U0000065d',
                        '\U0000065e', '\U000006d6', '\U000006d7', '\U000006d8',
                        '\U000006d9', '\U000006da', '\U000006db', '\U000006dc',
                        '\U000006df', '\U000006e0', '\U000006e1', '\U000006e2',
                        '\U000006e4', '\U000006e7', '\U000006e8', '\U000006eb',
                        '\U000006ec', '\U00000730', '\U00000732', '\U00000733',
                        '\U00000735', '\U00000736', '\U0000073a', '\U0000073d',
                        '\U0000073f', '\U00000740', '\U00000741', '\U00000743',
                        '\U00000745', '\U00000747', '\U00000749', '\U0000074a',
                        '\U000007eb', '\U000007ec', '\U000007ed', '\U000007ee',
                        '\U000007ef', '\U000007f0', '\U000007f1', '\U000007f3',
                        '\U00000816', '\U00000817', '\U00000818', '\U00000819',
                        '\U0000081b', '\U0000081c', '\U0000081d', '\U0000081e',
                        '\U0000081f', '\U00000820', '\U00000821', '\U00000822',
                        '\U00000823', '\U00000825', '\U00000826', '\U00000827',
                        '\U00000829', '\U0000082a', '\U0000082b', '\U0000082c',
                        '\U0000082d', '\U00000951', '\U00000953', '\U00000954',
                        '\U00000f82', '\U00000f83', '\U00000f86', '\U00000f87',
                        '\U0000135d', '\U0000135e', '\U0000135f', '\U000017dd',
                        '\U0000193a', '\U00001a17', '\U00001a75', '\U00001a76',
                        '\U00001a77', '\U00001a78', '\U00001a79', '\U00001a7a',
                        '\U00001a7b', '\U00001a7c', '\U00001b6b', '\U00001b6d',
                        '\U00001b6e', '\U00001b6f', '\U00001b70', '\U00001b71',
                        '\U00001b72', '\U00001b73', '\U00001cd0', '\U00001cd1',
                        '\U00001cd2', '\U00001cda', '\U00001cdb', '\U00001ce0',
                        '\U00001dc0', '\U00001dc1', '\U00001dc3', '\U00001dc4',
                        '\U00001dc5', '\U00001dc6', '\U00001dc7', '\U00001dc8',
                        '\U00001dc9', '\U00001dcb', '\U00001dcc', '\U00001dd1',
                        '\U00001dd2', '\U00001dd3', '\U00001dd4', '\U00001dd5',
                        '\U00001dd6', '\U00001dd7', '\U00001dd8', '\U00001dd9',
                        '\U00001dda', '\U00001ddb', '\U00001ddc', '\U00001ddd',
                        '\U00001dde', '\U00001ddf', '\U00001de0', '\U00001de1',
                        '\U00001de2', '\U00001de3', '\U00001de4', '\U00001de5',
                        '\U00001de6', '\U00001dfe', '\U000020d0', '\U000020d1',
                        '\U000020d4', '\U000020d5', '\U000020d6', '\U000020d7',
                        '\U000020db', '\U000020dc', '\U000020e1', '\U000020e7',
                        '\U000020e9', '\U000020f0', '\U00002cef', '\U00002cf0',
                        '\U00002cf1', '\U00002de0', '\U00002de1', '\U00002de2',
                        '\U00002de3', '\U00002de4', '\U00002de5', '\U00002de6',
                        '\U00002de7', '\U00002de8', '\U00002de9', '\U00002dea',
                        '\U00002deb', '\U00002dec', '\U00002ded', '\U00002dee',
                        '\U00002def', '\U00002df0', '\U00002df1', '\U00002df2',
                        '\U00002df3', '\U00002df4', '\U00002df5', '\U00002df6',
                        '\U00002df7', '\U00002df8', '\U00002df9', '\U00002dfa',
                        '\U00002dfb', '\U00002dfc', '\U00002dfd', '\U00002dfe',
                        '\U00002dff', '\U0000a66f', '\U0000a67c', '\U0000a67d',
                        '\U0000a6f0', '\U0000a6f1', '\U0000a8e0', '\U0000a8e1',
                        '\U0000a8e2', '\U0000a8e3', '\U0000a8e4', '\U0000a8e5',
                        '\U0000a8e6', '\U0000a8e7', '\U0000a8e8', '\U0000a8e9',
                        '\U0000a8ea', '\U0000a8eb', '\U0000a8ec', '\U0000a8ed',
                        '\U0000a8ee', '\U0000a8ef', '\U0000a8f0', '\U0000a8f1',
                        '\U0000aab0', '\U0000aab2', '\U0000aab3', '\U0000aab7',
                        '\U0000aab8', '\U0000aabe', '\U0000aabf', '\U0000aac1',
                        '\U0000fe20', '\U0000fe21', '\U0000fe22', '\U0000fe23',
                        '\U0000fe24', '\U0000fe25', '\U0000fe26', '\U00010a0f',
                        '\U00010a38', '\U0001d185', '\U0001d186', '\U0001d187',
                        '\U0001d188', '\U0001d189', '\U0001d1aa', '\U0001d1ab',
                        '\U0001d1ac', '\U0001d1ad', '\U0001d242', '\U0001d243',
                        '\U0001d244']  # noqa

inside_tmux = os.environ.get('TMUX') is not None

def start_gr_command():
    if inside_tmux:
        sys.stdout.write('\033Ptmux;\033\033_G')
    else:
        sys.stdout.write('\033_G')

def end_gr_command():
    if inside_tmux:
        sys.stdout.write('\033\033\\\033\\')
    else:
        sys.stdout.write('\033\\')

def upload(filename, image_id):
    start_gr_command()
    sys.stdout.write(f'a=t,f=100,t=f,i={image_id},q=1;')
    sys.stdout.write(base64.b64encode(os.path.realpath(filename).encode('utf-8')).decode('ascii'))
    end_gr_command()

def place(image_id, place_id, r, c):
    start_gr_command()
    if place_id is None:
        sys.stdout.write(f'a=p,U=1,i={image_id},r={r},c={c},q=1;')
    else:
        sys.stdout.write(f'a=p,U=1,i={image_id},p={place_id},r={r},c={c},q=1;')
    end_gr_command()

def placeholder(r=None, c=None):
    sys.stdout.write("\U0010EEEE")
    if r is not None:
        sys.stdout.write(rowcolumn_diacritics[r])
        if c is not None:
            sys.stdout.write(rowcolumn_diacritics[c])

class Cell:
    def __init__(self, image_id, place_id, r, c, bg=None):
        self.image_id = image_id
        self.place_id = place_id
        self.r = r
        self.c = c
        self.bg = bg

class Line:
    def __init__(self, image_id, place_id, r, c, width, bg=None):
        self.image_id = image_id
        self.place_id = place_id
        self.r = r
        self.c = c
        self.width = width
        self.bg = bg

    def draw(self, less_diacritics=False):
        if self.width == 0:
            return
        if self.image_id is not None:
            sys.stdout.write(f"\033[38;5;{self.image_id}m")
        if self.place_id is not None:
            sys.stdout.write(f"\033[58;5;{self.place_id}m")
        if self.bg is not None:
            sys.stdout.write(f"\033[48;5;{self.bg}m")

        if self.image_id is not None:
            if less_diacritics and self.width > 0:
                placeholder(self.r, self.c)
                for i in range(self.width - 1):
                    placeholder()
            else:
                for i in range(self.width):
                    placeholder(self.r, self.c + i)
        else:
            sys.stdout.write(' ' * self.width)

        if self.image_id is not None:
            sys.stdout.write(f"\033[39;m")
        if self.place_id is not None:
            sys.stdout.write(f"\033[59;m")
        if self.bg is not None:
            sys.stdout.write(f"\033[49;m")

    def can_extend(self, cell):
        return self.image_id == cell.image_id and self.place_id == cell.place_id and self.bg == cell.bg and self.c + self.width == cell.c and self.r == cell.r

    def extend(self, cell):
        self.width += 1

class Grid:
    def __init__(self, rows, columns):
        self.grid = [[Cell(None, None, 0, 0) for c in range(columns)] for r in
                     range(rows)]

    def draw(self, less_diacritics=False):
        for row in self.grid:
            current_line = Line(None, None, 0, 0, 0)
            for cell in row:
                if current_line.can_extend(cell):
                    current_line.extend(cell)
                else:
                    current_line.draw(less_diacritics)
                    current_line = Line(cell.image_id, cell.place_id, cell.r,
                                        cell.c, 1, cell.bg)
            current_line.draw(less_diacritics)
            sys.stdout.write('\n')

    def box(self, image_id, place_id, *, y, x, r, c, h, w, bg=None):
        for i in range(h):
            for j in range(w):
                self.grid[y + i][x + j] = Cell(image_id, place_id, r + i, c + j, bg)

def show_multiple_sizes(image_id):
    xsizes = [1, 2, 3, 4, 5, 6, 30]
    ysizes = [1, 2, 3, 4]
    grid = Grid(sum(ysizes), sum(xsizes) + 1)
    place_id = 1
    ystart = 0
    for ys in ysizes:
        xstart = 1
        for xs in xsizes:
            place_id += 1
            place(image_id, place_id, ys, xs)
            grid.box(image_id, place_id, y=ystart, x=xstart, r=0, c=0, h=ys, w=xs, bg=place_id+16)
            xstart += xs
        ystart += ys
    place_id += 1
    place(image_id, place_id, ystart, 1)
    grid.box(image_id, place_id, y=0, x=0, r=0, c=0, h=ystart, w=1, bg=place_id+16)
    grid.draw()

def download_images():
    if not os.path.exists('wikipedia.png'):
        urllib.request.urlretrieve(
            'https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/440px-Wikipedia-logo-v2.svg.png',
            'wikipedia.png')
    if not os.path.exists('transparency.png'):
        urllib.request.urlretrieve(
            'https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png',
            'transparency.png')
    if not os.path.exists('column.png'):
        urllib.request.urlretrieve(
            'https://upload.wikimedia.org/wikipedia/commons/9/95/Column6.png',
            'column.png')
    if not os.path.exists('horizontal.png'):
        urllib.request.urlretrieve(
            'https://upload.wikimedia.org/wikipedia/commons/2/2a/Horizontal_hemiola.png',
            'horizontal.png')
    if not os.path.exists('diagonal.png'):
        urllib.request.urlretrieve(
            'https://upload.wikimedia.org/wikipedia/commons/5/5d/Linear_Graph.png',
            'diagonal.png')

def main():
    tmpdir = f"/tmp/kitty-test-unicode-placeholders-{os.getuid()}"
    os.makedirs(tmpdir, exist_ok=True)
    os.chdir(tmpdir)

    download_images()

    upload('wikipedia.png', 1)
    upload('transparency.png', 2)
    upload('column.png', 3)
    upload('horizontal.png', 4)
    upload('diagonal.png', 5)

    # One image (watch out for artifacts).
    grid = Grid(40, 100)
    place(5, None, 40, 100)
    grid.box(5, None, y=0, x=0, r=0, c=0, h=40, w=100)
    grid.draw()
    print()

    # Show two images side-by-side.
    grid = Grid(5, 20)
    place(1, None, 5, 10)
    place(2, None, 5, 10)
    grid.box(1, None, y=0, x=0, r=0, c=0, h=5, w=10, bg=1)
    grid.box(2, None, y=0, x=10, r=0, c=0, h=5, w=10, bg=2)
    grid.draw()
    print()

    # Show images of different sizes.
    for i in [1, 2, 3, 4]:
        show_multiple_sizes(i)
        print()

    # Overlapping images.
    place(1, 100, 8, 16)
    place(2, 100, 4, 8)
    for less_diacritics in [False, True]:
        grid = Grid(12, 24)
        grid.box(1, None, y=0, x=0, r=0, c=0, h=5, w=10, bg=1)
        grid.box(1, None, y=7, x=14, r=0, c=0, h=5, w=10, bg=2)
        grid.box(2, None, y=0, x=14, r=0, c=0, h=5, w=10, bg=3)
        grid.box(2, None, y=7, x=0, r=0, c=0, h=5, w=10, bg=4)
        grid.box(1, 100, y=2, x=4, r=0, c=0, h=8, w=16, bg=5)
        grid.box(2, 100, y=4, x=8, r=0, c=0, h=4, w=8, bg=6)
        grid.draw(less_diacritics)
        print()

    # Show an hourglass.
    place(1, 101, 10, 20)
    place(2, 101, 10, 20)
    place(3, 101, 10, 20)
    place(4, 101, 10, 20)
    grid = Grid(10, 20)
    for i in range(10):
        grid.box(1, 101, y=i, x=0, r=i, c=0, h=1, w=20, bg=1)
        grid.box(3, 101, y=i, x=i*2+2, r=i, c=i*2+2, h=1, w=20-i*2-2, bg=3)
        grid.box(4, 101, y=i, x=20-i*2, r=i, c=20-i*2, h=1, w=i*2, bg=4)
        if i >= 5:
            grid.box(2, 101, y=i, x=20-i*2, r=i, c=20-i*2, h=1, w=i*4-18, bg=2)
    grid.draw()
    print()

    place(3, 102, 20, 40)
    place(4, 102, 20, 40)

    # Vertical stripes.
    grid = Grid(20, 40)
    for i in range(40):
        if i % 2 == 0:
            grid.box(3, 102, y=0, x=i, r=0, c=i, h=20, w=1, bg=20)
        else:
            grid.box(4, 102, y=0, x=i, r=0, c=i, h=20, w=1, bg=30)
    grid.box(3, 102, y=0, x=0, r=0, c=0, h=2, w=40, bg=20)
    grid.draw()
    print()

    # Horizontal stripes.
    grid = Grid(20, 40)
    for i in range(20):
        if i % 2 == 0:
            grid.box(3, 102, y=i, x=0, r=i, c=0, h=1, w=40, bg=22)
        else:
            grid.box(4, 102, y=i, x=0, r=i, c=0, h=1, w=40, bg=33)
    grid.box(4, 102, y=0, x=0, r=0, c=0, h=20, w=4, bg=33)
    grid.draw()


if __name__ == '__main__':
    main()
