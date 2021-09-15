#include "Shape.h"

//Shape::Shape() {}
Shape::Shape(string shape, unsigned int x, unsigned int y) : _shape(4), _sizeX(x), _sizeY(y)
{
    for(auto &s : _shape)
    {
         s.first = 0;  // x
         s.second = 0; // y
    }

    if(shape == "O")
    {
         _shape[0].first = 0;
         _shape[0].second = 0;
         _shape[1].first = 0;
         _shape[1].second = 1;
         _shape[2].first = 1;
         _shape[2].second = 0;
         _shape[3].first = 1;
         _shape[3].second = 1;
    }
    if(shape == "L")
    {
         _shape[0].first = 1;
         _shape[0].second = 0;
         _shape[1].first = 1;
         _shape[1].second = 1;
         _shape[2].first = 1;
         _shape[2].second = 2;
         _shape[3].first = 0;
         _shape[3].second = 2;
    }
    if(shape == "I")
    {
         _shape[0].first = 1;
         _shape[0].second = 0;
         _shape[1].first = 1;
         _shape[1].second = 1;
         _shape[2].first = 1;
         _shape[2].second = 2;
         _shape[3].first = 1;
         _shape[3].second = 3;
    }
    if(shape == "Z")
    {
         _shape[0].first = 0;
         _shape[0].second = 0;
         _shape[1].first = 1;
         _shape[1].second = 0;
         _shape[2].first = 1;
         _shape[2].second = 1;
         _shape[3].first = 2;
         _shape[3].second = 1;
    }
    if(shape == "T")
    {
         _shape[0].first = 1;
         _shape[0].second = 0;
         _shape[1].first = 2;
         _shape[1].second = 0;
         _shape[2].first = 3;
         _shape[2].second = 0;
         _shape[3].first = 2;
         _shape[3].second = 1;
    }
}

vector< pair<int,int> > & Shape::getShape()
{
     return _shape;
}

void Shape::fall()
{
     for(auto &s : _shape)
     {
          if(s.second == _sizeY-1)
               return;
     }
     ++_shape[0].second;
     ++_shape[1].second;
     ++_shape[2].second;
     ++_shape[3].second;
}

void Shape::rotate()
{
     swap(_shape[0].first, _shape[0].second);
     swap(_shape[1].first, _shape[1].second);
     swap(_shape[2].first, _shape[2].second);
     swap(_shape[3].first, _shape[3].second);
}

void Shape::left()
{
     for(auto &s : _shape)
     {
          if(s.first == 0)
               return;
     }
     --_shape[0].first;
     --_shape[1].first;
     --_shape[2].first;
     --_shape[3].first;
}

void Shape::right()
{
     for(auto &s : _shape)
     {
          if(s.first == _sizeY-1)
               return;
     }
     ++_shape[0].first;
     ++_shape[1].first;
     ++_shape[2].first;
     ++_shape[3].first;
}

Shape::~Shape()
{
     //for(auto &i : m_maps) delete i.second;
}
