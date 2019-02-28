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

m = new_matrix()
s = make_scale(2, 1, 1)

add_edge(m, 100, 100, 1, 200, 200, 1)
add_edge(m, 200, 200, 1, 300, 100, 1)
add_edge(m, 300, 100, 1, 100, 100, 1)

draw_lines( m, screen, color )
matrix_mult( s, m )
draw_lines( m, screen, red )
display(screen)


