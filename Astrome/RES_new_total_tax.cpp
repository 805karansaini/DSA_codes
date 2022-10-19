#include <iostream>
#include <bits/stdc++.h>
#include<cmath>
using namespace std;

int check(double gross_amount,double net_amount, double tax_rate, double slab_amount, double base_tax){
    double total_tax, tax_rebate, final_tax;
    total_tax = (((gross_amount-slab_amount) * tax_rate)/100) + base_tax;
    tax_rebate = (total_tax*total_tax) / gross_amount;
    final_tax = total_tax - tax_rebate;
    // cout<< ( -0.001 <= ((gross_amount-final_tax) - net_amount) <= 0.001) << " " << (gross_amount-final_tax) << " " << net_amount << endl;
    if ( ((gross_amount - final_tax) - net_amount) <= 0.000){
        // cout << "returned 1  " << height <<  endl;
        return 1;
        }
    else{
        // cout << "Returned -1  " << height <<  endl;
        return -1;
        }
    
    }

int main(){
    std::cout.precision(2);
    long double net_amount, tax_rate, slab_amount, base_tax;
    cin >> net_amount;
    cin >> tax_rate;
    cin >> slab_amount;
    cin >> base_tax;
    if (net_amount < slab_amount){
      cout<<fixed << base_tax << endl;
      return 0;
    }

    long long int low, high, gross_amount;
    int value;
    low = (int)floor(net_amount);
    high = INT_MAX;
    // cout << "START" << endl;
    
    while (low <= high){
        gross_amount = (int)(low + ((high - low) / 2));
        // cout<<fixed << low << " : " << high << " : " <<  gross_amount <<endl;
        
        value = check(gross_amount,net_amount, tax_rate, slab_amount, base_tax);
        // cout<<fixed << "Value : " <<  value <<endl;
        if (value == 1){
            low = gross_amount + 1 ;
        } 
        else if (value == -1){
            high = gross_amount - 1;
        }
        
    }
    

    // cout << " NNNNNEEEEEWWWWWWW START " << endl;
    long double  new_low = min(low,high);
    long double new_high = max(low,high);
    long double dgross_amount;
    while (new_low <= new_high){
        dgross_amount = (new_low + ((new_high - new_low) / 2));
        value = check(dgross_amount,net_amount, tax_rate, slab_amount, base_tax);
        if (value == 1){
            new_low = dgross_amount + 0.01 ;
        } 
        else if (value == -1){
            new_high = dgross_amount - 0.01;
        }
    }
    
    // cout << " NNNNNEEEEEWWWWWWW START " << endl;
    long double low_range, high_range;
    low_range = min(new_low, new_high) - 0.50;
    high_range = max(new_low, new_high) + 0.50;
    // cout << "Low High range : " << low_range << "  " << high_range << endl;
    for(long double i = low_range; i <= high_range; i = i+0.01){
        if ( check(i, net_amount, tax_rate, slab_amount, base_tax) == -1 ){
                double total_tax, tax_rebate, final_tax;
                total_tax = (((new_high-slab_amount) * tax_rate)/100) + base_tax;
                cout<<fixed << total_tax << endl;
                return 0;
        }
    }
}