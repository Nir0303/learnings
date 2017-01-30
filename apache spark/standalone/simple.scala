import org.apache.spark.SparkContext

import org.apache.spark.{SparkContext,SparkConf}
import org.apache.spark.SparkContext._

object test {
def main(ars:Array[String]): Unit ={
  val conf = new SparkConf().setAppName("SparkMe Application").setMaster("local[*]")
  val sc = new SparkContext(conf);
  println("hello world")
  
}
}
