//
// Created by majka on 10.04.2022.
//
#include "vehicles.hpp"
#include <iostream>
//#include <sstream>
#include <algorithm>
//#include <iomanip>
#include <numeric>

std::string to_string(const Vehicle& vehicle){
    std::ostringstream oss;
    oss<< vehicle.get_id() <<" "<< vehicle.get_brand();
    std::string result = oss.str();
    return result;
}

std::string to_string(std::vector<Vehicle*>::const_iterator vehicles_begin,
                      std::vector<Vehicle*>::const_iterator vehicles_end){
    std::string result;
    result = std::accumulate(vehicles_begin, vehicles_end, std::string(), [](std::string &result ,const Vehicle* vehicle){return result += to_string(*vehicle) + "\n";});
    return result;
};

std::string compute_min_travel_duration(const double distance, const Vehicle& vehicle){
    double time = (distance * 1)/vehicle.get_max_speed();
    std::ostringstream oss;
    oss<<time<<" h";
    std::string result = oss.str();
    return result;
}

std::vector<Vehicle*> filter_vehicles(
        std::vector<Vehicle*>::const_iterator vehicles_begin,
        std::vector<Vehicle*>::const_iterator vehicles_end,
        std::function<bool (const Vehicle&)> predicate){
    std::vector<Vehicle*> vehicles_filtered;
    std::copy_if(vehicles_begin, vehicles_end, std::back_inserter(vehicles_filtered), [&predicate](const Vehicle* vehicle_ptr){
        return predicate(*vehicle_ptr);});
    return vehicles_filtered;

}

