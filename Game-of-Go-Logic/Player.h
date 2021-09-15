/*
 * Player.h
 *
 *  Created on: 1. 8. 2017
 *      Author: valgrut
 */

#ifndef PLAYER_H_
#define PLAYER_H_

#include <iostream>


using namespace std;

class Player
{
	string name;
	int level;

public:
	Player();
	virtual ~Player();
	void say(const string &speech);

	const string& getName() const;
	void setName(const string& name);

	int getLevel() const;
	void setLevel(int level);

};

#endif /* PLAYER_H_ */
