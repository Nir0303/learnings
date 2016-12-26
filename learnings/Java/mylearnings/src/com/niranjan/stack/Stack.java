package com.niranjan.stack;

/**
 * Created by Niran0303 on 12/26/2016.
 */
public class Stack {
    int tos;
    int stack[];
    Stack(){
        tos=-1;
        stack=new int[10];
    }
    void push(int l){
        if (tos>9){
            System.out.println("Stack overflow");
        }
        else{
            stack[++tos]=l;
        }
    }
    int pop(){
        if (tos<0){
            System.out.println("Stack underflow");
            return -1;

        }
        else{
            return stack[tos--];
        }
    }
}
