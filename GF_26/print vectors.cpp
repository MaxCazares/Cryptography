#include<iostream>
#include<bitset>
#include<string>
#include<vector>
using namespace std;


int main(){
	string fx = "000011", gx = "001111"; 
    vector<bitset<6>> resParciales;
    bitset<6> bitsF(fx), bitsG(gx);
    
    resParciales.push_back(bitsF);
    
    for(int i = 0; i<resParciales.size();i++){
    	cout<<"\n"<<resParciales[i]<<endl;
	}
	
	resParciales.push_back(bitsG);
	for(int i = 0; i<resParciales.size();i++){
    	cout<<""<<resParciales[i]<<endl;
	}
}
