#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main(){
  int n;
  cin >> n;
  while(n--){
    int m;
    cin >> m;
    int array[m];
    for(int i=0; i<m; i++){
      cin >> array[i];
  }
  int sal = accumulate(array, array+m, 0);
  cout << sal << endl;

}
}