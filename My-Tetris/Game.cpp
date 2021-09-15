#include "Game.h"

Game::Game() : _board(8, 20), _score(0)
{
	srand (time(NULL));
	_currentShape = newRandom();
}

Game::~Game()
{
	for(auto &s : _placedShapes)
     {
		delete s;
	}
}

// main loop
void Game::run()
{
	render();

	int i = 0;
	bool f = false;

	int c = '0';
	while(1)
	{
		if(f == false)
		{
			system("/bin/stty raw");
			c = getchar();
			system("/bin/stty cooked");

			if(c == '9') return;

			// zpracovani vstupu
			handleInput(c);

			f = true;
		}

		if(_board.collision())
		{
			// aktualni shape vlozime do pole
			_placedShapes.push_back(_currentShape);
			for(int row = 0; row < _board.getSizeX(); row++)
			{
				if(_board.checkRow(row))
				{
					_score++;
					_board.pushBoardDown(row, 1);
				}
			}
			_currentShape = newRandom();
		}
		//_board.pushBoardDown(18, 1);
		_currentShape->fall();

		// vykreslime mapu
		render();

		cout << ++i << endl;
		sleep(1);
		f = false;
	}

}

Shape* Game::newRandom()
{
	string newShape;
	int rnd = rand() % 5;
	if(rnd == 0) newShape = "L";
	if(rnd == 1) newShape = "O";
	if(rnd == 2) newShape = "Z";
	if(rnd == 3) newShape = "I";
	if(rnd == 4) newShape = "T";
	return new Shape(newShape, _board.getSizeX(), _board.getSizeY());
}

void Game::handleInput(char c)
{
	switch(c)
	{
		case 'a': //left
			_currentShape->left();
			break;

		case 'd': //right
			_currentShape->right();
			break;

		case 'w': //rotate
			_currentShape->rotate();
			break;

		case 's':
			_currentShape->fall();
			break;
	}
}

void Game::render()
{
	system("clear");

	for(unsigned int y = 0; y < _board.getSizeY(); y++)
	{
		for(unsigned int x = 0; x < _board.getSizeX(); x++)
		{
			//cout << "y " << y << " |x " << x << endl;
			_board.setBoardAt(y, x, '.');
		}
	}

	for(auto &s : _placedShapes)
     {
		_board.placeShape(s);
	}
	_board.placeShape(_currentShape);
	_board.draw();

	cout << "Score: " << score() << endl;
}

Board & Game::getBoard()
{
     return _board;
}

unsigned int Game::score() const
{
	return _score;
}

void Game::setScore(unsigned int newScore)
{
	_score = newScore;
}
