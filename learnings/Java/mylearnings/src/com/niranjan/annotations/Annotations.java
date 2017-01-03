package com.niranjan.annotations;
import java.lang.annotation.*;
import java.lang.reflect.*;
/**
 * Created by Niran0303 on 12/31/2016.
 */
@Retention(RetentionPolicy.RUNTIME)
@interface MyAnno{
    String str() default "test";
    int val() default 500;
}
@Retention(RetentionPolicy.RUNTIME)
@interface Mymarker{}

@Retention(RetentionPolicy.RUNTIME)
@interface SingleAnno{ int  val();}

public class Annotations {
    @MyAnno(val=1000,str="Testing annontation")

    public static void meth() throws NoSuchMethodException{
        Annotations a= new Annotations();
        Class<?> c = a.getClass();
        Method m = c.getMethod("meth");
        Annotation ann[] = m.getAnnotations();
        for(Annotation i: ann ){
            System.out.println(i);
        }
        MyAnno anno = m.getAnnotation(MyAnno.class);

        System.out.println(anno.str()+" "+anno.val());
    }

    public static void main(String args[]){
        try {
            meth();
        } catch (NoSuchMethodException e) {
            e.printStackTrace();
        }
    }


}
