#include <iostream>
#include <string>
using namespace std;

int main() {
    long long n;
    cin >> n;
    std::string str("");

    while(n > 0) {
        if(n % 2 == 0) {
            str = "B" + str;
            n = n / 2;
        }
        else {
            str = "A" + str;
            n = n - 1;
        }
    }

    cout << str << endl;
}