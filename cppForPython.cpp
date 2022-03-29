#include <cmath>

bool is_prime(int n){
    if (n <= 1) {
        return false;
    } else if (n == 2) {
        return true;
    } else if (n % 2 == 0) {
        return false;
    }
    int sqrt_n = (int) sqrt(n);
    for (int i = 3; i <= sqrt_n; i += 1) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;

}

extern "C" {
    __declspec(dllexport) bool is_prime_cpp(int n) {
        return is_prime(n);
    }
}