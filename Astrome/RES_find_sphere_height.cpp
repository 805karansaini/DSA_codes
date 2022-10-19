#include <iostream>
using namespace std;





double double_pre(double value){
    stringstream ss;
    ss << fixed << setprecision(7) <<  value;
    double res = ss.str();
    cout << res << endl;
}
    




// check if this height (after applying volume formula ) is bigger or smaller than the required.
// i,e if calculated_volume > volume ( given in question ), we must reduce it.. hence return -1. else 1
int check(double height,double radius, double volume){
    // volume of sphere dome can be given by
    // Volume = ((pi * h*h) / 3) * (3R - H)
    // Volume == 1/3 pi h^2 ( 3*Radius  - height)
    double long calculated_volume;
    const long double pi = 3.14159265L;
    const long double three = 3L;
    
    calculated_volume = ((pi * height * height) / three) * ((three * radius) - height);
    if (calculated_volume - volume <= 0.0000000L){
        // cout << "returned 1  " << height <<  endl;
        return 1;
        }
    else{
        // cout << "Returned -1  " << height <<  endl;
        return -1;
        }
    }

int main(){
    std::cout.precision(7);
    double Radius, Volume;
    double temp_height, final_height;
    cin >> Radius;
    cin >> Volume;
    
    int low, high, value;
    low = 0;
    high = int((Radius + 2 ) * 2);
		// binary serach for Closest Integers 
    while (low <= high){
        temp_height = (int)(low + ((high - low) / 2));
        value = check(temp_height, Radius, Volume);
        if (value == -1){
            high = temp_height - 1;
        } 
        else if (value == 1){
            low = temp_height + 1;
        }
    }
  
  	// binary serach for Closest values  ( actual answer but below is one more check)
    // cout << low << " " << high << endl;
    double new_low = min(low,high);
    double new_high = max(low,high);
    while (new_high >= new_low ){
        // cout <<fixed <<  new_low << " " << new_high << endl;
        temp_height = (new_low + ((new_high - new_low) / 2));
        value = check(temp_height, Radius, Volume);
        if (value == -1){
            new_high = temp_height - 0.0000001;
            // cout << "Decresing " << endl;
        } 
        else if (value == 1){
            // cout << "Increasing " << endl;
            new_low = temp_height + 0.0000001;
        }
    }
    
  	// final check for closest vaue bigger than volume in the question.
    long double low_range, high_range;
    low_range = min(new_low, new_high) - 0.0000050;
    high_range = max(new_low, new_high) + 0.0000050;
    // cout << "Low High range : " << low_range << "  " << high_range << endl;
    for(long double i = low_range; i <= high_range; i = i+0.0000001){
        if ( check(i, Radius, Volume) == -1 ){
            cout<<fixed <<  i << endl;
            return 0;
        }
    }
    
}