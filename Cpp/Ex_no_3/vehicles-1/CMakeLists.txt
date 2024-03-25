cmake_minimum_required(VERSION 3.21)
project(vehicles_1)

set(CMAKE_CXX_STANDARD 14)
add_compile_options(-Wall -Wextra -Werror -Wpedantic -pedantic-errors)

include_directories(include)

set(SOURCE_FILES
        src/vehicles.cpp)

add_executable(vehicles_1 ${SOURCE_FILES} main.cpp)

set(SOURCES_FILES_TESTS
        test/test_vehicles.cpp

        )

add_executable(vehicles_1__test ${SOURCE_FILES} ${SOURCES_FILES_TESTS} test/main_gtest.cpp)


target_include_directories(vehicles_1__test PUBLIC
        ../../googletest-master/googlemock/include
        ../../googletest-master/googletest/include
        )


add_subdirectory(../../googletest-master googletest-master)

target_link_libraries(vehicles_1__test gmock)