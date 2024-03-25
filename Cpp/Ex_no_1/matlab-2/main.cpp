#include "matlab.hpp"

// Wersje bibliotek standardowych znanych z języka C, ale zaimplementowanych
// dla C++, mają przedrostek "c" (np. stdlib.h -> cstdlib).
#include <cstdlib>
#include <iostream>

int main() {
    int v[] = {1, 2, 3};
    print_vector(v, 3);
    MatVect v1(3);
    v1.set_elem(0,1);
    v1.set_elem(1,2);
    std::cout<<v1.norm()<< std::endl;





    return EXIT_SUCCESS;
}
