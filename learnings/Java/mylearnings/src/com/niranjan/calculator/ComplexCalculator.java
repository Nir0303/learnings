package com.niranjan.calculator;
import com.niranjan.calculator.util.InputString;
import com.niranjan.calculator.util.MathClass;

public class ComplexCalculator {


    public static void main(String args[]){
        try {
            String s1 = InputString.getInput("Enter a Number ");
            String s2 = InputString.getInput("Enter a Number ");
            String op = InputString.getInput("Enter operation (*,+,-,/): ");
            switch (op) {
                case "*":
                    MathClass.multNumbers(s1, s2);
                    break;
                case "-":
                    MathClass.subtractNumbers(s1, s2);
                    break;
                case "+":
                    MathClass.addNumbers(s1, s2);
                    break;
                case "/":
                    MathClass.divideNumbers(s1, s2);
                    break;
                default:
                    System.out.println("Unrecognised Operation");

            }
        }
        catch(NumberFormatException e){
                System.out.println("Number format exception for "+e.getMessage());
            }

    }

}
