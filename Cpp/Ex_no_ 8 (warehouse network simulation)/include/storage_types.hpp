//
// Created by majka on 06.01.2023.
//

#ifndef INC_7_TEMAT_SYMULACJA_SIECI__STORAGE_TYPES_HPP
#define INC_7_TEMAT_SYMULACJA_SIECI__STORAGE_TYPES_HPP



#include <list>
#include <numeric>
#include <ostream>
#include "package.hpp"
#include "types.hpp"

class Package;

enum class PackageQueueType {
    FIFO, LIFO
};

class IPackageStockpile{
public:
    using const_iterator = std::list<Package>::const_iterator;


    virtual void push(Package&& package) = 0;
    virtual bool empty() const = 0;
    virtual std::size_t size() const = 0;

    virtual const_iterator begin() const = 0;
    virtual const_iterator end() const = 0;
    virtual const_iterator cbegin() const  = 0;
    virtual const_iterator cend() const = 0;


    virtual ~IPackageStockpile() = default;
};

class IPackageQueue : public IPackageStockpile{
public:
    virtual Package pop() = 0;
    virtual PackageQueueType get_queue_type() const = 0;
};

class PackageQueue : public IPackageQueue{
public:
    PackageQueue(PackageQueueType queue_type) :queue_type_(queue_type) {};


    Package pop() override;
    PackageQueueType get_queue_type() const override;
    void push(Package&& package) override;
    bool empty() const override;
    std::size_t size() const override;

    std:: string str_type();

    const_iterator cbegin() const override{return packages_list_.cbegin();}
    const_iterator cend() const override {return packages_list_.cend();}
    const_iterator begin() const override {return packages_list_.cbegin();}
    const_iterator end() const override {return packages_list_.cend();}



private:
    PackageQueueType queue_type_;
    ElementList packages_list_;

};





#endif //INC_7_TEMAT_SYMULACJA_SIECI__STORAGE_TYPES_HPP
