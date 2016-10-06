#pragma comment(linker, "/STACK:63777216")
#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <cstring>
#include <cstring>
#include <stdlib.h>
#include <sstream>
#include <fstream>
#include <map>
#include <algorithm>
#include <assert.h>
#include <set>
#define mp make_pair
#define inf 2000000007
using namespace std;

ifstream in("hw6.txt");

//const int ht_size = 1000*1000*100*3;
//
//int abs (int v) {
//    return v < 0 ? -v : v;
//}
//
//int main() {
//    vector < long long > ve;
//    vector < set <long long> > ht(ht_size); //6GB RAM =)
//    long long cur;
//    while (in >> cur) {
//        int hash = abs((int)(cur % ht_size));
//        if (ht[hash].find(cur) == ht[hash].end()){
//            ht[hash].insert(cur);
//            ve.push_back(cur);
//        }
//    }
//    
//    long long ans = 0;
//    int i = 0;
//    for (int t = -10000; t <= 10000; ++t){
//        bool flag = false;
//        if (i%100 == 0){
//            cout << t << " " << ans << endl;
//        }
//        i+=1;
//        for (int j = 0; j < ve.size(); ++j){
//            if (t - ve[j] != ve[j]){
//                int hash = abs((int)(t - ve[j]) % ht_size);
//                if (ht[hash].find(t - ve[j]) != ht[hash].end()){
//                    flag = true;
//                    break;
//                }
//            }
//        }
//        if (flag)
//            ans ++;
//    }
//    
//    cout << ans;
//    return 0;
//}

vector < long long > ve;
int bin(long long v){
    int ans = -1;
    int l = 0, r = (int)ve.size()-1;
    while(l <= r){
        int mid = (l+r) >> 1;
        if (v == ve[mid]){
            ans = mid; break;
        }
        if (v > ve[mid]){
            l = mid + 1;
        }
        else {
            r = mid - 1;
        }
    }
    return ans;
}

int main() {
    long long cur;
    set < long long > s;
    while (in >> cur) {
        if (s.find(cur) == s.end()){
            s.insert(cur);
            ve.push_back(cur);
        }
    }

    sort(ve.begin(),ve.end());
    
    int ans = 0;
    int i = 0;
    bool flag = false;
    
    for (int t = -10000; t <= 10000; ++t){
        if (i%100 == 0){
            cout << t << " " << ans << endl;
        }
        i+=1;
        
        for (int j = 0; j < ve.size(); ++j){
            if (t - ve[j] != ve[j]){
                if (bin(t-ve[j]) != -1){
                    flag = true;
                    break;
                }
            }
        }
        if (flag){
            ans ++;
        }
        flag = false;
    }
    cout << ans;
    return 0;
}

