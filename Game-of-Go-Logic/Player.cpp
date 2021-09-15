/*
 * Player.cpp
 *
 *  Created on: 1. 8. 2017
 *      Author: valgrut
 */

#include "Player.h"

Player::Player() : name("Valgrut"), level(0)
{


}

Player::~Player() {

}

void Player::say(const string &speech)
{
	cout << speech << endl;
}

int Player::getLevel() const {
	return level;
}

void Player::setLevel(int level) {
	this->level = level;
}

const string& Player::getName() const
{
	return name;
}

void Player::setName(const string& name)
{
	this->name = name;
}
