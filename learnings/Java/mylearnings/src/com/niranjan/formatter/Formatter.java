package com.niranjan.formatter;

import java.text.NumberFormat;
import java.util.Locale;

/**
 * Created by Niran0303 on 12/29/2016.
 */
public class Formatter {
    public static void main(String args[]){
        NumberFormat numbF= NumberFormat.getNumberInstance();
        float num=1_232_231.123f;
        System.out.println(numbF.format(num));
        NumberFormat currF=NumberFormat.getCurrencyInstance();
        System.out.println(currF.format(num));
        NumberFormat intF=NumberFormat.getIntegerInstance();
        System.out.println(intF.format(num));
        Locale locale=new Locale("eng","IN");
        NumberFormat numbFI= NumberFormat.getNumberInstance(locale);
        System.out.println(numbFI.format(num));
        NumberFormat currFI=NumberFormat.getCurrencyInstance(locale);
        System.out.println(currFI.format(num));
        NumberFormat intFI=NumberFormat.getIntegerInstance(locale);
        System.out.println(intFI.format(num));
    }
}
