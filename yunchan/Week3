#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int solution(int n) {
    // 10진수를 3진수로 변환
    string base_3 = "";
    while (n > 0) {
        base_3 += to_string(n % 3);
        n /= 3;
    }
    
    // 3진수를 뒤집기
    reverse(base_3.begin(), base_3.end());
    
    // 뒤집힌 3진수를 10진수로 변환
    int result = 0;
    int power = 1;
    for (int i = 0; i < base_3.length(); i++) {
        result += (base_3[i] - 48) * power;
        power *= 3;
    }
    
    return result;
}
