#include <iostream>
#include <string>
#include <vector>
#include <assert.h>

#define DEBUG
#undef DEBUG

using namespace std;

unsigned int sizeX = 8;
unsigned int sizeY = 8;
unsigned int MINES = 8;

vector<vector<char> > pole;

void initSurround(unsigned int y, unsigned int x);
void setMine(unsigned int y, unsigned int x)
{
	assert(y < sizeY);
	assert(x < sizeX);
	pole[y][x] = '*';
}

int main()
{
	srand (time(NULL));
	
	cout << "Minesweeper" << endl;
	cout << endl;

	// minesweeper initialisation
	pole.resize(sizeY);

	for(unsigned int i = 0; i < sizeY; i++)
	{
		pole.at(i).resize(sizeX, '0');
	}
	
	// nastaveni min (random)
	int xcoord, ycoord;
	for(unsigned int rnd = 0; rnd < MINES; )
	{
		xcoord = rand() % MINES;
		ycoord = rand() % MINES;
		if(pole[ycoord][xcoord] != '*')
		{
			setMine(ycoord, xcoord);
			rnd++;
		}
		else
			continue;
	}

	// calculation of surrounding
	for(int y = 0; y < sizeY; y++)
	{
		for(int x = 0; x < sizeX; x++)
		{
			if(pole[y][x] == '*')
			{
				initSurround(y, x);
			}
		}
	}

	// vykresleni pole
	for(unsigned int i = 0; i < sizeY; i++)
	{
		for(unsigned int j = 0; j < sizeX; j++)
			cout << pole.at(i).at(j);
		cout << endl;
	}

	return 0;
}


void initSurround(unsigned int y, unsigned int x)
{
	int ymin = (y-1 < 0) ? y-1 : 0;
	int xmin = (x-1 < 0) ? x-1 : 0;
	
	int test = y-1;
	if(test < 0)
	{
		ymin = 0;
	}
	else 
	{
		ymin = y-1;
	}

	test = x-1;
	if(test < 0)
	{
		xmin = 0;
	}
	else 
	{
		xmin = x-1;
	}
	test = y+1;
	int ymax = ((test) >= sizeY) ? sizeY : test+1; // zde
	test = x+1;
	int xmax = ((test) >= sizeX) ? sizeX : test+1;

	//cerr << "min: " << ymin << " " << xmin << endl;
	//cerr << "max: " << ymax << " " << xmax << endl;
	//cerr << endl;

	for(int sy = ymin; sy < ymax; sy++)   // ymax+1
	{			
		for(int sx = xmin; sx < xmax; sx++) // xmax+1
		{
			if(pole[sy][sx] != '*')
			{
				//cout << sy << " " << sx << endl; 
				int n = pole[sy][sx] - '0';
				n++;
				pole[sy][sx] = n + '0';
			}
		}
	}
	//cout << endl;	
}
