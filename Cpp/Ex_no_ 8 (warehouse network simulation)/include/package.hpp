//
// Created by majka on 06.01.2023.
//


#ifndef INC_7_TEMAT_SYMULACJA_SIECI__PACKAGE_HPP
#define INC_7_TEMAT_SYMULACJA_SIECI__PACKAGE_HPP



#include <list>
#include <set>
#include <numeric>
#include <algorithm>
#include <ostream>
#include "storage_types.hpp"
#include "types.hpp"




class Package{
public:
    Package();
    Package(ElementID id) : id_(id){ assigned_IDs_.insert(id_);}
    Package(Package&& package) = default;
    Package& operator=(Package&& other) noexcept;
    ElementID get_id() const;
    ~Package();

    static std::set<ElementID> get_assigned_IDs();
    static std::set<ElementID> get_freed_IDs();

private:
    ElementID id_;
    static std::set<ElementID> assigned_IDs_;
    static std::set<ElementID> freed_IDs_;
};


#endif //INC_7_TEMAT_SYMULACJA_SIECI__PACKAGE_HPP
