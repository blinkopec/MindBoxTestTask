from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()


categories = spark.createDataFrame([
    (1, 'name_category_1'),
    (2, 'name_category_2'),
    (3, 'name_category_3'),
    (4, 'name_category_4'),],
    ['id', 'category_name'],
)

products = spark.createDataFrame([
    (1, 'name_product_1'),
    (2, 'name_product_2'),
    (3, 'name_product_3'),
    (4, 'name_product_4'),
    (5, 'name_product_5'),
    (6, 'name_product_6'),
    (7, 'name_product_7'),
    (8, 'name_product_8'),
    (9, 'name_product_9'),],
    ['id', 'product_name']
)


categories_products = spark.createDataFrame([
    (1, 1),
    (1, 1),
    (2, 2),
    (2, 3),
    (3, 3),
    (3, 4),
    (4, 5),],
    ['category_id', 'product_id']
)


df_data = (products
    .join(categories_products,products.id == categories_products.product_id, how='left')
    .join(categories, categories_products.category_id == categories.id, how='left')
    .select(['category_name', 'product_name'])
)

df_data.orderBy('category_id', 'product_id', ).show(truncate=True)