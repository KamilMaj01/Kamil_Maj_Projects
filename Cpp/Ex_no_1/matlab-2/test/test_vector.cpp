#include "gtest/gtest.h"

#include "matlab.hpp"

TEST(MatlabVectorTest, add) {
    const std::size_t size = 3;
    MatVect v1(size);
    MatVect v2(size);

    for(std::size_t i = 0; i < size; i++){
        v1.set_elem(i, (int)(size-i));
        v2.set_elem(i, (int)i);
    }

    MatVect v_sum = add_vectors(v1, v2);

    ASSERT_NE(NULL, v_sum.size());

    EXPECT_EQ(v_sum.get_elem(0), 3);
    EXPECT_EQ(v_sum.get_elem(1), 3);
    EXPECT_EQ(v_sum.get_elem(2), 3);

}

TEST(MatlabVectorTest, norm){
    MatVect v1(3U);
    v1.set_elem(0,3);
    v1.set_elem(1,4);
    v1.set_elem(2,0);

    EXPECT_EQ(v1.norm(), 5);
}

TEST(MatlabVectorTest, createWithSize) {
    MatVect v(2U);

    ASSERT_EQ(v.size(), 2U);  // przyrostek "U" oznacza wartość bez znaku (ang. unsigned)
    EXPECT_EQ(v.get_elem(0), 0);
    EXPECT_EQ(v.get_elem(1), 0);
}