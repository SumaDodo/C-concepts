#include <iostream>
#include <vector>

int main() {

    vector<int> vec;

    std::cout << "before"<<vec.size()<<endl;

    for (int i =0;i<5;i ++)
    {
        vec.push_back(i);
    }

    std::cout << "After size" << vec.size()<<endl;

    //Using iterator to access the values
    vector<int>::iterator v = vec.begin();
    while(v !=vec.end()){
        std::cout<<"value of v" << *v <<endl;
    }
    return 0;
}
