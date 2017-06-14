val pages = sqlContext.read.format("com.databricks.spark.xml").option("rowTag", "page").load("/datasets/enwikivoyage-20170101-pages-articles.xml.bz2")

pages.map (row => ( row.getAs[String]("title"), row.getAs[String]("revision.text._VALUE") ) )
val revisions = pages.select("title", "revision")

val dublinPage = pages.where(col("title") === "Dublin")

val dublinRevision = dublinPage.select("revision.*") 

val dublinRevText = dublinRevision.select("text._VALUE")

dublinRevText.show

