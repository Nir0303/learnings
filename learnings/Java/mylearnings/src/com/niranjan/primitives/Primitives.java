package com.niranjan.primitives;

import java.text.NumberFormat;

/**
 * Created by Niran0303 on 12/29/2016.
 */
public class Primitives {
    public static void main(String args[]){
        long v=10_000_000;
        System.out.println(v);
        NumberFormat formatter= NumberFormat.getNumberInstance();
        String formattedNumber= formatter.format(v);
        System.out.println(formattedNumber);

        String bool = "true";
        boolean boolparse= Boolean.parseBoolean(bool);
        System.out.println(boolparse);

        int value=2;
        String svalue = Integer.toString(value);
        String svalueappend = svalue +"nd";
        System.out.println(svalueappend);

    }
}
