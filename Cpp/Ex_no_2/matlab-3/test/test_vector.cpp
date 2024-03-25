#include "gtest/gtest.h"

#include "matlab.hpp"

TEST(MatlabVectorTest, createWithSize) {
    MatVect v(2U);

    // Użyto ASSERT_XXX, gdyż dalsze warunki testowe mają sens tylko wówczas,
    //   gdy wektor zawiera (co najmniej) dwie składowe. Jeśli warunek nie jest
    //   spełniony, należy bezwzględnie przerwać dalsze wykonywanie testów
    //   (inaczej np. wywołanie `v.get_elem(0)` może rzucić wyjątek, jeśli
    //   kontener jest pusty.
    // EXPECT_XXX jedynie oznacza test jako "nie powiódł się", jednak pozwala na
    //   wykonywanie dalszych instrukcji w ramach tego testu, co często umożlwia
    //   uzyskanie dalszych informacji diagnostycznych (np. tu - informację
    //   o faktycznej wartości obu (!) składowych, niezależnie od tego, czy są
    //   to wartości poprawne, czy też nie.
    ASSERT_EQ(v.size(), 2U);
    EXPECT_EQ(v[0], 0);
    EXPECT_EQ(v[1], 0);
}

TEST(MatlabVectorTest, norm) {
    std::vector<int> vec;
    vec.push_back(2);
    vec.push_back(5);
    vec.push_back(2);
    MatVect v2(vec);
    double norm_result = v2.norm();
    EXPECT_EQ(norm_result, sqrt(4+4+25));
}

TEST(MatlabVectorTest, add) {
    MatVect v1({1, 2});
    MatVect v2({4, 5});

    MatVect v_sum = add_vectors(v1,v2);

    ASSERT_EQ(v_sum.size(), 2);
    EXPECT_EQ(v_sum[0], 5);
    EXPECT_EQ(v_sum[1], 7);

}

TEST(MatlabVectorTest, string){
    std::vector<int> vec;
    vec.push_back(1);
    vec.push_back(5);
    vec.push_back(2);
    MatVect v2(vec);
    v2[0] = 6;
    std::string str = to_string(v2);
    EXPECT_EQ("6 5 2 ", str);
}
