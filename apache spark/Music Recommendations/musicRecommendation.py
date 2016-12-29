from pyspark import SparkContext

sc = SparkContext()

userRawdata = sc.textFile("/oasis/projects/nsf/sun116/addankn/profiledata_06-May-2005/user_artist_data.txt",5)

for i in userRawdata.take(5): print i

userStats = userRawdata.map(lambda _:_.split(' ')).map(lambda x:float(x[0])).stats()

useridMax,useridMin=userStats.max(),userStats.min()

print "Userid mx and min are {0} {1}".format(useridMax,useridMin)

artistStats = userRawdata.map(lambda _:_.split(' ')).map(lambda x:float(x[1])).stats()

artistidMax,artistidMin=artistStats.max(),artistStats.min()

print "Artist id max and min are {0} {1}".format(artistidMax,artistidMin)


artistRawData=sc.textFile("/oasis/projects/nsf/sun116/addankn/profiledata_06-May-2005/artist_data.txt",5)

def artistp(x):
	token={}
	tokens=x.split('\t')
	if len(tokens)<2:
		return None
	else:
		token['id']=int(tokens[0])
		token['artistName']=tokens[1].strip()
		return token

artistData=artistRawData.map(lambda x: artistp(x))

def artist(x):
	token=[0,0]
	tokens=x.split('\t')
	if len(tokens)==2:
		try:
			token[0]=int(tokens[0])
		except ValueError:
			token[0]=00000
		token[1]=tokens[1].strip()
		return token

artistDatat=artistRawData.map(lambda x: artist(x))

		
artistRawAliasData=sc.textFile("/oasis/projects/nsf/sun116/addankn/profiledata_06-May-2005/artist_alias.txt",5)


def artistap(x):
	token={}
	tokens=x.split('\t')
	if len(tokens)<2:
		return None
	else:
		token['id']=int(tokens[0])
		token['aliasid']=tokens[1].strip()
		return token
		

artistAliasData=artistRawAliasData.map(lambda x : artistap(x))


#artistAliasDatab=sc.broadcast(artistAliasData.values.collectAsMap())


def userdatap(x):
	userData=[0,0,0]
	tokens=x.split(' ')
	userData[0]=int(tokens[0])
	userData[1]=int(tokens[1])
	userData[2]=int(tokens[2])
	return userData


userData= userRawdata.map(lambda x:userdatap(x)).cache()


from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating

model=ALS.trainImplicit(userData,10,10,0.1)


recommendations = model.recommendProducts(1000002,5)

x=[[i.products,0] for i in recommendations]
y=sc.parallelize(x)

for i in artistDatat.filter(lambda x:x is not None).join(y).take(5):
	print i[1][0]