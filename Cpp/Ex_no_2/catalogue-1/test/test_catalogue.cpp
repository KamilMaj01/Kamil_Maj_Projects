//
// Created by majka on 30.03.2022.
//

#include "catalogue.hpp"
#include "gtest/gtest.h"
#include "gmock/gmock.h"

TEST(CatalogueTest, containsKeyIsNotPresent){
    Product apple("R4", "apple", 4.5567);
    Catalogue fruits;
    fruits.add_product(apple);


    EXPECT_EQ(fruits.contains("R5"), false);

}


TEST(CatalogueTest, containsKeyIsPresent){
    Product apple("R4", "apple", 4.5567);
    Catalogue fruits;
    fruits.add_product(apple);

    EXPECT_EQ(fruits.contains("R4"), true);

}

using ::testing::Property;

// ...

TEST(CatalogueTest, get_products_by_name_part_case_sensitive) {
    Product p1("X1", "TOY uppercase", 10);
    Product p2("X2", "toy lowercase", 10);

    Catalogue catalogue(Catalogue::inventory_t{
            {p1.get_id(), p1},
            {p2.get_id(), p2},
    });

    auto filtered_products = catalogue.get_products_by_name_part("toy", true);

    ASSERT_EQ(filtered_products.size(), 1U);
    EXPECT_EQ(filtered_products[0].get_id(), p2.get_id());
}

TEST(CatalogueTest, get_products_by_name_part_case_insensitive) {
    Product p1("X1", "TOY uppercase", 10);
    Product p2("X2", "toy lowercase", 10);

    Catalogue catalogue(Catalogue::inventory_t{
            {p1.get_id(), p1},
            {p2.get_id(), p2},
    });

    auto filtered_products = catalogue.get_products_by_name_part("toy", false);

    ASSERT_EQ(filtered_products.size(), 2U);

    // Upewnij się, że wektor z wynikami zawiera element, którego metoda
    // `Product::get_id()` zwraca wartość `p1.get_id()`.
    EXPECT_THAT(filtered_products, Contains(Property(&Product::get_id, p1.get_id())));

    EXPECT_THAT(filtered_products, Contains(Property(&Product::get_id, p2.get_id())));
}