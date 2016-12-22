import org.apache.spark._

def isHeader(line: String) = line.contains("id_1")

case class matchdata(id1:Int,id2:Int,id3:Double,Match:Boolean)

def lineparser(lines:String) = {
val line=lines.split(',')
val a = line(0).toInt
val b = line(1).toInt
val c = line(2).toDouble
val d = line(11).toBoolean
matchdata(a,b,c,d)
}

val text=sc.textFile("C:\\Users\\Niran0303\\Dropbox\\working\\spark\\data\\data")

val line = text.filter{x=> !isHeader(x)}

val l = line.map{line => lineparser(line)}

val matcheddata = l.filter(_.Match)

val groupcounts=l.groupBy{_.Match}.mapValues{x=>x.size}

val linesplit = line.flatMap{l=>l.split(',')}

val linecnt = line.map{l=>1}.reduce{_+_}

val twordcnt = line.map{l=>l.split(',')}.map{w=> 1}.reduce{_+_}

val iwordcnt = line.flatMap{l=>l.split(',')}.map{word => (word,1)}.reduceByKey{_+_}.sortBy{-_._2}

iwordcnt.take(5).foreach(println)

val rdd = sc.parallelize(Array(1,2,3,3,4,34,343),5)

val rdd2 = rdd.map{x=> x*x}


	
