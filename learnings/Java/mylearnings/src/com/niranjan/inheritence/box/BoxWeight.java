package com.niranjan.inheritence.box;

/**
 * Created by Niran0303 on 12/27/2016.
 */
public class BoxWeight extends Box {
    double weight;
    BoxWeight(double length, double width, double height, double weight){
        //this.length=length;
        //this.height=height;
        //this.width=width;
        super(length,width,height);
        this.weight=weight;
    }

    /**
     * aa
     */
    BoxWeight(){
        super();
        this.weight=-1;
    }
    BoxWeight(double len,double weight){
        super(len);
        this.weight=weight;
    }
    BoxWeight(BoxWeight b){
        super( b);
        this.weight=b.weight;
    }

}
