package com.hackerrank.java.basic;

import java.text.DateFormat;
import java.time.format.DateTimeFormatter;
import java.util.Calendar;

/**
 * Created by Niran0303 on 12/30/2016.
 */
public class DayOfYear {
    public static void main(String args[]){
        Calendar cal =  Calendar.getInstance();
        cal.set(2016,12,30);
        DateTimeFormatter dft = new DateTimeFormatter();
        System.out.println(cal.DAY_OF_WEEK);


    }
}
