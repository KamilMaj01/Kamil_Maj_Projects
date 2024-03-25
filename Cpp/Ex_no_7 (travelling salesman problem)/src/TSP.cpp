#include "TSP.hpp"

#include <algorithm>
#include <stack>
#include <optional>

#include <iostream>

std::ostream& operator<<(std::ostream& os, const CostMatrix& cm) {
    for (std::size_t r = 0; r < cm.size(); ++r) {
        for (std::size_t c = 0; c < cm.size(); ++c) {
            const auto& elem = cm[r][c];
            os << (is_inf(elem) ? "INF" : std::to_string(elem)) << " ";
        }
        os << "\n";
    }
    os << std::endl;

    return os;
}

/* PART 1 */

/**
 * Create path from unsorted path and last 2x2 cost matrix.
 * @return The vector of consecutive vertex.
 */

//**********ZROBIONE**********//

path_t StageState::get_path() {
    std::size_t cost;
    NewVertex vertex;

    for(std::size_t i = 0; i<2; ++i) {
        cost = reduce_cost_matrix();

        update_lower_bound(cost);
        vertex = choose_new_vertex();

        append_to_path(vertex.coordinates);
        update_cost_matrix(vertex.coordinates);
    }

    path_t resul_path = {unsorted_path_[0].row, unsorted_path_[0].col};
    const auto unsorted_path = get_unsorted_path();
    while (resul_path.front() != resul_path.back()) {
        for (const auto vertex : unsorted_path) {
            if (vertex.row == resul_path.back()) {
                resul_path.push_back(vertex.col);
            }
        }
    }

    resul_path.erase(resul_path.begin());

    return resul_path;
}

/**
 * Get minimum values from each row and returns them.
 * @return Vector of minimum values in row.
 */

//**********ZROBIONE**********//

std::vector<cost_t> CostMatrix::get_min_values_in_rows() const {
    std::vector<cost_t> min_values;
    cost_t min = 0;
    for(const auto& i : matrix_){
        min = i[0];
        for(const auto j : i){
            if(j<min){
                min = j;
            }
        }
        if(is_inf(min)){
            min =0;
        }
        min_values.push_back(min);
    }

    return min_values;
}


/**
 * Reduce rows so that in each row at least one zero value is present.
 * @return Sum of values reduced in rows.
 */

//**********ZROBIONE**********//

cost_t CostMatrix::reduce_rows() {
    std::vector<cost_t> min_values = get_min_values_in_rows();

    for(std::size_t i =0; i<matrix_.size(); ++i){
        for(std::size_t j = 0; j<matrix_[i].size(); ++j){
            if(not is_inf(matrix_[i][j])) {
                matrix_[i][j] = matrix_[i][j] - min_values[i];
            }
        }
    }

    cost_t sum = std::accumulate(min_values.begin(),min_values.end(),0);
    return sum;
}

/**
 * Get minimum values from each column and returns them.
 * @return Vector of minimum values in columns.
 */

//**********ZROBIONE**********//

std::vector<cost_t> CostMatrix::get_min_values_in_cols() const {

    std::vector<cost_t> min_values;

    cost_t min;
    for(std::size_t j = 0; j < matrix_.size(); ++j){
        min = matrix_[0][j];
        for(std::size_t i = 0; i < matrix_.size(); ++i){
            if(matrix_[i][j] < min){
                min = matrix_[i][j];
            }

        }
        if(is_inf(min)){
            min = 0;
        }
        min_values.push_back(min);
    }

    return min_values;
}



/**
 * Reduces rows so that in each column at least one zero value is present.
 * @return Sum of values reduced in columns.
 */

//**********ZROBIONE**********//

cost_t CostMatrix::reduce_cols() {
    std::vector<cost_t> min_values = get_min_values_in_cols();

    for(std::size_t i =0; i<matrix_.size(); ++i){
        for(std::size_t j = 0; j<matrix_[i].size(); ++j){
            if(not is_inf(matrix_[i][j])) {
                matrix_[i][j] = matrix_[i][j] - min_values[j];
            }
        }
    }

    cost_t sum = std::accumulate(min_values.begin(),min_values.end(),0);
    return sum;
}

/**
 * Get the cost of not visiting the vertex_t (@see: get_new_vertex())
 * @param row
 * @param col
 * @return The sum of minimal values in row and col, excluding the intersection value.
 */

//**********ZROBIONE**********//

cost_t CostMatrix::get_vertex_cost(std::size_t row, std::size_t col) const {

    cost_t min_row;
    cost_t min_col;

    if(col == 0){
        min_row = matrix_[row][1];
    }else{
        min_row = matrix_[row][0];
    }
    if(row == 0){
        min_col = matrix_[1][col];
    }else{
        min_col = matrix_[0][col];
    }


    for(std::size_t j = 0; j < matrix_[row].size();++j){
        if(j != col){
            if(matrix_[row][j] < min_row){
                min_row = matrix_[row][j];
            }
        }
    }

    for(std::size_t j = 0; j < matrix_.size();++j){
        if(j != row){
            if(matrix_[j][col] < min_col){
                min_col = matrix_[j][col];
            }
        }
    }
    cost_t total_sum = min_col + min_row;
    if(is_inf(min_row) || is_inf(min_col)){
        total_sum = INF;
    }

    return total_sum;
}

/* PART 2 */

/**
 * Choose next vertex to visit:
 * - Look for vertex_t (pair row and column) with value 0 in the current cost matrix.
 * - Get the vertex_t cost (calls get_vertex_cost()).
 * - Choose the vertex_t with maximum cost and returns it.
 * @param cm
 * @return The coordinates of the next vertex.
 */
//**********ZROBIONE**********//

NewVertex StageState::choose_new_vertex() {
    cost_t max_cost  = 0;
    std::size_t row = 0;
    std::size_t col = 0;

    cost_matrix_t matrix = matrix_.get_matrix();
    for(std::size_t i = 0; i<matrix.size();++i){
        for(std::size_t j =0; j<matrix.size();++j){
            if(matrix[i][j] == 0){
                if(max_cost<matrix_.get_vertex_cost(i,j)){
                    max_cost = matrix_.get_vertex_cost(i,j);
                    row = i;
                    col = j;
                }

            }

        }
    }

    NewVertex result({row,col},max_cost);
    return result;
}

/**
 * Update the cost matrix with the new vertex.
 * @param new_vertex
 */

//**********ZROBIONE**********//

void StageState::update_cost_matrix(vertex_t new_vertex) {
    for (std::size_t i = 0; i < matrix_.size(); ++i) {
        matrix_[i][new_vertex.col] = INF;
        matrix_[new_vertex.row][i] = INF;
    }
    matrix_[new_vertex.col][new_vertex.row] = INF;
    const unsorted_path_t unsorted_path = get_unsorted_path();
    std::vector<std::size_t> sorted_path;

    std::size_t start;
    std::size_t stop;


    for (const auto vertex: unsorted_path) {
        sorted_path.push_back(vertex.row);
        sorted_path.push_back(vertex.col);

    for(std::size_t amount = 0; amount < unsorted_path.size() - 1 && sorted_path.size() != unsorted_path.size() + 1 ;++amount) {
        for (const auto el: unsorted_path) {
            if (el.row != vertex.row && el.col != vertex.col) {
                if (el.row == sorted_path.back()) {
                    sorted_path.push_back(el.col);

                }
            }
        }
    }
        if (sorted_path.size() == unsorted_path.size() + 1 && sorted_path.size()<matrix_.size()) {
            start = sorted_path.front();
            stop = sorted_path.back();
            matrix_[stop][start] = INF;

        }

        sorted_path.clear();


    }
}
/**
 * Reduce the cost matrix.
 * @return The sum of reduced values.
 */

//**********ZROBIONE**********//

cost_t StageState::reduce_cost_matrix() {
    std::size_t sum_rows = matrix_.reduce_rows();
    std::size_t sum_cols = matrix_.reduce_cols();

    cost_t total_sum = sum_cols + sum_rows;

    return total_sum;
}

/**
 * Given the optimal path, return the optimal cost.
 * @param optimal_path
 * @param m
 * @return Cost of the path.
 */
cost_t get_optimal_cost(const path_t& optimal_path, const cost_matrix_t& m) {
    cost_t cost = 0;

    for (std::size_t idx = 1; idx < optimal_path.size(); ++idx) {
        cost += m[optimal_path[idx - 1]][optimal_path[idx]];
    }

    // Add the cost of returning from the last city to the initial one.
    cost += m[optimal_path[optimal_path.size() - 1]][optimal_path[0]];

    return cost;
}

/**
 * Create the right branch matrix with the chosen vertex forbidden and the new lower bound.
 * @param m
 * @param v
 * @param lb
 * @return New branch.
 */
StageState create_right_branch_matrix(cost_matrix_t m, vertex_t v, cost_t lb) {
    CostMatrix cm(m);
    cm[v.row][v.col] = INF;
    return StageState(cm, {}, lb);
}

/**
 * Retain only optimal ones (from all possible ones).
 * @param solutions
 * @return Vector of optimal solutions.
 */
tsp_solutions_t filter_solutions(tsp_solutions_t solutions) {
    cost_t optimal_cost = INF;
    for (const auto& s : solutions) {
        optimal_cost = (s.lower_bound < optimal_cost) ? s.lower_bound : optimal_cost;
    }

    tsp_solutions_t optimal_solutions;
    std::copy_if(solutions.begin(), solutions.end(),
                 std::back_inserter(optimal_solutions),
                 [&optimal_cost](const tsp_solution_t& s) { return s.lower_bound == optimal_cost; }
    );

    return optimal_solutions;
}

/**
 * Solve the TSP.
 * @param cm The cost matrix.
 * @return A list of optimal solutions.
 */
tsp_solutions_t solve_tsp(const cost_matrix_t& cm) {

    StageState left_branch(cm);

    // The branch & bound tree.
    std::stack<StageState> tree_lifo;

    // The number of levels determines the number of steps before obtaining
    // a 2x2 matrix.
    std::size_t n_levels = cm.size() - 2;

    tree_lifo.push(left_branch);   // Use the first cost matrix as the root.

    cost_t best_lb = INF;
    tsp_solutions_t solutions;

    while (!tree_lifo.empty()) {
        left_branch = tree_lifo.top();
        tree_lifo.pop();

        while (left_branch.get_level() != n_levels && left_branch.get_lower_bound() <= best_lb) {
            // Repeat until a 2x2 matrix is obtained or the lower bound is too high...
            if (left_branch.get_level() == 0) {
                left_branch.reset_lower_bound();
            }

            // 1. Reduce the matrix in rows and columns.
            cost_t new_cost = left_branch.reduce_cost_matrix(); // dTODO (KROK 1)



            // 2. Update the lower bound and check the break condition.
            left_branch.update_lower_bound(new_cost);
            if (left_branch.get_lower_bound() > best_lb) {
                break;
            }

            // 3. Get new vertex and the cost of not choosing it.
            NewVertex new_vertex = left_branch.choose_new_vertex(); // eTODO (KROK 2)
            // 4. eTODO Update the path - use append_to_path method.
            left_branch.append_to_path(new_vertex.coordinates);

            // 5. eTODO (KROK 3) Update the cost matrix of the left branch.
            left_branch.update_cost_matrix(new_vertex.coordinates);

            // 6. Update the right branch and push it to the LIFO.
            cost_t new_lower_bound = left_branch.get_lower_bound() + new_vertex.cost;
            tree_lifo.push(create_right_branch_matrix(cm, new_vertex.coordinates,
                                                      new_lower_bound));
        }

        if (left_branch.get_lower_bound() <= best_lb) {

            // If the new solution is at least as good as the previous one,
            // save its lower bound and its path.
            best_lb = left_branch.get_lower_bound();

            path_t new_path = left_branch.get_path();

            solutions.push_back({get_optimal_cost(new_path, cm), new_path});

        }

    }

    return filter_solutions(solutions); // Filter solutions to find only optimal ones.
}
