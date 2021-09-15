SHELL=/bin/sh
CC=g++
FLAGS=-std=c++14 -Weffc++ -Wall -Wextra
COMMAND=$(CC) -c $<

main: main.o Board.o Shape.o Game.o
	$(CC) $(FLAGS) $^ -o $@

main.o: main.cpp
	$(COMMAND)

Board.o: Board.cpp Board.h
	$(COMMAND)

Shape.o: Shape.cpp Shape.h
	$(COMMAND)

Game.o: Game.cpp Game.h
	$(COMMAND)

clean:
	rm *.o
