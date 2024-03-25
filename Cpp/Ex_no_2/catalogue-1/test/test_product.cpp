//
// Created by majka on 30.03.2022.
//
#include "gtest/gtest.h"
#include "catalogue.hpp"


TEST(ProductTest, creat) {
    Product apple("R4", "apple", 4.5567);
    EXPECT_EQ(apple.get_id(), "R4");
    EXPECT_EQ(apple.get_name(), "apple");
    EXPECT_EQ(apple.get_price(), 4.5567);

}

TEST(ProductTest, toString){
    Product apple("R4", "apple", 4.5567);
    std::string result = to_string(apple);
    EXPECT_EQ(result, "apple [R4] : $4.56");

}

TEST(CatalogueTest, getProductsWithAppropriatePrice) {
    Product p1("X1", "Toy X1", 10.3);
    Product p2("X2", "Toy X2", 8.3);

    Catalogue catalogue(Catalogue::inventory_t{
            {p1.get_id(), p1},
            {p2.get_id(), p2},
    });

    std::function<bool (double)> predicate = [](double price) {
        return (price < 10.0);
    };
    auto filtered_products = catalogue.get_products_with_appropriate_price(predicate);

    ASSERT_EQ(filtered_products.size(), 1U);
    EXPECT_EQ(filtered_products[0].get_id(), p2.get_id());
}