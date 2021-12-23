#include<iostream>
#include<bitset>
#include<string>
#include<vector>
#include<stdio.h>
#define N 8

using namespace std;
void multiplicationX(bitset<8> *bits){
    bitset<N> res;
    if(!(*bits).test(7)){
        *bits <<= 1;
    }
    else{
        bitset<N> aux(string("00011011"));
        (*bits<<=1) ^= aux;
    }
}

int main(){
	string fx,gx;
    vector<bitset<N>> resParciales;
    
    while(true){
	    cout<<"\nenter the binary coefficients of f(x): ";
	    cin>>fx;
	    cout<<"\nenter the binary coefficients of g(x): ";
	    cin>>gx;   
		
	    bitset<N> bitsF(fx), bitsG(gx),aux,fxgx;
	    
	    for(int i = (N - 1); i > 0; i--){
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
	    cout<<"\nf(x)g(x) mod m(x) = "<<fxgx<<"\n"<<endl;
	}
    return 0;
}