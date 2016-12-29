package com.niranjan.exceptions.multipleexceptions;


/**
 * Created by Niran0303 on 12/28/2016.
 */
public class MultiException {
    public static void main(String args[]){
        int ar[]=new int[10];
        try{
            int a=args.length;
            int i=1/a;
            System.out.println(ar[a]);
        }
        catch(ArithmeticException e){
            System.out.println(e);
        }
        catch(ArrayIndexOutOfBoundsException e){
            System.out.println(e);
        }
    }
}
