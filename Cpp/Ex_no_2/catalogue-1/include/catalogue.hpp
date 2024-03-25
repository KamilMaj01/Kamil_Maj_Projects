//
// Created by majka on 30.03.2022.
//

#ifndef CATALOGUE_1_CATALOGUE_HPP
#define CATALOGUE_1_CATALOGUE_HPP

#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <functional>
#include <cctype>
#include <clocale>
#include <algorithm>


class Product {
public:
    Product(std::string id, std::string name, double price) : id_(id), name_(name), price_(price){}

    std::string get_id() const { return id_;}
    std::string  get_name() const { return name_;}
    double get_price() const { return price_;}


private:
    std::string id_;
    std::string name_;
    double price_;

};



std::string to_string(const Product& product);

class Catalogue {
public:
    using inventory_t = std::map<std::string, Product>;
    Catalogue(const inventory_t& inventory = inventory_t{}) : inventory_(inventory){}

    void add_product(const Product& product){ inventory_.emplace(product.get_id(), product);}

    bool contains(std::string id){ return inventory_.find(id) != inventory_.end() ; }

    std::vector<Product> get_products_with_appropriate_price(std::function<bool (double)> prices)const;
    std::vector<Product> get_products_by_name_part(std::string substr, bool is_case_sensitive) const;


private:
    inventory_t inventory_;

};





#endif //CATALOGUE_1_CATALOGUE_HPP
