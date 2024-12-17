#include <iostream>
#include <cmath>
using namespace std;


class Stack{

    public:
        int arr[100];
        int top;

        Stack(){
            top=-1;
        }

        void push(int x){
            top++;
            arr[top] = x;
        }

        int pop(){
            if(isEmpty() == true)
                return -1;
            int chr = arr[top];
            top--;
            return chr;
        }

        int peek(){
            return arr[top];
        }

        bool isEmpty(){
            if(top == -1)
                return true;
            else return false;
        }

};

int main(){
    Stack stack;
    string postfix;

    cout << "Enter postfix expression to be evaluated : ";
    cin >> postfix;

    for(int i=0; i<postfix.length(); i++){
        char ch = postfix[i];
        if(isdigit(ch) == true)
            stack.push(ch - '0'); //stores the numeric value instead of char i.e 5 instead of '5'
        else{
            int value1 = stack.pop();
            int value2 = stack.pop();

            if(value1 == -1 || value2 == -1){
                cout << "Invalid expression!!!";
                return 0;
            }

            if(ch=='+')
                stack.push(value2+value1);
            if(ch=='-')
                stack.push(value2-value1);
            if(ch=='*')
                stack.push(value2*value1);
            if(ch=='/')
                stack.push(value2/value1);        
            if(ch=='^')
                stack.push(pow(value2, value1));     
                // value2 ^ value1 INVALID as it XORs them
        }        
    }

    if(stack.top == 0){
        cout << "Valid expression!!!" <<endl;
    }
    else{
        cout << "Invalid expression!!!";
        return 0;
    }

    int ans = stack.peek();
    cout << "The value of the postfix expression is : " << ans;

    return 0;

}