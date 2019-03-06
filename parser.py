from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):

    # setup cmds
    f = open(fname, 'r')
    
    line = f.readline().rstrip('\n')
    count = 0

    while line:
        print line
        if line == 'line':
            args = f.readline().rstrip('\n').split()
            args = [int(x) for x in args]
            add_edge(points, args[0], args[1], args[2], args[3], args[4], args[5])

            print line

        if line == 'ident':
            ident(transform)

        if line == 'scale':
            args = f.readline().rstrip('\n').split()
            args = [int(x) for x in args]
            s = make_scale( args[0], args[1], args[2])
            matrix_mult(s, transform)
            print line

        if line == 'translate' or line == 'move':
            args = f.readline().rstrip('\n').split()
            args = [int(x) for x in args]
            t = make_translate( args[0], args[1], args[2])
            matrix_mult(t, transform)
            print line

        if line == 'rotate':
            args = f.readline().rstrip('\n').split()
            if args[0] == 'x':
                r = make_rotX( int(args[1]) )
            if args[0] == 'y':
                r = make_rotY( int(args[1]) )
            if args[0] == 'z':
                r = make_rotZ( int(args[1]) )
            matrix_mult(r, transform)
            
            print line

        if line == 'apply':
            matrix_mult(transform, points)
            for row in range( len(points) ):
                for col in range( len(points[0]) ):
                    points[row][col] = int(points[row][col])


        if line == 'display':
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)

        if line == 'save':
            args = f.readline().rstrip('\n').split()
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_extension(screen, args[0])

        if line == 'quit':
            break

        # incremet
        line = f.readline().rstrip('\n') 

    print_matrix(points)

