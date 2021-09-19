// # 5주차_모음사전
// # https://programmers.co.kr/learn/courses/30/lessons/84512

#include <string>
#include <vector>
#include <assert.h>

using namespace std;

int solution(string word) {
    int n_length = word.length();

    int n_unit_count = ( ( ( 5 + 1 )*5 + 1 )*5 + 1 )*5 + 1; // 첫 번째 글자 기준 781, 156, 31, 6, 1
    for( auto c_letter : word ) {
        switch (c_letter) {
        case 'A':
            n_length += n_unit_count*0; break;
        case 'E':
            n_length += n_unit_count*1; break;
        case 'I':
            n_length += n_unit_count*2; break;
        case 'O':
            n_length += n_unit_count*3; break;
        case 'U':
            n_length += n_unit_count*4; break;
        default:
            assert("Wrong Letter");     break;
        }

        n_unit_count = (n_unit_count - 1) / 5;              // 한 글자씩 넘어갈수록 그에 맞게 사이즈 조절
    }

    return n_length;
}









// A
// AA
// AAA
// AAAA
// AAAAA
// AAAAE
// AAAAI
// AAAAO
// AAAAU
// AAAE
// AAAEA
// AAAEE
// AAAEI
// AAAEO
// AAAEU
// AAAI
// AAAIA
// AAAIE
// AAAII
// AAAIO
// AAAIU
// AAAO
// AAAOA
// AAAOE
// AAAOI
// AAAOO
// AAAOU
// AAAU
