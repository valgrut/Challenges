#include "Board.h"

Board::Board(unsigned int x, unsigned int y) : _sizeX(x), _sizeY(y)
{
	cout << "Board vytvoren" << endl;

	_board.resize(_sizeY);
     for(unsigned int y = 0; y < _sizeY; y++)
     {
		_board.at(y).resize(_sizeX);
          for(unsigned int x = 0; x < _sizeX; x++)
          {
			//cout << "y " << y << " |x " << x << endl;
			_board.at(y).at(x) = '.';
          }
     }
}

bool Board::collision()
{
	return false;
}

bool Board::checkRow(int i) const
{
	for(auto x = _board.at(i).begin(); x != _board.at(i).end(); ++x)
	{
		if(*x == '.')
		{
			return false;
		}

	}
	return true;
}

void Board::pushBoardDown(int od, int oKolik)
{
	//assert(od < _sizeY-1 && od > 0);
	assert(od < _sizeY && od > 0);
	assert((od + oKolik) < _sizeY);

	for(int o = 0; o < oKolik; o++)
	{
		for(unsigned int y = od+1; y > 0; y--)    // y >= 0
		{
			for(unsigned int x = 0; x < _sizeX; x++)
			{
				_board.at(y).at(x) = _board.at(y-1).at(x);
				//_board.at(y+1).at(x) = _board.at(y).at(x);
				if(y == 1)
				{
					_board.at(y-1).at(x) = '.';
				}
			}
		}
		/*
		for(unsigned int y = od; y > 0; y--)    // y >= 0
		{
			for(unsigned int x = 0; x < _sizeX; x++)
			{
				if(y == 1)
				{
					_board.at(y).at(x) = _board.at(y-1).at(x);
					_board.at(y-1).at(x) = '.';
				}
				else
				{
					//_board.at(y+1).at(x) = _board.at(y).at(x);
					_board.at(y).at(x) = _board.at(y-1).at(x);
				}
			}
		}
		*/
	}
}

void Board::placeShape(Shape *s)
{
	for(auto &sh : s->getShape())
	{
		_board.at(sh.second).at(sh.first) = '0';
	}
}

void Board::draw() const
{
     cout << "***** TETRIS *****" << endl;

     for(int b = 0; b <= _sizeX+1; b++) cout << '#';
	cout << endl;

     for(unsigned int y = 0; y < _sizeY; y++)
     {
		//cout << y;
		cout << '#';
          for(unsigned int x = 0; x < _sizeX; x++)
          {
               cout << _board.at(y).at(x);
          }
		cout << '#';
          cout << endl;
     }

     for(int b = 0; b <= _sizeX+1; b++) cout << '#';
	cout << endl;
}

Board::~Board()
{
}
