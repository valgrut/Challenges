#include "Game.h"

Game::Game()
{
	_board = new Board(make_pair(100, 70));
	_ant   = new Ant(make_pair(100, 70));
}

Game::~Game()
{
	delete _board;
	delete _ant;
}

// main loop
void Game::run()
{
	render();

	while(1)
	{
		if(_board->isWhite(_ant->getAntPosition()))
		{
			_ant->turnRight();
		}
		else if(_board->isBlack(_ant->getAntPosition()))
		{
			_ant->turnLeft();
		}

		_board->invertColor(_ant->getAntPosition());
		if(_ant->moveForward())
			return;

		// vykreslime mapu
		render();

		//sleep(0.5);  //s
		//usleep(500); //ms
		
		std::this_thread::sleep_for(std::chrono::milliseconds(500));
	}

}

void Game::render()
{
	system("clear");

	_board->draw();
}
