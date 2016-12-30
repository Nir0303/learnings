package com.niranjan.oliveprocessing;
import com.niranjan.oliveprocessing.model.*;
import java.util.ArrayList;
import java.util.List;
/**
 * Created by Niran0303 on 12/30/2016.
 */
public class Main {
    public static void main(String args[]){
        /*
        *@args
         */
        List<Olive> olives=new ArrayList<>();

        olives.add(new Kalamata());
        olives.add(new Rose());
        olives.add(new Berry());
        olives.add(new Kalamata());
        olives.add(new Rose());
        olives.add(new Berry());
        olives.add(new Kalamata());
        olives.add(new Rose());
        olives.add(new Berry());

        Press press = new OliveProcessing();
        press.setOil(5.0);
        double totalOil= press.getOil(olives);
        System.out.println("Total oil crushed is "+totalOil);


        List<Olive> olives2=new ArrayList<>();

        olives2.add(new Kalamata());
        olives2.add(new Rose());
        olives2.add(new Berry());
        olives2.add(new Kalamata());
        olives2.add(new Rose());
        olives2.add(new Berry());
        olives2.add(new Kalamata());
        olives2.add(new Rose());
        olives2.add(new Berry());
        olives2.add(new Berry());
        olives2.add(new Kalamata());
        olives2.add(new Berry());
        olives2.add(new Kalamata());


        Press press2 = new OliveProcessing();
        double totalOil2= press2.getOil(olives2);
        System.out.println("Total oil crushed is "+totalOil2);

    }
}
