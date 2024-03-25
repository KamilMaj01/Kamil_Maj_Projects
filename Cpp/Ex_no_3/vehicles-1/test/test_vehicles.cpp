//
// Created by majka on 10.04.2022.
//
#include <vehicles.hpp>
#include "gtest/gtest.h"
#include "gmock/gmock.h"

// for Bicycle:

TEST( BicycleTest, get_max_speed){
    Bicycle bicycle1("R4", "romet", 4 );

    EXPECT_EQ(12, bicycle1.get_max_speed());

}

TEST( CarTest, get_max_speed){
    Car car1("BMW", "E71", 306 );

    EXPECT_EQ(306, car1.get_max_speed());

}

TEST(CarTest, to_string){
    Car car1("BMW", "E71", 306 );
    EXPECT_EQ("BMW E71", to_string(car1));
}

TEST(VehicleAuxTest, computeMinTravelDuration){
    Car car1("BMW", "E71", 40 );
    Bicycle bicycle1("R100", "romet", 10);

    EXPECT_EQ(compute_min_travel_duration(15, bicycle1), "0.5 h");
    EXPECT_EQ(compute_min_travel_duration(80, car1), "2 h");
}

TEST(VehiclesAlgorithms, filter){
    Car car1("C1", "", 100.0);
    Car car2("C2", "", 200.0);
    Bicycle bicycle("B1", "", 0);

    std::vector<Vehicle*> vehicles = { &car1, &bicycle, &car2 };

    std::function<bool(const Vehicle&)> faster_than_50_kph = [](const Vehicle& vehicle) {
        return vehicle.get_max_speed() > 50;
    };
    auto filtered_vehicle = filter_vehicles(std::begin(vehicles), std::end(vehicles), faster_than_50_kph);
    ASSERT_EQ(filtered_vehicle.size(), 2U);
    EXPECT_THAT(filtered_vehicle, Contains(testing::Property(&Vehicle::get_id, car1.get_id())));
    EXPECT_THAT(filtered_vehicle, Contains(testing::Property(&Vehicle::get_id, car2.get_id())));
}