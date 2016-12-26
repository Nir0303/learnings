package com.niranjan.stack;

/**
 * Created by Niran0303 on 12/26/2016.
 */
public class StackDemo {
    public static void main(String args[]){
        Stack s1= new Stack();
        for(int i=10;i<20;i++)  s1.push(i);
        for(int i=0;i<10;i++) System.out.println("Pop element "+s1.pop());
    }
}
