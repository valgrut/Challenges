/*
 * Board.cpp
 *
 *  Created on: 1. 9. 2017
 *      Author: valgrut
 */

#include "Board.h"

/*
 *
 */
Board::Board(unsigned int size) : _board(size * size), _gobanSize(size)
{
	for(auto n = 0; n < _board.size(); n++)
	{
		_board[n] = nullptr;
	}
}

/*
 * Destruktor - vycisti hraci plochu
 */
Board::~Board()
{
	for(auto n = 0; n < _board.size(); ++n)
	{
		if(_board[n] == nullptr)
		{
			continue;
		}
		delete _board[n];
	}
	std::cout << "Board by mel byt cisty." << std::endl;
}

/*
 * Vrati ptr na Stone umisteny na x,y
 */
Stone* Board::stoneAt(unsigned int x, unsigned int y)
{
	if(outOfBoard(x, y))
	{
		std::cout << "Out Of Range" << std::endl;
		return nullptr;
	}

	int place = x + y * _gobanSize;
	return _board[place];
}

/*
 * Funkce umisti kamen do hraci plochy.
 */
void Board::placeStoneTo(unsigned int x, unsigned int y)
{
	if(outOfBoard(x, y))
	{
		std::cout << "Out Of Range" << std::endl;
		return;
	}

	int place = get2DPlace(x,y);

	if(_board[place] != nullptr)
	{
		std::cout << "Pozice obsazena" << std::endl;
		return;
	}

	// vlozime kamen na hraci plochu
	_board[place] = new Stone(std::make_pair(x,y));
	_gameHistory.push_back(*_board[place]);

	// ulozime souradnice posledniho polozeneho kamene
	_current = std::make_pair(x,y);

	//pridat kamen do skupiny
	_groups[Group::getCounter()].addStone(*stoneAt(x,y));
	//_groups[Group::getCounter()].setGroupNumber(Group::getCounter());

	// vlevo
	scout(x,y,-1,0);

	// vpravo
	scout(x,y,+1,0);

	// nahore
	scout(x,y,0,-1);

	// dole
	scout(x,y,0,+1);
}

/*
 *
 */
void Board::scout(int x, int y, int xx, int yy)
{
	if(outOfBoard(x + xx,y + yy) == false)
	{
		Stone *near = stoneAt(x + xx,y + yy); //TODO nebo lépe- group???


		// pokud tato pozice neni prazdna
		if(near != nullptr)
		{
			// stejne barvy
			if(stoneAt(x,y)->color() == near->color())
			{
				std::cout << "Stejna barva" << std::endl;

				// pokud je uz soucasti skupiny (Kvuli ruzne zakroucenym tvarum)
				if(groupOfCurrentStone() == near->getBelongingGroup())
				{
					std::cout << "Stejne skupina" << std::endl;
					_groups[groupOfCurrentStone()].setLiberties(_groups[groupOfCurrentStone()].getLiberties() - 1);
					_groups[groupOfCurrentStone()].setLiberties(_groups[groupOfCurrentStone()].getLiberties() - 1);

				}

				// pokud je stejne barvy ALE NENI JESTE soucasti skupiny
				else
				{
					/*
					std::cout << "Jina skupina" << std::endl;
					_groups[groupOfCurrentStone()].setLiberties(_groups[groupOfCurrentStone()].getLiberties() - 1);
					//_groups[near->getBelongingGroup()].setLiberties(_groups[near->getBelongingGroup()].getLiberties() - 1);

					_groups[groupOfCurrentStone()].mergeGroups(_groups[near->getBelongingGroup()]);
					*/

					std::cout << "Jina skupina" << std::endl;
					_groups[groupOfCurrentStone()].mergeGroups(_groups[near->getBelongingGroup()]);

					_groups[groupOfCurrentStone()].setLiberties(_groups[groupOfCurrentStone()].getLiberties() - 2);
					//_groups[near->getBelongingGroup()].setLiberties(_groups[near->getBelongingGroup()].getLiberties() - 1);
				}
			}

			// nepratele
			else
			{
				std::cout << "Jina barva" << std::endl;
				// upravim svobodu sobe
				_groups[groupOfCurrentStone()].setLiberties(_groups[groupOfCurrentStone()].getLiberties() - 1);

				// upravim svobodu nepratelske skupince, ktera uz na plose byla
				_groups[near->getBelongingGroup()].setLiberties(_groups[near->getBelongingGroup()].getLiberties() - 1);

			}
		}
		// tato okolni pozice je prazdna
		else
		{
			return;
		}
	}

	// kraj hraci plochy
	else
	{
		_groups[groupOfCurrentStone()].setLiberties(_groups[groupOfCurrentStone()].getLiberties() - 1);
	}
}

int Board::groupOfCurrentStone()
{
	Stone *s = stoneAt(_current);
	return s->getBelongingGroup();
}

Stone* Board::getCurrentStone()
{
	return _board[get2DPlace(_current)];
}

Stone* Board::stoneAt(std::pair<unsigned int, unsigned int> &pair)
{
	return stoneAt(pair.first, pair.second);
}

/*
 * Odstrani kamen z hraci desky (Dealokace)
 * TODO kamen musi byt odstranen i z prislusne skupiny, do ktere patri
 */
void Board::killStoneAt(unsigned int x, unsigned int y)
{
	if(outOfBoard(x, y))
	{
		std::cout << "Out Of Range" << std::endl;
		return;
	}

	int place = get2DPlace(x,y);

	if(_board[place] != nullptr)
	{
		delete _board[place];
		_board[place] = nullptr;
	}
}

/*
 * Vykresli hraci plochu
 */
void Board::printGoban() const
{
	// TODO Upravit tak, aby to vypisovalo kameny podle skupin.
	int cnt = 0;
	for(auto n = 0; n < _board.size(); ++n)
	{
		if(_board[n] == nullptr || _groups.at(_board[n]->getBelongingGroup()).getLiberties() == 0)
		{
			std::cout << '.';
		}
		else
		{
			// vykreslit pouze skupiny ktere jsou zive
			//std::cerr << _board[n]->getBelongingGroup() << std::endl;

			if(_groups.at(_board[n]->getBelongingGroup()).getLiberties() > 0)
			{
				if(_board[n]->color() == "Black")
					std::cout << 'B';

				if(_board[n]->color() == "White")
					std::cout << 'W';
			}
		}

		if(cnt == _gobanSize-1)
		{
			std::cout << std::endl;
			cnt = 0;
			continue;
		}
		cnt++;
	}
}

/*
 * Testovaci funkce, ktera vypise skupiny a kameny v nich s jejich umistenim
 */
void Board::printGroups() const
{
	for(auto n : _groups)
	{
		// vypiseme pouze aktivni (zive)  skupiny // TODO volitelne
		if(n.second.getLiberties() != 0)
			n.second.printStones();
	}
}

/*
 * Kontrola, jestli kamen nebyl umisten mimo hraci plochu
 */
bool Board::outOfBoard(unsigned int x, unsigned int y) const
{
	return (get2DPlace(x,y)) < _gobanSize*_gobanSize ? false : true;
}

/*
 * Kontrola, jestli kamen nebyl umisten mimo hraci plochu
 */
bool Board::outOfBoard(std::pair<int, int> coord) const
{
	return (get2DPlace(coord.first, coord.second)) < _gobanSize*_gobanSize ? false : true;
}

/*
 * Z 2D souradnice vytvori 1D a vrati ji
 */
int Board::get2DPlace(int x, int y) const
{
	return (x + y * _gobanSize);
}

void Board::printHistory() const
{
	for(auto n : _gameHistory)
	{
		std::cout << n.color() << " " << n.coords().first << " " << n.coords().second << std::endl;
	}
}

int Board::get2DPlace(std::pair<unsigned int,unsigned int> coord) const
{
	return (coord.first + coord.second * _gobanSize);
}
