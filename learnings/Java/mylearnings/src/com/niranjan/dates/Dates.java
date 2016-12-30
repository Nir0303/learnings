package com.niranjan.dates;

import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.text.DateFormat;
import java.util.GregorianCalendar;
import java.util.Locale;
import java.time.LocalDateTime;
import java.time.LocalDate;
/**
 * Created by Niran0303 on 12/29/2016.
 */
public class Dates {
    public static void main(String args[]){
        //old format for java dates
        Locale locale=new Locale("eng","IN");
        Date dt=new Date();
        System.out.println(dt);

        GregorianCalendar gc = new GregorianCalendar(1947,07,15);
        Date iday = gc.getTime();
        System.out.println(iday);

        DateFormat dateFormat = DateFormat.getDateInstance(DateFormat.FULL);

        System.out.println(dateFormat.format(iday));
        //new Format
        LocalDateTime ldt= LocalDateTime.now();
        System.out.println(ldt);
        LocalDate ld = LocalDate.of(1947,8,15);
        System.out.println(ld);
        DateTimeFormatter df = DateTimeFormatter.ofPattern("MMM-dd-yyyy");
        System.out.println(df.format(ld));
    }
}
