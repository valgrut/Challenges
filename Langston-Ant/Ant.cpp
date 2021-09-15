#include "Ant.h"

Ant::Ant(const std::pair<int,int> mapsize) : _direction("UP"), _mapsize(mapsize)
{
     //this->_mapsize = mapsize;
     this->_position.first = this->_mapsize.first/2;   // x
     this->_position.second = this->_mapsize.second/2; // y
}

std::pair<int,int>& Ant::getAntPosition() {return this->_position;}
std::string Ant::getDirection() const {return this->_direction;}

bool Ant::moveForward()
{
     if(check())
          return true;

     if(_direction == "UP")
     {
          _position.second--;
          return false;
     }
     if(_direction == "DOWN")
     {
          _position.second++;
          return false;
     }
     if(_direction == "LEFT")
     {
          _position.first--;
          return false;
     }
     if(_direction == "RIGHT")
     {
          _position.first++;
          return false;
     }
}

void Ant::turnLeft()
{
     if(_direction == "UP")
     {
          _direction = "LEFT";
          return;
     }
     if(_direction == "DOWN")
     {
          _direction = "RIGHT";
          return;
     }
     if(_direction == "LEFT")
     {
          _direction = "DOWN";
          return;
     }
     if(_direction == "RIGHT")
     {
          _direction = "UP";
          return;
     }
}

void Ant::turnRight()
{
     if(_direction == "UP")
     {
          _direction = "RIGHT";
          return;
     }
     if(_direction == "DOWN")
     {
          _direction = "LEFT";
          return;
     }
     if(_direction == "LEFT")
     {
          _direction = "UP";
          return;
     }
     if(_direction == "RIGHT")
     {
          _direction = "DOWN";
          return;
     }
}

// returns true pokud se blizi k nejake hranici mapy (boardu)
bool Ant::check()
{
     if(_position.first == 1 || _position.first == _mapsize.first-2
     || _position.second == 1 || _position.second == _mapsize.second-2)
          return true;
     else
          return false;
}

Ant::~Ant()
{

}
