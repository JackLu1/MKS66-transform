from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
red = [255, 0, 0]
edges = []
transform = new_matrix()

parse_file( 'script', edges, transform, screen, color )

# ===================== testing ========================
#m = []
#add_edge(m, 100, 100, 1, 100, 200, 1)
#add_edge(m, 100, 200, 1, 200, 200, 1)
#add_edge(m, 200, 200, 1, 200, 100, 1)
#add_edge(m, 200, 100, 1, 100, 100, 1)
#print_matrix(m)
#
#center = make_translate(250, 250, 0)
##a = make_translate(120, 0, 0)
#a = make_rotZ(45)
##print_matrix(a)
#
#draw_lines( m, screen, color )
#
#matrix_mult( a, m )
#for i in range(len(m)):
#    temp = m[i]
#    temp = [int(x) for x in temp]
#    m[i] = temp
#
#matrix_mult(center, m)
#
#print_matrix(m)
#draw_lines( m, screen, red )
#display(screen)


