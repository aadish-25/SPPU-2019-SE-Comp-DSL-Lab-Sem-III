#include <iostream>
#include <cctype>
using namespace std;


class Stack{
    public : 
        int arr[100];
        int top;

        Stack(){
            top = -1;
        }

        void push(int x){
            top++;
            arr[top] = x;
        }

        char pop(){
            char chr = arr[top];
            top--;
            return chr;
        }

        bool isEmpty(){
            if(top == -1)
                return true;
            else 
                return -1;
        }  
};

int main(){
    Stack obj;

    string str;
    cout << "Enter expression to be checked : ";
    cin >> str;

    for(int i=0; i<str.length(); i++){
        char ch = str[i];
        if (ch == '(' || ch == '[' || ch == '{')
            obj.push(ch);
        else{
            char popped = obj.pop();
            if ((ch == ')' && popped != '(') ||
                (ch == ']' && popped != '[') ||
                (ch == '}' && popped != '{')){
                    cout << "NOT PARANTHESISED EXPRESSION";
                    return 0;
                }
        }
    }

    if(obj.top == -1)
        cout << "PARANTHESISED";
    else    
        cout << "NOT PARANTHESISED EXPRESSION";
    
    return 0;

}