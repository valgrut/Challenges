/*
 * Stone.cpp
 *
 *  Created on: 1. 9. 2017
 *      Author: valgrut
 */

#include "Stone.h"

/*
 *
 */
Stone::Stone() : _coord(std::make_pair(0,0)), _inGroup(0), _color("Black")
{
	++_count;

	if( _count % 2 == 1) // todo mozna bude potreba prohodit
	{
		this->_color = "Black";
	}
	else
	{
		this->_color = "White";
	}
}

Stone::Stone(std::pair<int,int> coord) : _coord(coord), _inGroup(0), _color("Black")
{
	++_count;

	if( _count % 2 == 1)
	{
		this->_color = "Black";
	}
	else
	{
		this->_color = "White";
	}
}

/*
 *
 */
Stone::~Stone() {

}

/*
 *
 */
void Stone::setCoords(int int1, int int2)
{
	_coord.first = int1;
	_coord.second = int2;
}

/*
 *
 */
void Stone::setCoords(std::pair<int, int> pair)
{
	_coord = pair;
}

/*
 *
 */
std::pair<int, int> Stone::coords() const
{
	return _coord;
}

/*
 *
 */
void Stone::setColor(std::string color)
{
	_color = color;
}

/*
 *
 */
std::string Stone::color() const
{
	return _color;
}

/*
 * Funkce vraci Skupinu, do ktere kamen patri
 */
int Stone::getBelongingGroup() const
{
	return _inGroup;
}

/*
 *
 */
void Stone::setBelongingGroup(int g)
{
	_inGroup = g;
}

/*
 *
 */
int Stone::getCounter() {return _count;}
int Stone::_count = 0;

