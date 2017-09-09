#include <cmath>
#include <vector>
#include <iostream>

using namespace std;

#define MAX_N 65536
bool es_primo[MAX_N+1] = {true};
vector<int> primos;

void marcar_multiplos(int step, int max_n){
	for(int i=step; i<=max_n; i+=step){
		es_primo[i] = false;
	}
}

void criba(int max_n){
	primos.push_back(1);
	for(int i=2; i<=max_n; i++){
		if(es_primo[i]){
			primos.push_back(i);
			marcar_multiplos(i, max_n);
		}
	}
}

int main(){
	criba(MAX_N);
	int T;
	cin >> T;
	while(T!=0){
		int root = sqrt(T)+1;
		bool apagada = false;
		cout << "primos len " << primos.size() << endl;
		for(int p : primos){
			if(p>root) {
				cout << "break: p=" << p << ", root=" << root << endl;
				break;
			}
			if((T%p)==0) {
				cout << T << " % " << p << " = " << T%p << endl;
				apagada = not apagada;
			}
		}
		if(apagada)
			cout << "no" << endl;
		else
			cout << "yes" << endl;
		cin >> T;
	}
	return 0;
}

