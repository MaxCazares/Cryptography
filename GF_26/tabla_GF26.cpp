#include <iostream>
#include <bitset>
#include <string>
#include <vector>
#include <stdio.h>
#include <fstream>

using namespace std;
void multiplicationX(bitset<6> *bits){
    bitset<6> res;
    if(!(*bits).test(5))
        *bits <<= 1;
    else{
        bitset<6> aux(string("000011"));
        (*bits<<=1) ^= aux;
    }
}

bitset<6> MulGF26(int f, int g){
	vector<bitset<6>> resParciales;
	bitset<6> bitsF(f), bitsG(g),aux,fxgx;
	
	for(int i = 5; i > 0; i--){
        aux = bitsF;
        if(bitsG.test(i)){
            for(int j = i; j > 0; j--)
                multiplicationX(&aux);  
            resParciales.push_back(aux); 
        }
    }

    if(bitsG.test(0))
        resParciales.push_back(bitsF);
	
    fxgx = resParciales[0];  
    for(int i = 1; i < resParciales.size(); i++){
        fxgx ^= resParciales[i];
    }
	return fxgx;	
}

int main(){
	ofstream archivo;
    archivo.open("tablaGF26.txt");
    
	int tam = 63;
	bitset<6> matriz[tam][tam];
	for(int i = 1; i <= tam; i++){
		for(int j = 1; j <= tam; j++){
			matriz[i-1][j-1] = MulGF26(i, j);
		}
	}
	
	for(int i = 0; i < tam; i++){
		for(int j = 0; j < tam; j++){
			archivo<<"producto: "<<matriz[i][j];
			archivo<<"\t";
		}
		archivo<<"\n";
	}
	archivo.close();    
    return 0;
} 