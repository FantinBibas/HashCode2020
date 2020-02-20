./main.py inputs/a_example.txt > outputs/a.txt &
./main.py inputs/b_read_on.txt > outputs/b.txt &
./main.py inputs/c_incunabula.txt > outputs/c.txt &
./main.py inputs/d_tough_choices.txt > outputs/d2.txt & 
./main.py inputs/e_so_many_books.txt > outputs/e.txt &
./main.py inputs/f_libraries_of_the_world.txt > outputs/f.txt &

zip outputs/aled.zip *.py
