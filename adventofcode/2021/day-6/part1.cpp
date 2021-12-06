#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdint>

using namespace std;


void SplitString(string s, vector<uint_fast8_t> &v){
	
	string temp = "";
	for(int i=0;i<s.length();++i){
		
		if(s[i]==','){
			v.push_back(std::stoi(temp));
			temp = "";
		}
		else{
			temp.push_back(s[i]);
		}
		
	}
	/* v.push_back(temp); */
	v.push_back(std::stoi(temp));
}


void PrintVector(vector<uint_fast8_t> v)
{
	for(int i=0;i<v.size();++i)
		cout<<v[i];
	cout<<"\n";
}

int main(int argc, char *argv[]) 
{
    std::ifstream fdata("input.txt");
    /* std::ifstream fdata("input1.txt"); */
    vector<uint_fast8_t> lanfish_timers;

    std::string fishdata;
    std::getline(fdata, fishdata);

    SplitString(fishdata, lanfish_timers);
    PrintVector(lanfish_timers);

    int days_of_simulation = 256;  // part1: 80, part2: 256 (exponential growth!)
    for(int i = 0; i < days_of_simulation; i++)
    {
        cout << "calculation day: " << i+1 << endl;
        int current_len = lanfish_timers.size();
        for(int fish_i = 0; fish_i < current_len; fish_i++)
        {
            bool newf = false;
            if(lanfish_timers[fish_i] == 0)
            {
                lanfish_timers[fish_i] = 6;
                lanfish_timers.push_back(8);
                newf = true;
            }

            if(newf == false)
            {
                lanfish_timers[fish_i] -= 1;
            }
        }
        
        cout << "After " << i+1 << " days: " << lanfish_timers.size() << endl;
    }
    fdata.close(); 
}
