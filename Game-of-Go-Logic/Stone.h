/*
 * Stone.h
 *
 *  Created on: 1. 9. 2017
 *      Author: valgrut
 */

#ifndef STONE_H_
#define STONE_H_

#include <iostream>
#include <utility>
#include <string>

class Stone {
public:
	Stone();
	Stone(std::pair<int,int> coord);
	virtual ~Stone();

	void setCoords(int, int);
	void setCoords(std::pair<int,int>);
	std::pair<int,int> coords() const;

	void setColor(std::string color);
	std::string color() const;

	int getBelongingGroup() const;
	void setBelongingGroup(int g);

	static int _count;
	static int getCounter();

private:
	std::pair<int,int> _coord;
	std::string _color;
	int _inGroup;

};

#endif /* STONE_H_ */
