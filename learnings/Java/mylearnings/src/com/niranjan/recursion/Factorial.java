package com.niranjan.recursion;

/**
 * Created by Niran0303 on 12/26/2016.
 */
public class Factorial {
    int factorial(int n){
        if (n==1) return 1;
        return n*factorial(n-1);
    }
}
