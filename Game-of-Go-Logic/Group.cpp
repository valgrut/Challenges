/*
 * Group.cpp
 *
 *  Created on: 1. 9. 2017
 *      Author: valgrut
 */

#include "Group.h"

/*
 *
 */
Group::Group() : _liberties(4), _group(0), _groupNumber(0)
{
	_groupNumber = _count;
	++Group::_count;
}

/*
 *
 */
Group::Group(int groupNumber) : _liberties(4), _group(0), _groupNumber(groupNumber)
{
	//_groupNumber = _count;
	//++Group::_count;
}

/*
 *
 */
Group::~Group()
{
}

/*
 * vrati & vector<Stone>
 */
std::vector<Stone> & Group::getGroup()
{
	return _group;
}

/*
 * Vlozi do skupiny kamen
 */
void Group::addStone(Stone &s)
{
	s.setBelongingGroup(groupNumber());
	_group.push_back(s);
}

/*
 * Vrati pocet kamenu ve skupine
 */
int Group::getCountInGroup() const
{
	return _group.size();
}

/*
 * Vypise vsechny kameny v teto skupine a informace o skupine samotne
 */
void Group::printStones() const
{
	std::cout << "Group no. " << groupNumber() << std::endl;
	std::cout << "Liberties " << getLiberties() << std::endl;
	for(auto n : _group)
		std::cout << n.coords().first << "|" << n.coords().second << " group:" << n.getBelongingGroup() <<  std::endl;
	std::cout << std::endl;
}

/*
 *
 */
unsigned int Group::getLiberties() const
{
	return _liberties;
}

void Group::setLiberties(int lib)
{
	this->_liberties = lib;
}

/*
 *
 */
void Group::mergeGroups(Group &g)
{
	std::cout << "Merging ..." << std::endl; // TODO odstranit pak

	_group.reserve(g.getCountInGroup() + getCountInGroup());
	_group.insert(_group.end(), g.getGroup().begin(), g.getGroup().end());

	// nastavime prislusnictvi k nove skupine vsem kamenum v teto skupině
	for(auto &n : _group)
	{
		n.setBelongingGroup(_groupNumber);
		std::cout << "m: "<< n.coords().first << " | " << n.coords().second << std::endl; // TODO odstranit pak
	}

	_liberties += g.getLiberties();

	// skupina se jiz presunula do nove, takze ji znicime
	g.setLiberties(0);

	//std::cout << groupW.getGroup()[0].getBelongingGroup() << std::endl;
}

/*
 *
 */
unsigned int Group::groupNumber() const
{
	return _groupNumber;
}

/*
 *
 */
void Group::setGroupNumber(unsigned int gn)
{
	_groupNumber = gn;

	// nastavime prislusenstvi k nove skupine vsem kamenum
	if(! _group.empty())
	{
		for(auto &n : _group)
		{
			n.setBelongingGroup(_groupNumber);
		}
	}
}

int Group::getCounter() {return _count;}
int Group::_count = 0;
