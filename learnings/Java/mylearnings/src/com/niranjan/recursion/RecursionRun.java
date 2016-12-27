package com.niranjan.recursion;

/**
 * Created by Niran0303 on 12/26/2016.
 */
public class RecursionRun {
    public static void main(String args[]){
        Factorial f=new Factorial();
        System.out.println("Factorial of 3 is "+f.factorial(3));
        System.out.println("Factorial of 4 is "+f.factorial(4));
        System.out.println("Factorial of 1 is "+f.factorial(1));
        Fibonnaci fibo = new Fibonnaci();
        System.out.println("Fibonnaci number of index 5 is "+fibo.fibovalue(5));
    }
}
