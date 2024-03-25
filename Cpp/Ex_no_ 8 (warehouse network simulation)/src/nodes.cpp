//
// Created by plejc on 19.01.2023.
//
#include <nodes.hpp>


///****************************KLASA ReceiverPreferences****************************///
void ReceiverPreferences::add_receiver(IPackageReceiver* receiver) {

    double probability = 0; //prawdopodopodobieństwo wybrania konkretnego odbiorcy
    preferences_.emplace(std::make_pair(receiver, probability));
    const double const_probobility = 1/preferences_.size();

    for (auto& pair : preferences_)
    {
        pair.second = const_probobility;

    }


//    if(preferences_.empty())
//    {
//        preferences_[receiver] = 1.0;
//    }
//    else
//    {
//        preferences_[receiver] = probability;
//    }
//
//    for(auto &pair : preferences_)
//    {
//        probability_sum += pair.second;
//    }
//    if(probability_sum != 1)
//    {
//        std::cout<<" sum of probabilities != 1 ";
//        //tu powinna być funkcja, która przeskaluje odpowiednio prawdopodobieństwo
//        //ale to nie takie proste i piszą, żeby się nią nie przejmować xdd
//    }
}


void ReceiverPreferences::remove_receiver(IPackageReceiver* receiver){

    if(preferences_.find(receiver) != preferences_.end())
    {
        const_iterator it;
        it = preferences_.find(receiver);
        preferences_.erase(it);

        const double const_probobility = 1/preferences_.size();

        for (auto& pair : preferences_)
        {
            pair.second = const_probobility;

        }
    }

//    for(auto &pair : preferences_)
//    {
//        probability_sum += pair.second;
//    }
//    if(probability_sum != 1)
//    {
//        std::cout<<" sum of probabilities != 1 ";
//        //tu powinna być funkcja, która przeskaluje odpowiednio prawdopodobieństwo
//
//    }

};

IPackageReceiver* ReceiverPreferences::choose_receiver()
{
    const double rand_val = pg_();
    double min_val = 0.0;
    for( const auto& pair : preferences_)//przejście preferncji po parze <wsk. na odbiorce - prawdopodobienstwo>
    { min_val += pair.second;
        if(rand_val <= min_val){
            return pair.first;
        }
    }
    return nullptr;
};


///****************************KLASA PackageSender****************************///
void PackageSender::send_package() {
    if(buffer_.has_value()) {
        IPackageReceiver* receiver = receiver_preferences_.choose_receiver();
        receiver -> receive_package(std::move(buffer_.value()));
        buffer_.reset();
    }

}

///****************************KLASA IPackageReceiver****************************///


///****************************KLASA Ramp****************************///
void Ramp::deliver_goods(Time t) {
    if (t % di_ == 0) {
        send_package();
    } else if (get_sending_buffer().has_value() == false) {
        push_package(Package());
    }

}

///****************************KLASA Worker****************************///
void Worker::do_work(Time t){
    if(t >= package_processing_start_time + pd_){
        send_package();
    }

    if(get_sending_buffer().has_value() == false && q_->size() != 0)
    {
        push_package(q_->pop());
        package_processing_start_time = t;
    }
}

void Worker::receive_package(Package&& p){
    q_->push(std::move(p));
}

///****************************KLASA Storehouse****************************///
void Storehouse::receive_package(Package&& p)
{
    d_->push(std::move(p));
}