package com.niranjan.oliveprocessing.model;

/**
 * Created by Niran0303 on 12/30/2016.
 */
public abstract class Olive {

    /* constant declaration
    public static final String KALAMATA="kalamata";
    public static final String ROSE="rose";
    public static final String BERRY="berry";
    */

    private OliveNames name=OliveNames.KALAMATA;
    private OliveColors color=OliveColors.BLUE;
    private double qty=2.0;
    public Olive(){};
    public Olive(OliveNames name,OliveColors color,double qty){
        this.name=name;
        this.color=color;
        this.qty=qty;
    }
    public OliveNames getName() {
        return name;
    }

    public void setName(OliveNames name) {
        this.name = name;
    }

    public OliveColors getColor() {
        return color;
    }

    public void setColor(OliveColors color) {
        this.color = color;
    }

    public double crush() {
        return qty;
    }

    public void setQty(double qty) {
        this.qty = qty;
    }
    public abstract String getOrigin();

}
