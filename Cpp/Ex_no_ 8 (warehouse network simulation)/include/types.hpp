//
// Created by majka on 06.01.2023.
//

#ifndef INC_7_TEMAT_SYMULACJA_SIECI__TYPES_HPP
#define INC_7_TEMAT_SYMULACJA_SIECI__TYPES_HPP

#include "package.hpp"
#include "storage_types.hpp"

#include <list>
#include <vector>
#include <numeric>
#include <ostream>

class Package;

using ElementID = std::size_t;

using ElementList = std::list<Package>;

#endif //INC_7_TEMAT_SYMULACJA_SIECI__TYPES_HPP
