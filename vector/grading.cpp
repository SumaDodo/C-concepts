#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the gradingStudents function below.
 */
vector<int> gradingStudents(vector<int> grades) {
    /*
     * Write your code here.
     */
    vector<int> final_marks(grades.size());
    int difference = 0;
    int intermediate = 0;
    int c =0;
    for(int i=0; i<grades.size();i++)
    {
        if(grades[i]<38)
            final_marks[i]=grades[i];
        else if(grades[i]>=38)
        {
            intermediate = grades[i]%5;
            difference = 5 - intermediate;
            if(difference < 3){
                c =grades[i]+difference;
                if(c>38)
                    final_marks[i] = c;
                else
                    final_marks[i] = grades[i];
            }
            else
                final_marks[i]=grades[i];
        }
    }
    return final_marks;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<int> grades(n);

    for (int grades_itr = 0; grades_itr < n; grades_itr++) {
        int grades_item;
        cin >> grades_item;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        grades[grades_itr] = grades_item;
    }

    vector<int> result = gradingStudents(grades);

    for (int result_itr = 0; result_itr < result.size(); result_itr++) {
        fout << result[result_itr];

        if (result_itr != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}
