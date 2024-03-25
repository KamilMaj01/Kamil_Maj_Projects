cmake_minimum_required(VERSION 3.13)

set(PROJECT_ID 7_temat_symulacja_sieci_)



set(SOURCE_FILES
        src/storage_types.cpp
        src/package.cpp

        )

set(SOURCES_FILES_TESTS
        test/test_package.cpp
        test/test_storage_types.cpp
        )

include(../SetCommonConfig.cmake)