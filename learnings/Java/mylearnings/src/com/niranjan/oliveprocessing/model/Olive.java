package com.niranjan.oliveprocessing.model;

/**
 * Created by Niran0303 on 12/30/2016.
 */
public class Olive {

    public String name="kalamata";
    public String color="Blue";
    public double qty=2.0;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public double crush() {
        return qty;
    }

    public void setQty(double qty) {
        this.qty = qty;
    }


}
