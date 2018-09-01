#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the timeConversion function below.
 */
string timeConversion(string s) {
    /*
     * Write your code here.
     */
    string s1 = "A";
    string s2 = "P";
    int point;
    int point2, hours;
    point = s.rfind(s1);
    point2 = s.rfind(s2);
    string hour,mins,secs,time;
    hour = s.substr(0,2);
    mins = s.substr(3,5);
    secs = s.substr(6,8);
    if(point2!=std::string::npos)
    {
       if(hour == "12")
        {
            hour = hour;
        }
        else
        {
            hours = stoi(hour);
            hours = hours+12;
            hour = to_string(hours);
        }
    }
    else if(point!=std::string::npos)
    {
        if(hour == "12")
        {
            hour = "00";
        }
    }
    time = hour+":"+mins;
    return (time);
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
