#ifndef GAME_H
#define GAME_H

#include <iostream>
#include <string>
#include <unistd.h>
#include <chrono>
#include <thread>

#include "Board.h"
#include "Ant.h"

using namespace std;

class Game
{
public:
     Game();
     virtual ~Game();
     void render();
     void run();

private:
     Ant* _ant;
     Board* _board;

};

#endif
