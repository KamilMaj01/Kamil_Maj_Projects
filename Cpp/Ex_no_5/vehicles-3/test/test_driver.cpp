#include "gtest/gtest.h"

#include "vehicles.hpp"

TEST(DriverTest, toStringNoVehicle) {
    Driver owner("Adam Abacki", Gender::Male);

    std::string str = to_string(owner);

    ASSERT_EQ(str, "Adam Abacki : [no vehicle]");
}

TEST(DriverTest, toStringWithVehicle) {
    Driver owner("Adam Abacki", std::make_unique<Car>("C1", "Lexus", 500.0), Gender::Male);

    std::string str = to_string(owner);

    std::string vehicle_str = to_string(*(owner.get_vehicle()));
    ASSERT_EQ(str, "Adam Abacki : " + vehicle_str );
}

TEST(DriverAuxTest, copying) {
    Driver driver1("Adam Abacki", std::make_unique<Car>("C1", "Lexus", 500.0), Gender::Male);

    Driver driver2(std::move(driver1));

    EXPECT_EQ(driver1.get_vehicle(), nullptr);
    EXPECT_EQ((driver2.get_vehicle())->get_id(), "C1");
}

TEST(DriverAuxTest, assignment) {
    Driver driver1("Adam Abacki", std::make_unique<Car>("C1", "Lexus", 500.0), Gender::Male);
    Driver driver2("Bogdan Babacki", Gender::Male);

    driver2 = std::move(driver1);

    EXPECT_EQ(driver1.get_vehicle(), nullptr);
    EXPECT_EQ((driver2.get_vehicle())->get_id(), "C1");
}

TEST(DriverAuxTest, assignVehicleToDriver) {
    std::vector<std::unique_ptr<Vehicle>> ptr_result;
    std::unique_ptr<Car> car_1 = std::make_unique<Car>("C10", "audi", 100.1);
    std::unique_ptr<Bicycle> bicycle_1 = std::make_unique<Bicycle>("R10", "romet", 8);
    std::unique_ptr<Car> car_2 = std::make_unique<Car>("C11", "bmw", 306.0);
    ptr_result.push_back(std::move(car_1));
    ptr_result.push_back(std::move(bicycle_1));
    ptr_result.push_back(std::move(car_2));

    Driver owner("Kamil Maj", Gender::Male);
    assign_vehicle_to_driver(ptr_result, owner);

    ASSERT_EQ(ptr_result.size(), 3U);
    EXPECT_EQ(ptr_result[0]->get_id(), "C10");
    EXPECT_EQ(ptr_result[1]->get_id(), "R10");
    EXPECT_EQ(owner.get_gender(), Gender::Male);


    EXPECT_EQ(owner.get_vehicle()->get_id(), "C11");




}
