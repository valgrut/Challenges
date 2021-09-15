/*
 * Group.h
 *
 *  Created on: 1. 9. 2017
 *      Author: valgrut
 */

#ifndef GROUP_H_
#define GROUP_H_

#include <vector>
#include "Stone.h"

class Group
{
public:
	Group();
	Group(int groupNumber);
	virtual ~Group();

	std::vector<Stone> & getGroup();
	void mergeGroups(Group &g);
	void printStones() const;

	void addStone(Stone &s);

	int getCountInGroup() const;
	unsigned int getLiberties() const;
	void setLiberties(int lib);

	unsigned int groupNumber() const;
	void setGroupNumber(unsigned int gn);

	static int _count;
	static int getCounter();

private:
	std::vector<Stone> _group;
	unsigned int _liberties;
	unsigned int _groupNumber;
};

#endif /* GROUP_H_ */
