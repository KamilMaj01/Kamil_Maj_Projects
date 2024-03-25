#include "shapes.hpp"
#include <vector>
#include <algorithm>
#include <numeric>

double calculate_total_area(const std::vector<Shape*>& shapes){

    return std::accumulate(shapes.begin(),shapes.end(),0.0,
                           [](auto acc, const auto& el){return acc += el->area();});

}