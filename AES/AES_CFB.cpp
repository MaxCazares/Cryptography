// g++ -g3 -ggdb -O0 -DDEBUG -I/usr/include/cryptopp qwerty.cpp -o qwerty -lcryptopp -lpthread
// g++ -g -O2 -DNDEBUG -I/usr/include/cryptopp qwerty.cpp -o qwerty.exe -lcryptopp -lpthread

#include "osrng.h"
using CryptoPP::AutoSeededRandomPool;

#include <iostream>
using std::cout;
using std::cerr;
using std::endl;

#include <string>
using std::string;

#include <cstdlib>
using std::exit;

#include "cryptlib.h"
using CryptoPP::Exception;

#include "hex.h"
using CryptoPP::HexEncoder;
using CryptoPP::HexDecoder;

#include "filters.h"
using CryptoPP::StringSink;
using CryptoPP::StringSource;
using CryptoPP::StreamTransformationFilter;
using CryptoPP::HashFilter;

#include "aes.h"
using CryptoPP::AES;

#include "modes.h"
using CryptoPP::CFB_Mode;

#include <fstream>
using std::fstream;
using std::ofstream;
using std::ifstream;

using std::vector;
using std::cin;

#include "hmac.h"
using CryptoPP::HMAC;

#include "sha.h"
using CryptoPP::SHA256;

#include "base64.h"
using CryptoPP::Base64Encoder;

void saveFiel(string data, string filename){

    fstream file_out;
    file_out.open(filename, std::ios_base::out);
    if (!file_out.is_open()) {
        cout << "failed to open " << filename << '\n';
    } else {
        file_out << data << endl;
    }
}

string openFile(string filename){
    string ans = "";
    vector<string> lines;
    string line;

    ifstream input_file(filename);
    if (!input_file.is_open()) {
        cerr << "Could not open the file"<< endl;
    }
    while (getline(input_file, line)){
        lines.push_back(line);
        ans+=line;
    }
    input_file.close();
    return ans;
}

int main(int argc, char* argv[])
{

/*
    byte key[AES::DEFAULT_KEYLENGTH] = {0x01,0x23,0x45,0x67,0x89,0xab,0xcd,0xef, 0x23,0x45,0x67,0x89,0xab,0xcd,0xef,0x01};
    byte iv[AES::BLOCKSIZE] = {0x12,0x34,0x56,0x78,0x90,0xab,0xcd,0xef, 0x34,0x56,0x78,0x90,0xab,0xcd,0xef,0x12};
*/
	AutoSeededRandomPool prng;

	byte key[AES::DEFAULT_KEYLENGTH];
    byte iv[AES::BLOCKSIZE];
    
	prng.GenerateBlock(key, sizeof(key));
	prng.GenerateBlock(iv, sizeof(iv));


    string file, cipher, encoded, recovered, plain, filename;

        //PlainText
        cout << "Plaintext: ";
        cin >> file;
        plain = openFile(file);

	    //Key
	    encoded.clear();
	    StringSource(key, sizeof(key), true,
            new HexEncoder(new StringSink(encoded))); 

        cout << "Key: ";
        cin >> filename;
        saveFiel(encoded,filename);

	    //Iv
	    encoded.clear();
	    StringSource(iv, sizeof(iv), true,
		    new HexEncoder(new StringSink(encoded)));
        cout << "IV: ";
        cin >> filename;
        saveFiel(encoded,filename);

        //Cipher
	    	CFB_Mode< AES >::Encryption e;
	    	e.SetKeyWithIV(key, sizeof(key), iv);
		    StringSource(plain, true, 
			    new StreamTransformationFilter(e,new StringSink(cipher)));

	    //Saved
	    encoded.clear();
	    StringSource(cipher, true,
		    new HexEncoder(new StringSink(encoded)));
        cout << "Cipher: ";
        cin >> filename;
        saveFiel(encoded,filename);


        //Decrypted
	    	CFB_Mode< AES >::Decryption d;
		    d.SetKeyWithIV(key, sizeof(key), iv);
		    StringSource s(cipher, true, 
			    new StreamTransformationFilter(d,new StringSink(recovered)));
        
        
        
        
        //Saved
            cout << "Decrypted: ";
            cin >> filename;
            saveFiel(recovered,filename);
	return 0;
}

/*
    //Cipher
    cout << "Encoded Base64: ";
    cin >> file;
    CryptoPP::StringSource scipher(ciphertext, true, 
    new CryptoPP::Base64Encoder(new CryptoPP::StringSink(encoded)));
    saveFile64(encoded,file);

    // Decrypt
    cout << "Decode Base64: ";
    cin >> file;
    decoded = openFile(file);
    CryptoPP::StringSource sencoded(encoded, true,
    new CryptoPP::Base64Decoder(new CryptoPP::StringSink(decoded)));
*/