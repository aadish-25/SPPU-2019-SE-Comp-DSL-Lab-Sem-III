#include <iostream>
#include <string>
using namespace std;

void push(char &value, int &top, char arr[], char stack[]){
        top++;
        stack[top] = value;
    }

char pop(char stack[], int &top){
    char ch = stack[top];
    top--;
    return ch;
}

int main(){
    string s;
    int top = -1;
    bool find = true;
    char arr[100];
    char stack[100];

    cout << "Enter the expression ending with # " << endl;
    cin >> s;

    // writing the string into an empty array
    for(int i=0; s.length(); i++){
        if(s[i] == '#'){
            arr[i] = '\0';
            break;
        }
        arr[i] = s[i];
    }

    // display the string
    cout << "The entered string is : " << endl;
    for(int i=0; arr[i]!='\0'; i++){
        cout << arr[i];
    }
    cout << "\n";

    for(int i=0; arr[i]!='\0'; i++){
        char ch = arr[i];

        if(ch=='(' || ch=='{' || ch=='['){
            push(ch, top, arr, stack);
        }
        if(ch==')' || ch=='}' || ch==']'){
            char popped = pop(stack, top);
            if((ch==')' && popped!='(') || (ch==']' && popped!='[') || (ch=='}' && popped!='{')){
                    push(ch, top, arr, stack);
                    // push to the stack so that the stack isnt empty
                    break;
            }
        }
    }
    
    if(top==-1)
        cout << "Paranthesised equation";
    else
        cout << "Not a paranthesised equation";
    return 0;
}