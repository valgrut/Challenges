#include "Board.h"

Board::Board(std::pair<int,int> size)
{
	_mapsize = size;
	std::cout << "Board vytvoren" << std::endl;

	_board.resize(_mapsize.second);
     for(unsigned int y = 0; y < _mapsize.second; y++)
     {
		_board.at(y).resize(_mapsize.first);
          for(unsigned int x = 0; x < _mapsize.first; x++)
          {
			//std::cout << "y " << y << " |x " << x << std::endl;
			_board.at(y).at(x) = ' ';
          }
     }
}

bool Board::isBlack(int x, int y)
{
	return (_board.at(y).at(x) == '#');
}
bool Board::isBlack(std::pair<int,int> coord)
{
	return (_board.at(coord.second).at(coord.first) == '#');
}
bool Board::isWhite(int x, int y)
{
	return (_board.at(y).at(x) == ' ');
}
bool Board::isWhite(std::pair<int,int> coord)
{
	return (_board.at(coord.second).at(coord.first) == ' ');
}

void Board::invertColor(int x, int y)
{
	if(isWhite(x, y))
	{
		_board.at(y).at(x) = '#';
		return;
	}
	if(isBlack(x, y))
	{
		_board.at(y).at(x) = ' ';
		return;
	}
}

void Board::invertColor(std::pair<int,int> coord)
{
	invertColor(coord.first, coord.second);
}

void Board::draw() const
{
     std::cout << "***** Langton's Ant *****" << std::endl;

     for(int b = 0; b <= _mapsize.first+1; b++) std::cout << '#';
	std::cout << std::endl;

     for(unsigned int y = 0; y < _mapsize.second; y++)
     {
		//std::cout << y;
		std::cout << '#';
          for(unsigned int x = 0; x < _mapsize.first; x++)
          {
               std::cout << _board.at(y).at(x);
          }
		std::cout << '#';
          std::cout << std::endl;
     }

     for(int b = 0; b <= _mapsize.first+1; b++) std::cout << '#';
	std::cout << std::endl;
}

Board::~Board()
{
}
