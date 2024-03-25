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

TEST(MatlabVectorTest, createFromVector) {
    MatVect v(std::vector<int>{1, 2});

    ASSERT_EQ(v.size(), 2U);
    EXPECT_EQ(v[0], 1);
    EXPECT_EQ(v[1], 2);
}

TEST(MatlabVectorTest, createFromString) {
    MatVect v("[1, 2, 3]");

    ASSERT_EQ(v.size(), 3U);
    EXPECT_EQ(v[0], 1);
    EXPECT_EQ(v[1], 2);
    EXPECT_EQ(v[2], 3);
}

TEST(MatlabVectorTest, norm) {
    // Inicjalizacja w poniższym teście została przeprowadzona w sposób bardziej
    //   zwięzły, za pomocą tzw. list initialization:
    //   https://en.cppreference.com/w/cpp/language/list_initialization
    std::vector<int> vs{3, 4, 0};
    MatVect v(vs);

    EXPECT_EQ(v.norm(), 5);
}

TEST(MatlabVectorTest, add) {
    MatVect v1(std::vector<int>{1, 2});
    MatVect v2(std::vector<int>{4, 5});

    MatVect v_sum = add_vectors(v1, v2);

    ASSERT_EQ(v_sum.size(), 2U);
    EXPECT_EQ(v_sum[0], 5);
    EXPECT_EQ(v_sum[1], 7);
}

TEST(MatlabVectorTest, toString) {
    MatVect v(std::vector<int>{1, 2});

    std::string str = to_string(v);

    ASSERT_EQ(str, "[ 1, 2 ]");
}

TEST(MatlabVectorTest, sumElements) {
    MatVect v(std::vector<int>{1, 2});

    ASSERT_EQ(v.sum(), 3);
}
