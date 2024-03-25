//
// Created by plejc on 19.01.2023.
//

#ifndef INC_7_TEMAT_SYMULACJA_SIECI__HELPERS_HPP
#define INC_7_TEMAT_SYMULACJA_SIECI__HELPERS_HPP

#include <functional>
#include <random>


extern std::random_device rd;
extern std::mt19937 rng;

extern double default_probability_generator();

using ProbabilityGenerator = std::function<double ()>;
extern ProbabilityGenerator probability_generator;

#endif //INC_7_TEMAT_SYMULACJA_SIECI__HELPERS_HPP
