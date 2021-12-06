
CC=g++
CFLAGS=-O2
DEPS=

%.o: %.cpp $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

part1: part1.o
	$(CC) $(CFLAGS) -o part1 part1.o

.PHONY: clean

clean:
	rm part1.o part1
