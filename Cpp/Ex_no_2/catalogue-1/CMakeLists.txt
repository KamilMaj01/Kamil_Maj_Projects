cmake_minimum_required(VERSION 3.21)
project(catalogue_1)

set(CMAKE_CXX_STANDARD 14)
add_compile_options(-Wall -Wextra -Werror -Wpedantic -pedantic-errors)

include_directories(include)

set(SOURCE_FILES
        src/catalogue.cpp)

add_executable(catalogue_1 ${SOURCE_FILES} main.cpp)

set(SOURCES_FILES_TESTS
        test/test_product.cpp
        test/test_catalogue.cpp
        )

add_executable(catalogue_1__test ${SOURCE_FILES} ${SOURCES_FILES_TESTS} test/main_gtest.cpp)


target_include_directories(catalogue_1__test PUBLIC
        ../../googletest-master/googlemock/include
        ../../googletest-master/googletest/include
        )


add_subdirectory(../../googletest-master googletest-master)

target_link_libraries(catalogue_1__test gmock)
