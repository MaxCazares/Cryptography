#include <iostream>
#include <iomanip>
#include "cryptopp/modes.h"
#include "cryptopp/aes.h"
#include "cryptopp/filters.h"
#include <fstream>

using namespace std;

string openFile(string file){
    string ans = "";
    fstream myfile;
    myfile.open(file, ios::in);
    if(myfile.is_open()){
        string line;
        while(getline(myfile,line)){
            ans+=line;
        }
        myfile.close();
    }
    return ans;
}

void saveFile64(string text, string file){
    fstream myfile;
    myfile.open(file, ios::out);
    if(myfile.is_open()){
            myfile << text;
        myfile.close();
    }
}

void saveFileH(string text, string file){
    fstream myfile;
    myfile.open(file, ios::out);
    if(myfile.is_open()){
        for( long unsigned int i = 0; i < text.size(); i++ ) {
            myfile << "0x" <<  hex << (0xFF & static_cast<byte>(text[i])) << " ";
        }
        myfile.close();
    }
}

void saveFile(string text, string file){
    fstream myfile;
    myfile.open(file, ios::out);
    if(myfile.is_open()){
        for( long unsigned int i = 0; i < text.size(); i++ ) {
            myfile << text[i];
        }
        myfile.close();
    }
}

int main(){
/*
    byte key[AES::DEFAULT_KEYLENGTH] = {0x01,0x23,0x45,0x67,0x89,0xab,0xcd,0xef, 0x23,0x45,0x67,0x89,0xab,0xcd,0xef,0x01};
    byte iv[AES::BLOCKSIZE] = {0x12,0x34,0x56,0x78,0x90,0xab,0xcd,0xef, 0x34,0x56,0x78,0x90,0xab,0xcd,0xef,0x12};
*/
    byte key[ CryptoPP::AES::DEFAULT_KEYLENGTH ], iv[ CryptoPP::AES::BLOCKSIZE ];
    memset( key, 0x00, CryptoPP::AES::DEFAULT_KEYLENGTH );
    memset( iv, 0x00, CryptoPP::AES::BLOCKSIZE );
    
    // For Plain Text
    string file;
    string plaintext;
    string ciphertext;
    string decryptedtext;

    cout << "Plain text document: ";
    cin >> file;
    plaintext = openFile(file);

    //Cipher
    CryptoPP::AES::Encryption aesEncryption(key, CryptoPP::AES::DEFAULT_KEYLENGTH);
    CryptoPP::CBC_Mode_ExternalCipher::Encryption cbcEncryption( aesEncryption, iv );

    CryptoPP::StreamTransformationFilter stfEncryptor(cbcEncryption, new CryptoPP::StringSink( ciphertext ) );
    stfEncryptor.Put( reinterpret_cast<const unsigned char*>( plaintext.c_str() ), plaintext.length() + 1 );
    stfEncryptor.MessageEnd();

    //For Cipher Text
    cout << "Cipher text document: ";
    cin >> file;
    saveFileH(ciphertext,file);
    
    // Decrypted
    CryptoPP::AES::Decryption aesDecryption(key, CryptoPP::AES::DEFAULT_KEYLENGTH);
    CryptoPP::CBC_Mode_ExternalCipher::Decryption cbcDecryption( aesDecryption, iv );

    CryptoPP::StreamTransformationFilter stfDecryptor(cbcDecryption, new CryptoPP::StringSink( decryptedtext ) );
    stfDecryptor.Put( reinterpret_cast<const unsigned char*>( ciphertext.c_str() ), ciphertext.size() );
    stfDecryptor.MessageEnd();

    // For Decrypted Text
    cout << "Decrypted text document: ";
    cin >> file;
    saveFile(decryptedtext,file);
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


