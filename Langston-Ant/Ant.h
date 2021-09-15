#ifndef ANT_H
#define ANT_H

#include <iostream>
#include <string>
#include <vector>
#include <utility>

class Ant
{
    public:
        Ant(const std::pair<int,int> mapsize);
        virtual ~Ant();

        std::pair<int,int>& getAntPosition();
        std::string getDirection() const;

        bool moveForward();
        void turnLeft();
        void turnRight();

    protected:

    private:
         std::string _direction;
         std::pair<int,int> _position;
         const std::pair<int,int> _mapsize;


         bool check();
};

#endif
