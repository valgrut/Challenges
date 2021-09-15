#ifndef BOARD_H
#define BOARD_H

#include <cassert>
#include <iostream>
#include <vector>
#include <string>

#include "Shape.h"

using namespace std;

class Board
{
    public:
        Board(unsigned int x, unsigned int y);
        virtual ~Board();

	   bool checkRow(int i) const;
	   void pushBoardDown(int od, int oKolik);
	   void placeShape(Shape *s);
        Shape *getShape();

        bool collision();

	   void draw() const;
        unsigned int getSizeX() const {return _sizeX;}
        unsigned int getSizeY() const {return _sizeY;}
        void setBoardAt(int y, int x, char c) {_board.at(y).at(x) = c;}

    protected:

    private:
         vector< vector<char> > _board;
         unsigned int _sizeX; //8
         unsigned int _sizeY; //20
};

#endif
