package com.niranjan.questionprog;

/**
 * Created by Niran0303 on 12/28/2016.
 */
public class quiz  implements SharedConstants{
    static void answer(int x) {
        switch (x) {
            case YES:
                System.out.println("Yes");
                break;
            case NO:
                System.out.println("NO");
                break;
            case MAYBE:
                System.out.println("MAYBE");
                break;
            case SOON:
                System.out.println("Soon");
                break;
            case LATER:
                System.out.println("LATER");
                break;
            default:
                System.out.println("Never");
        }
    }
    public static void main(String args[]){
        Question q=new Question();

        answer(q.ask());
        answer(q.ask());
        answer(q.ask());
        answer(q.ask());
        answer(q.ask());
        //int i=1/0;
    }
}
