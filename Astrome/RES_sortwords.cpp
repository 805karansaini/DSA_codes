#include<bits/stdc++.h>
#include <iostream>
#include<vector>
using namespace std;

bool sortDecr(char a,char b){
    return a>b;
}

bool sortIncr(char a,char b){
    return a<b;
}

vector <string> adv_tokenizer(string s, char del)
{   
    vector <string> colours;
    stringstream ss(s);
    string word;
    while (!ss.eof()) {
        getline(ss, word, del);
        colours.push_back(word);
    }
    return colours;
}

string sortCharDec(string &str){
  sort(str.begin(), str.end(),sortDecr);
  return str;
}

string sortCharIncr(string &str){
  sort(str.begin(), str.end(),sortIncr);
  return str;
}

int main(){
    string s;
    vector <string> words;
    getline(cin,s);
    words = adv_tokenizer(s, '-');
    int n = words.size();
    for(int i=0; i<n;++i){
        transform(words[i].begin(), words[i].end(), words[i].begin(), ::tolower);
    }
    sort(words.begin(), words.end());
    char c = 'a';
    int a_v = (int)c;
    for(int i=0; i<n;++i){
        int m = words[i].size();
        int temp = 0;
        for(int j=0; j<m;++j){
            temp += ( ( (int)words[i][j] ) - a_v + 1);
        }
        if (temp%2 == 0){
            sortCharIncr( words[i] );
        }
        else{
            sortCharDec( words[i] );
        }
    }
    int i = 0;
    for(i; i<n-1;i++){
        cout << words[i] << "-";
    }
    cout << words[i] ;
    return 0;
}