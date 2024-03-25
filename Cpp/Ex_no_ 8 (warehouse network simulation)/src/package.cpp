//
// Created by majka on 06.01.2023.
//

#include "package.hpp"

std::set<ElementID> Package::assigned_IDs_ = {};
std::set<ElementID> Package::freed_IDs_ = {};

ElementID Package::get_id() const {
    return id_;
}

Package::Package() {
    if(assigned_IDs_.empty())
        freed_IDs_.insert(1);

    if(!freed_IDs_.empty())
    {
        id_ = *freed_IDs_.begin();
        freed_IDs_.erase(freed_IDs_.begin());
        assigned_IDs_.insert(id_);
    }
    else
    {
        id_ = *std::max_element(assigned_IDs_.begin(), assigned_IDs_.end()) + 1;
        assigned_IDs_.insert(id_);
    }
}




Package::~Package() {
    freed_IDs_.insert(id_);
    assigned_IDs_.erase(id_);

}



std::set<ElementID> Package::get_assigned_IDs(){
    return assigned_IDs_;
}


std::set<ElementID> Package::get_freed_IDs(){
    return freed_IDs_;
}

Package& Package::operator=(Package&& other) noexcept
{
    assigned_IDs_.erase(id_);
    freed_IDs_.insert(id_);
    id_ = other.id_;
    return *this;
}
