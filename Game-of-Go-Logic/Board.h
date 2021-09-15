/*
 * Board.h
 *
 *  Created on: 1. 9. 2017
 *      Author: valgrut
 */

#ifndef BOARD_H_
#define BOARD_H_

#include <iostream>
#include <map>
#include <vector>
#include <utility>
#include "Group.h"
#include "Stone.h"

class Board {
public:
	Board(unsigned int size);
	virtual ~Board();

	Stone* stoneAt(unsigned int x, unsigned int y);
	Stone* stoneAt(std::pair<unsigned int, unsigned int> &pair);

	void placeStoneTo(unsigned int x, unsigned int y);
	void killStoneAt(unsigned int x, unsigned int y);

	void printGoban() const;
	void printGroups() const;
	void printHistory() const;

	int groupOfCurrentStone();
	Stone* getCurrentStone();

private:
	std::pair<unsigned int,unsigned int> _current; // posledni polozeny kamen
	std::vector<Stone*> _board;
	std::map<int, Group> _groups;
	unsigned int _gobanSize;
	std::vector<Stone> _gameHistory;

	bool outOfBoard(unsigned int x, unsigned int y) const;
	bool outOfBoard(std::pair<int,int> coord) const;

	void scout(int x, int y, int xx, int yy);

	int get2DPlace(int x, int y) const;
	int get2DPlace(std::pair<unsigned int,unsigned int> coord) const;
};

#endif /* BOARD_H_ */
