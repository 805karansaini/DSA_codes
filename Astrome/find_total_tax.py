# //  Dear Sir/madam, I did not know that the PER UNIT SCORE would be reduced if i get compilations error.
# // its 6:21 Am i have been trying to solve it now for some time.. Just beacuse i am bit sleepy right now and forgot to add ";" thats why i have error and my per unit score was reduced to 0.6
# // its my fault  but i didnt even know my per unit score would be reduced.
# // but ok 


# #include <iostream>

# using namespace std;
# int check(double gross_amount,double net_amount, double tax_rate, double slab_amount, double base_tax){
#     double total_tax, tax_rebate, final_tax;
#     total_tax = (((gross_amount-slab_amount) * tax_rate)/100) + base_tax;
#     tax_rebate = (total_tax*total_tax) / gross_amount;
#     final_tax = total_tax - tax_rebate;
#     // cout<< ( -0.001 <= ((gross_amount-final_tax) - net_amount) <= 0.001) << " " << (gross_amount-final_tax) << " " << net_amount << endl;
#     if (net_amount  == gross_amount - final_tax){
#         return 1;
#         }
#     else if ( net_amount  > gross_amount - final_tax){
#         return 2;
#         }
#     else{
#         return 3;
#         }
#     }

# int main(){
#     std::cout.precision(2);
#     double net_amount, tax_rate, slab_amount, base_tax;
#     cin >> net_amount;
#     cin >> tax_rate;
#     cin >> slab_amount;
#     cin >> base_tax;
#     double gross_amount;
#     double calculated_gross_amount = -1000;
#     int low, high;
#     int value;
#     low = (int)(net_amount + base_tax);
#     high = 1000000000;
#     // cout << "START" << endl;
#     while (low <= high){
#         gross_amount = (int)(low + ((high - low) / 2));
#         // cout<<fixed << low << " : " << high << " : " <<  gross_amount <<endl;
        
#         value = check(gross_amount,net_amount, tax_rate, slab_amount, base_tax);
#         // cout<<fixed << "Value : " <<  value <<endl;
#         if (value == 1){
#             calculated_gross_amount = gross_amount;
#             break;
#         } 
#         else if (value == 2){
#             low = gross_amount + 1;
#         }
#         else if ( value == 3){
#             high =  gross_amount - 1;
#         }
#     }
#     if (calculated_gross_amount != -1000){
#         double total_tax, tax_rebate, final_tax;
#         total_tax = (((calculated_gross_amount-slab_amount) * tax_rate)/100) + base_tax;
#         cout<<fixed << total_tax << endl;
#         return 0;
#     }
#     // cout << " NNNNNEEEEEWWWWWWW START " << endl;
#     double new_low = min(low,high);
#     double new_high = max(low,high);
#     // cout << new_low << " " << new_high;
#     bool flag = false;
#     while (new_low < new_high){
#         gross_amount = (new_low + ((new_high - new_low) / 2));
#         // cout<<fixed << new_low << " : " << new_high << " : " <<  gross_amount <<endl;
        
#         value = check(gross_amount,net_amount, tax_rate, slab_amount, base_tax);
#         // cout<<fixed << "Value : " <<  value <<endl;
        
#         if (value == 1){
#             calculated_gross_amount = gross_amount;
#             flag = true;
#             break;
#         } 
#         else if (value == 2){
#             new_low = gross_amount + 0.01;
#         }
#         else if ( value == 3){
#             new_high =  gross_amount - 0.01;
#         }
#     }
#     if (flag==true){
#       new_high = calculated_gross_amount;
#     }
    # double total_tax, tax_rebate, final_tax;
    # total_tax = (((new_high-slab_amount) * tax_rate)/100) + base_tax;
    # cout<<fixed << total_tax << endl;
    # return 0;
    
# }

def solve():
    net = 5_000_000
    R = 30
    SA = 1_000_000
    BT = 125000
    
    def check(GA):
        TT = (((GA-SA) * R) / 100 )+ BT
        TR = (TT*TT) / GA
        FT = TT - TR
        if net + FT == GA:
            return 0
        elif net + FT > GA:
            return 1
        else:
            return -1
    answer = None
    start = net + BT
    last = 10**9
    print(start, last)
    while start <= last:
        GA = (start + (last - start) // 2)
        print("Estimated : ", GA)
        value = check(GA)
        if value == 0:
            answer = GA
            break
        elif value == 1:
            start = GA + 1
        else:
            last =  GA - 1
    
    print(start, last)
solve()
