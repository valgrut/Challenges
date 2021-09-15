//============================================================================
// Name        : EclipseTest2.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <utility>

#include "Board.h"

#include "Group.h"
#include "Stone.h"

int main()
{
	/*
	Group groupB(1);
	Group groupW(2);

	Stone stone1;
	stone1.setCoords(5, 8);

	Stone stone2;
	stone2.setCoords(7, 8);

	Stone stone3;
	stone3.setCoords(6, 8);
	*/

	/* GROUPS */
	/*
	groupB.addStone(stone1);
	groupB.addStone(stone3);
	groupB.printStones();

	groupW.addStone(stone2);
	groupW.printStones();

	groupW.mergeGroups(groupB);
	groupW.printStones();
	*/


	/************** BOARD ****************/
	Board b(9);

	//b.placeStoneTo(3, 5);
	//b.placeStoneTo(4, 5);
	//b.placeStoneTo(4, 6);

	//b.printGoban();
	//b.printGroups();

	/* game loop */
	int posX = 0;
	int posY = 0;
	while(1)
	{
		std::cin >> posX;
		std::cin >> posY;
		b.placeStoneTo(posX, posY);
		b.printGoban();
		b.printGroups();
	}

	b.printHistory();

	return 0;
}
