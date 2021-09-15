#ifndef GAME_H
#define GAME_H

#include <iostream>
#include <string>
#include <unistd.h>

#include "Board.h"
#include "Shape.h"

using namespace std;

class Game
{
public:
     Game();
     virtual ~Game();
     void handleInput(char c);
     void render();
     void run();

     Shape* newRandom();

     Board & getBoard();
     unsigned int score() const;
     void setScore(unsigned int newScore);

private:
     Shape * _currentShape;
     vector<Shape*> _placedShapes;
     Board _board;
     unsigned int _score;

};

#endif
