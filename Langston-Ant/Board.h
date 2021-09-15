#ifndef BOARD_H
#define BOARD_H

#include <cassert>
#include <iostream>
#include <vector>
#include <string>

#include "Ant.h"

class Board
{
    public:
        Board(std::pair<int,int> size);
        virtual ~Board();

	   void draw() const;
        unsigned int getSizeX() const {return _mapsize.first;}
        unsigned int getSizeY() const {return _mapsize.second;}
        void setBoardAt(int y, int x, char c) {_board.at(y).at(x) = c;}
        void setBoardAt(std::pair<int,int> coord, char c) {_board.at(coord.second).at(coord.first) = c;}
        void invertColor(int x, int y);
        void invertColor(std::pair<int,int> coord);
        bool isBlack(int x, int y);
        bool isBlack(std::pair<int,int> coord);
        bool isWhite(int x, int y);
        bool isWhite(std::pair<int,int> coord);

    protected:

    private:
         std::vector< std::vector<char> > _board;
         std::pair<int,int> _mapsize;
};

#endif
