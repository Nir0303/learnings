package com.niranjan.calculator;
import com.niranjan.calculator.util.*;
/**
 * Created by Niran0303 on 12/29/2016.
 */
public class SimpleCalculator {
    public static void main(String args[]){

        String s1 =InputString.getInput("Please enter first integer: ");

        String s2 =InputString.getInput("Please enter second integer: ");

        MathClass.addNumbers(s1,s2);

    }
}
