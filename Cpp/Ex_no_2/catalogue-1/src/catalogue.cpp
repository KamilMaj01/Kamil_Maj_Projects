//
// Created by majka on 30.03.2022.
//
#include "catalogue.hpp"

#include <iomanip>

std::string to_string(const Product& product){
    std::ostringstream full_name;
    full_name << std::fixed << std::setprecision(2);
    full_name<<product.get_name()<<" "<<"["<<product.get_id()<<"] : $"<<product.get_price();

    return full_name.str();


}


std::vector<Product> Catalogue::get_products_with_appropriate_price(std::function<bool (double)> prices)const{
    std::vector<Product> product_result;

    for(const auto& el : inventory_){
        const auto& product = el.second;
        if(prices(product.get_price())){
            product_result.push_back(product);
        }


    }

return product_result;
}

std::vector<Product> Catalogue::get_products_by_name_part(std::string substr, bool is_case_sensitive) const{
    std::vector<Product> product_result;
    for(const auto& el : inventory_){
        const auto& product = el.second;
        std::string name = product.get_name();

        std::string transformed_name = name;
        std::string chunk_transformed = substr;

        if( !is_case_sensitive){
            std::transform(name.begin(), name.end(), transformed_name.begin(), ::tolower );
            std::transform(substr.begin(), substr.end(), chunk_transformed.begin(), ::tolower);
        }

        bool result = (transformed_name.find(chunk_transformed) != std::string::npos);

        if(result){
            product_result.push_back(product);
        }





    }
    return product_result;
}