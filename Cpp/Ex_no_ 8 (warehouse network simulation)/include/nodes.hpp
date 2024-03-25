//
// Created by plejc on 19.01.2023.
//

#ifndef INC_7_TEMAT_SYMULACJA_SIECI__NODES_HPP
#define INC_7_TEMAT_SYMULACJA_SIECI__NODES_HPP

#include "helpers.hpp"
#include "storage_types.hpp"
#include <optional>
#include <map>
#include <memory>



enum class ReceiverType{
    Ramp,
    Worker,
    Storehouse
};

class IPackageReceiver{
public:
    virtual void receive_package(Package&& p)  = 0;
    virtual ElementID get_id() const = 0;

    virtual IPackageStockpile::const_iterator begin() const = 0;
    virtual IPackageStockpile::const_iterator end() const = 0;
    virtual IPackageStockpile::const_iterator cbegin() const  = 0;
    virtual IPackageStockpile::const_iterator cend() const = 0;

};

//class Storehouse{
//public:
//
//};

class ReceiverPreferences{
public:
    ReceiverPreferences(ProbabilityGenerator pg = probability_generator) : pg_(pg) {}

    using preferences_t = std::map<IPackageReceiver*, double>;
    using const_iterator = preferences_t::const_iterator;

    void add_receiver(IPackageReceiver* receiver); //dodanie odbiorcy(suma prawdopodobieństw =1)
    void remove_receiver(IPackageReceiver* receiver);
    IPackageReceiver* choose_receiver();
    const preferences_t& get_preferences() { return preferences_;};

    const_iterator begin() const {return preferences_.cbegin();};
    const_iterator cbegin() const {return preferences_.cbegin();};
    const_iterator end() const {return preferences_.cend();};
    const_iterator cend() const {return preferences_.cend();};


private:
    ProbabilityGen pg_;
    preferences_t preferences_;
};

class PackageSender{
public:
    PackageSender() = default;
    PackageSender(PackageSender&&) = default;
    PackageSender(Package&) = delete;

    void send_package();
    const std::optional<Package> get_sending_buffer() const{return buffer_;};
    ReceiverPreferences receiver_preferences_;
protected:
    void push_package(Package&& package){buffer.emplace(std::move(package));}

private:
    std::optional<Package> buffer_;
};

class Ramp : public PackageSender
        {
public:
    Ramp(ElementID id, TimeOffset di) : id_(id), di_(di) {}
    void deliver_goods(Time t);
    TimeOffset get_delivery_interval() const {return di_;}
    ElementID get_id() const {return id_;}

private:
    ElementID id_;
    TimeOffset di_;
};

class Worker : public IPackageReceiver, public PackageSender{
public:
    Worker(ElementID id, TimeOffset pd, std::unique_ptr<IPackageQueue> q) : id_(id), pd_(pd), q_(std::move(q)), package_processing_start_time(0) {}
    virtual void receive_package(Package&& p) override;
    virtual ElementID get_id() const override{ return id_;}
    void do_work(Time t);
    TimeOffset get_processing_duration() const {return pd_;}
    Time get_package_processing_start_time() const {return package_processing_start_time_;}

    virtual IPackageStockpile::const_iterator begin() const override { return q_->cbegin(); }
    virtual IPackageStockpile::const_iterator end() const override { return q_->cend(); }
    virtual IPackageStockpile::const_iterator cbegin() const override { return q_->cbegin(); }
    virtual IPackageStockpile::const_iterator cend() const override { return q_->cend(); }
private:
    ElementID id_;
    TimeOffset pd_;
    std::unique_ptr<IPackageQueue> q_;
    Time package_processing_start_time;
};

class Storehouse : public IPackageReceiver{
public:
    Storehouse(ElementID id, std::unique_ptr<IPackageStockpile> d = std::make_unique<PackageQueue>(PackageQueueType::FIFO)) : id_(id), d_(std::move(d)) {};
    virtual void receive_package(Package&& p) override;
    virtual ElementID get_id() const override { return id_; }
    virtual IPackageStockpile::const_iterator begin() const override { return d_->cbegin(); }
    virtual IPackageStockpile::const_iterator end() const override { return d_->cend(); }
    virtual IPackageStockpile::const_iterator cbegin() const override { return d_->cbegin(); };
    virtual IPackageStockpile::const_iterator cend() const override { return d_->cend(); };
private:
    ElementID id_;
    std::unique_ptr<IPackageStockpile> d_;
};

#endif //INC_7_TEMAT_SYMULACJA_SIECI__NODES_HPP
