//
// Created by majka on 06.01.2023.
//
#include "storage_types.hpp"
#include <iostream>


PackageQueueType PackageQueue::get_queue_type() const  {
    return queue_type_;
}

Package PackageQueue::pop() {
    Package result;

    switch (queue_type_) {
        case PackageQueueType::FIFO:
            result = std::move(*(std::begin(packages_list_)));
            packages_list_.pop_front();
            return result;
        case PackageQueueType::LIFO:
            result = (std::move(*(std::end(packages_list_))));
            packages_list_.pop_back();
            return result;
        default:
            return EXIT_FAILURE;

    }

}

void PackageQueue::push(Package&& package) {
    switch (queue_type_) {
        case PackageQueueType::FIFO:
            packages_list_.emplace_back(std::move(package));
            break;
        case PackageQueueType::LIFO:
            packages_list_.emplace_front(std::move(package));
            break;
        default:
            break;
    }

}
bool PackageQueue::empty() const {
    return packages_list_.empty();

}
std::size_t PackageQueue::size() const {
    return packages_list_.size();
}

std::string PackageQueue::str_type(){
    switch (queue_type_) {
        case PackageQueueType::FIFO:
            return "FIFO";
        case PackageQueueType::LIFO:
            return "LIFO";
        default:
            return "ERROR TYPE";
    }

}
