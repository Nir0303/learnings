/**
  * Created by Niran0303 on 1/22/2017.
  */
object test {
def main(ars:Array[String]): Unit ={
  val a = (1 to 100).toList
  val b = a.map{ x=>(x,x*x)}
  b.foreach(println)

}
}
