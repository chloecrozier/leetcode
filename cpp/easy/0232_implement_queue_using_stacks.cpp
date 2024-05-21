// https://leetcode.com/problems/implement-queue-using-stacks/description/
class MyQueue {
public:
    stack<int> in;
    stack<int> out;

    MyQueue() {
        in = stack<int>();
        out = stack<int>();
    }
    
    void push(int x) {
        while(!out.empty()){
            in.push(out.top());
            out.pop();
        }
        in.push(x);
    }
    
    int pop() {
        while(!in.empty()){
            out.push(in.top());
            in.pop();
        }
        int temp = out.top();
        out.pop();
        return temp;
    }
    
    int peek() {
        while(!in.empty()){
            out.push(in.top());
            in.pop();
        }
        return out.top();
    }
    
    bool empty() {
        return in.empty() && out.empty();
    }
};
