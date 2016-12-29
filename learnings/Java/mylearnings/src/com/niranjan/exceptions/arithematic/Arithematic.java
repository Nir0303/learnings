package com.niranjan.exceptions.arithematic;

/**
 * Created by Niran0303 on 12/28/2016.
 */
public class Arithematic {
    public static void main(String args[]){
        try{
            int i =1/0;
            System.out.println("This wont be printed");
        }
        catch(ArithmeticException E){
            System.out.println("Ignore once"+ E);
        }
    }
}
