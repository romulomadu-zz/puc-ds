# Trabalho Prático 2 - HD
# Autor: Rômulo Madureira Rodrigues

# Questão 1

df = sqlContext.read.option("header","True").format("csv").load("/FileStore/tables/j1dnoxbo1499910557677/")

# Questão 2

df.printSchema()

# Questão 3

df.count()

# Questão 4

df = df.select("User_ID","Product_ID","Gender","Age","Occupation","City_Category","Stay_In_Current_City_Years","Marital_Status","Product_Category_1","Product_Category_2","Product_Category_3",df.Purchase.cast('int'))
df.describe('Purchase').show()

# Questão 5

df.select("Product_ID").distinct().count()

# Questão 6

df.crosstab('Age','Gender').show()

# Questão 7

pur_gt20k =  df.filter(df.Purchase>15000)
pur_gt20k.count()

# Questão 8

pur_bt20k45k_f = df.filter((df.Purchase>20000) & (df.Purchase<45000) & (df.Gender=="F"))
pur_bt20k45k_f.count()

# Questão 9

#df.groupby("Age").mean().orderBy("Age").show()
from pyspark.sql.functions import mean
pur_avgbyage = df.groupby("Age").agg(mean("Purchase").alias("AVG(PurchaseI)"))
pur_avgbyage.show()

# Questão 10

df.groupby("Gender").agg(mean("Purchase").alias("AVG(PurchaseI)")).show()

# Questão 11

pur_avgbyage.withColumn("Pur_10_percent", pur_avgbyage['AVG(PurchaseI)'] *1.1 ).select('Age', 'AVG(PurchaseI)',"Pur_10_percent").show()
