#include <fstream>
#include <iostream>
#include <string>
#include <bits/stdc++.h>

int main()
{
    std::ifstream file{"input.txt"};

    if(!file)
    {
        std::cerr << "No file found\n";

        return 0;
    }


    //std::stringstream ssInp(file);
    std::string tempStr;
    //std::cout << strInp << '\n';
    long total = 0;


    while(getline(file, tempStr, ','))
    {
        std::stringstream ss(tempStr);
        std::string t;

        int i = 0;
        long range[2];
        //int digits[2];

        while(getline(ss, t, '-'))
        {
            range[i] = std::stoll(t);
            //std::cout << t << '\n';
            i = 1;
        }

        //std::cout << std::setfill('0') << std::setw(digits[0]) << range[0] << ' ' << std::setw(digits[1]) << range[1] << '\n';
        
        for(long j{range[0]}; j <= range[1]; j++)
        {
            bool valid = true;
            std::string numberBuffer;
            
            numberBuffer = std::to_string(j);
            /*if(numberBuffer.size() % 2 != 0)
            {
                numberBuffer = '0' + numberBuffer;
            }*/

            int size = numberBuffer.size();

            std::string halves[2];
            halves[0] = numberBuffer.substr(0, (size)/2);
            halves[1] = numberBuffer.substr((size/2), size-1);

            //std::cout << halves[0] << ' ' << halves[1] << '\n';

            if(halves[0] == halves[1])
                valid = false;

            if(size == 1)
            {
                valid = true;
            }

            if(!valid)
                //std::cout << numberBuffer << '\n';
                total += std::stoll(numberBuffer);
        }
    }

    std::cout << total << '\n';

    return 0;
}
