#ifndef SHAPE_H
#define SHAPE_H

#include <iostream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

class Shape
{
    public:
        //Shape();
        Shape(string shape, unsigned int x, unsigned int y);
        virtual ~Shape();

        vector< pair<int,int> > & getShape();

        void rotate();
        void left();
        void right();
        void fall();

    protected:

    private:
         vector< pair<int,int> > _shape;
         unsigned int _sizeX;
         unsigned int _sizeY;
};

#endif
