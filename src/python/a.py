from neo4j import GraphDatabase
import pymysql

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "12345678"))
cnx = pymysql.connect(user='root', password='myroot', host='127.0.0.1', database='downloadsites')

cursor = cnx.cursor()
cursor1 = cnx.cursor()
cursor2 = cnx.cursor()

# 执行查询操作获取数据
query = ("SELECT person_name FROM person")
cursor.execute(query)
for row in cursor:
    name = row[0]


    with driver.session() as session:
        result = session.run("OPTIONAL MATCH (p:Person {name: $name}) RETURN p IS NOT NULL AS exists",name=name)
        yes = result.value()[0]
        if(not yes):
            query = "select company_name from company where person = %s"
            data = (name)
            cursor1.execute(query,data)
            for row1 in cursor1:
                cname = row1[0]
                print(cname)
                session.run("MATCH (n:Company {name: $cname}) CREATE (m:Person {name: $name})-[:HAS_COMPANY]->(n)",cname=cname,name=name)