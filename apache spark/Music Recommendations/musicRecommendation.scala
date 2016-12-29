val userRawdata = sc.textFile("user_artist_data.txt",5)

val userStats= userRawdata.map{_.split(' ')(0).toDouble}.stats()

val userMax=userStats.max

val userMin=userStats.min

val artistStats = userRawdata.map{_.split(' ')(1).toDouble}.stats()

val artistMax= artistStats.max

val artistMin= artistStats.min 


val artistData= sc.textFile("artist_data.txt")




val artistDataPars= artistData.flatMap{line =>
val (id,artistName)=line.span(_!='\t')
if (artistName.isEmpty){
None
} 
else {
try {
Some((id.toInt,artistName.trim)) 
} 
catch { 
case e: NumberFormatException => None 
} 
}
}


val artistDatap = artistData.map{line =>
val (id,name) = line.span(_ != '\t')
if (name.isEmpty) {
None
}
else{
(id.toInt,name.trim)
}
}


val rawartistalias = sc.textFile("artist_alias.txt")


val artistAlias = rawartistalias.flatMap{ line =>
val tokens = line.split('\t')
if (tokens(1).isEmpty) {
None
}
else{
Some((tokens(0).toInt,tokens(1).trim))
}
}.collectAsMap()


val artistAliasb = sc.broadcast(artistAlias)


val trainData = userRawdata.map{ line =>
val Array(userid,artistid,count)=line.split(' ').map(_.toInt)
val finalArtistId = artistAliasb.value.getOrElse(id,id)
Array(userid,finalArtistId,count)
}