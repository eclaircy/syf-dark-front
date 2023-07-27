import csv
import time

from bs4 import BeautifulSoup
import hashlib
#
# def generate_dom_sequence(node):
#     """将DOM节点表示为字符串序列"""
#     # 节点的标签名
#     tag = node.name
#     # 节点的属性，将属性名和属性值拼接成字符串
#     attributes = ''.join([f'{k}={v}' for k, v in sorted(node.attrs.items())])
#     # 节点的文本内容
#     text = node.text.strip()
#
#     # 将节点的标签名、属性和文本内容拼接成一个字符串序列
#     sequence = f'<{tag} {attributes}>{text}</{tag}>'
#     return sequence
#
# def generate_dom_tree_sequence(dom_tree):
#     """将DOM树表示为字符串序列"""
#     # 递归遍历DOM树，将每个节点表示为字符串序列，并将序列拼接起来
#     sequence = ''
#     for child in dom_tree.children:
#         if child.name is not None:
#             sequence += generate_dom_sequence(child)
#             sequence += generate_dom_tree_sequence(child)
#     return sequence
#
# def calculate_html_similarity(html1, html2):
#     """计算HTML文档之间的相似度"""
#     # 解析HTML文档，生成DOM树
#     soup1 = BeautifulSoup(html1, 'html.parser')
#     soup2 = BeautifulSoup(html2, 'html.parser')
#
#     # 将DOM树表示为字符串序列
#     sequence1 = generate_dom_tree_sequence(soup1)
#     sequence2 = generate_dom_tree_sequence(soup2)
#
#     # 计算字符串序列之间的相似度（这里使用Jaccard相似度）
#     set1 = set(sequence1.split())
#     set2 = set(sequence2.split())
#     similarity = len(set1 & set2) / len(set1 | set2)
#     return similarity
#
# # 示例使用
# with open('1599.html', 'r', encoding='utf-8') as f1, open('1597.html', 'r', encoding='utf-8') as f2:
#     html1 = f1.read()
#     html2 = f2.read()
#
# similarity = calculate_html_similarity(html1, html2)
# print(f'相似度：{similarity}')
#
# with open("test.csv", 'r', errors='ignore') as csvfile:
#     reader1 = csv.DictReader(csvfile,
#                              fieldnames=["id", "url", "资产标签", "IP", "IP标签", "端口", "网站标题", "域名", "应用/组件", "备案单位",
#                                          "备案号", "国家", "省份", "市区", "运营商", "注册机构", "download_domain_1",
#                                          "download_domain_2", "download_domain_3", "download_domain_4",
#                                          "download_domain_5", "soft_name_1", "soft_name_2", "soft_name_3",
#                                          "soft_name_4", "soft_name_5", "is_bad", "is_record", "is_download"])
#     next(reader1)
#
#     for row in reader1:
#         id = (row["id"])
#         print(id)
#
#         with open("test.csv", 'r', errors='ignore') as csvfile2:
#             reader2 = csv.DictReader(csvfile2,
#                                      fieldnames=["id", "url", "资产标签", "IP", "IP标签", "端口", "网站标题", "域名", "应用/组件", "备案单位",
#                                                  "备案号", "国家", "省份", "市区", "运营商", "注册机构", "download_domain_1",
#                                                  "download_domain_2", "download_domain_3", "download_domain_4",
#                                                  "download_domain_5", "soft_name_1", "soft_name_2", "soft_name_3",
#                                                  "soft_name_4", "soft_name_5", "is_bad", "is_record", "is_download"])
#             next(reader2)
#
#             for row2 in reader2:
#                 id1 = (row2["id"])
#                 print(id1)
#
#                 # 示例使用
#                 try:
#                     with open(str(id1)+'.html', 'r', encoding='utf-8') as f1, open(str(id) + '.html', 'r',
#                                                                               encoding='utf-8') as f2:
#                         html1 = f1.read()
#                         html2 = f2.read()
#
#                     similarity = calculate_html_similarity(html1, html2)
#                     if (similarity > 0.15):
#                         print(f'相似度：{similarity}---' + str(id1)+'<---->'+str(id))
#                 except:
#                     pass
#
#
#
#
#




# from bs4 import BeautifulSoup
# import numpy as np
#
# # 计算两个节点的相似度
# def node_similarity(n1, n2):
#     if n1.tag != n2.tag:
#         return 0
#     sim = 0
#     if n1.text and n2.text:
#         sim += min(len(n1.text), len(n2.text)) / max(len(n1.text), len(n2.text))
#     if n1.attrib and n2.attrib:
#         sim += len(set(n1.attrib.items()) & set(n2.attrib.items())) / \
#                len(set(n1.attrib.items()) | set(n2.attrib.items()))
#     return sim
#
# # 计算两个子树的编辑距离
# def subtree_edit_distance(t1, t2):
#     m, n = len(t1), len(t2)
#     dp = np.zeros((m + 1, n + 1))
#     for i in range(m + 1):
#         dp[i][0] = i
#     for j in range(n + 1):
#         dp[0][j] = j
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1 - node_similarity(t1[i - 1], t2[j - 1]))
#     return dp[m][n]
#
# # 计算两个网页的相似度
# def webpage_similarity(t1, t2):
#     return 1 - subtree_edit_distance(t1, t2) / (len(t1) + len(t2))
#
# # 读取HTML源码文件，转换成BeautifulSoup对象，并提取出其中的DOM树节点列表
# with open('29.html', 'r', encoding='utf-8') as f:
#     html1 = f.read()
# soup1 = BeautifulSoup(html1, 'html.parser')
# t1 = soup1.find_all()
#
# with open('30.html', 'r', encoding='utf-8') as f:
#     html2 = f.read()
# soup2 = BeautifulSoup(html2, 'html.parser')
# t2 = soup2.find_all()
#
# # 计算网页相似度
# print(webpage_similarity(t1, t2))


# from bs4 import BeautifulSoup
# import numpy as np
#
# # 计算两个节点的相似度
# def node_similarity(n1, n2):
#     if n1.tag != n2.tag:
#         return 0
#     sim = 0
#     if n1.text and n2.text:
#         sim += min(len(n1.text), len(n2.text)) / max(len(n1.text), len(n2.text))
#     if n1.attrib and n2.attrib:
#         sim += len(set(n1.attrib.items()) & set(n2.attrib.items())) / \
#                len(set(n1.attrib.items()) | set(n2.attrib.items()))
#     return sim
#
# # 计算两个子树的编辑距离
# def subtree_edit_distance(t1, t2):
#     m, n = len(t1), len(t2)
#     dp = np.zeros(n + 1)
#     for j in range(n + 1):
#         dp[j] = j
#     for i in range(1, m + 1):
#         # 初始值
#         dp[0] = i
#         # 记录上一行的值
#         pre = dp[0]
#         for j in range(1, n + 1):
#             # 保存当前位置的值，防止被覆盖
#             cur = dp[j]
#             # 转移
#             dp[j] = min(dp[j] + 1, dp[j - 1] + 1, pre + (1 - node_similarity(t1[i - 1], t2[j - 1])))
#             # 更新pre
#             pre = cur
#     return dp[n]
#
# # 计算两个网页的相似度
# def webpage_similarity(t1, t2):
#     return 1 - subtree_edit_distance(t1, t2) / (len(t1) + len(t2))
#
# # 读取HTML源码文件，转换成BeautifulSoup对象，并提取出其中的DOM树节点列表
# with open('29.html', 'r', encoding='utf-8') as f:
#     html1 = f.read()
# soup1 = BeautifulSoup(html1, 'html.parser')
# t1 = soup1.find_all()
#
# with open('30.html', 'r', encoding='utf-8') as f:
#     html2 = f.read()
# soup2 = BeautifulSoup(html2, 'html.parser')
# t2 = soup2.find_all()
#
# # 计算网页相似度
# print(webpage_similarity(t1, t2))

# from joblib import Parallel, delayed
# import numpy as np
# from bs4 import BeautifulSoup
#
# # 计算两个节点的相似度
# def node_similarity(n1, n2):
#     if n1.tag != n2.tag:
#         return 0
#     sim = 0
#     if n1.text and n2.text:
#         sim += min(len(n1.text), len(n2.text)) / max(len(n1.text), len(n2.text))
#     if n1.attrs and n2.attrs:
#         sim += len(set(n1.attrs.items()) & set(n2.attrs.items())) / len(set(n1.attrs.items()) | set(n2.attrs.items()))
#     return sim
#
# # 计算两个子树的编辑距离
# def subtree_edit_distance_row(t1, t2, i):
#     n = len(t2)
#     dp = np.zeros(n + 1)
#     dp[0] = i
#     pre = dp[0]
#     for j in range(1, n + 1):
#         cur = dp[j]
#         dp[j] = min(dp[j] + 1, dp[j - 1] + 1, pre + (1 - node_similarity(t1[i - 1], t2[j - 1])))
#         pre = cur
#     return dp
#
# def subtree_edit_distance(t1, t2):
#     m, n = len(t1), len(t2)
#     rows = Parallel(n_jobs=-1)(delayed(subtree_edit_distance_row)(t1, t2, i) for i in range(1, m + 1))
#     return rows[-1][-1] / (len(t1) + len(t2))
#
# # 计算两个网页的相似度
# def webpage_similarity(html1, html2):
#     soup1 = BeautifulSoup(html1, 'html.parser')
#     t1 = soup1.find_all()
#     soup2 = BeautifulSoup(html2, 'html.parser')
#     t2 = soup2.find_all()
#     return 1 - subtree_edit_distance(t1, t2)
#
# # 读取HTML源码文件
# with open('29.html', 'r', encoding='utf-8') as f:
#     html1 = f.read()
#
# with open('30.html', 'r', encoding='utf-8') as f:
#     html2 = f.read()
#
# # 计算网页相似度
# print(webpage_similarity(html1, html2))




# from html_similarity import style_similarity, similarity, structural_similarity
from neo4j import GraphDatabase

# driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "a109122392"))
# query = 'MATCH (a:website {name: "dxz.51xiazai.cn"})-[r:SIMILAR_TO1]-(b:website {name: "dxzbd.51xiazai.cn"}) return r'
#
# # 获取查询结果中的节点名称
# with driver.session() as session:
#     result = session.run(query)
#     if(len(result.data())==0):
#         print(123)




import csv
import time
from urllib.parse import urlparse

import requests
from html_similarity import style_similarity, similarity, structural_similarity
from neo4j import GraphDatabase
import pymysql
import os

def relationship_exists(tx, domain1, domain2):
    result = tx.run("MATCH (:website {name: $domain1})-[:SIMILAR_TO]-(:website {name: $domain2}) RETURN COUNT(*) AS count",
                    domain1=domain1, domain2=domain2)
    count = result.single()["count"]
    return count > 0





def sim(domain):
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "a109122392"))
    cnx = pymysql.connect(user='root', password='a109122392', host='127.0.0.1', database='pachong')

    cursor = cnx.cursor()
    cursor1 = cnx.cursor()

    # 执行查询操作获取数据
    query = ("SELECT url,home_page_html,`domain` FROM site_info where `domain` = %s")
    data=(domain)
    cursor.execute(query,data)
    for row in cursor:
        url = row[0]
        domain1 = row[2]

        parsed_url = urlparse(url)
        protocol = parsed_url.scheme + "://"
        hostname = parsed_url.netloc

        new_url = protocol + hostname
        print(new_url)
        try:
            res = requests.get(new_url, timeout=2)
            html = res.text

            if (html == ""):
                continue

            if("404 Not Found" in html or "403 Forbidden" in html or "500 Internal Server Error" in html or "blocked" in html or 503 == res.status_code or 404 == res.status_code):
                continue

            update_statement = "UPDATE site_info SET home_page_html = %s WHERE url = %s"
            html1 = html
            data = (html, url)

            # 执行更新语句
            cursor1.execute(update_statement, data)

            # 提交事务
            cnx.commit()
        except Exception as e:
            print(e)
            continue


        # 执行查询操作获取数据
        query = ("SELECT url,home_page_html,`domain` FROM site_info")

        cursor1.execute(query)

        for row in cursor1:
            html2 = row[1]
            domain2 = row[2]
            if (domain1 == domain2):
                continue
            if (html2 ==None):
                continue
            if ("403 Forbidden" in html2 or "404 Not Found" in html2 or "500 Internal Server Error" in html2 or "blocked" in html2):
                continue
            try:
                similarity1 = similarity(html1, html2)
            except:
                continue

            with driver.session() as session:
                exists = session.read_transaction(relationship_exists, domain1, domain2)
                if (exists != 0):
                    continue
                result = session.run("""//相似度3
        MATCH (d1:website), (d2:website)
        WHERE d1.name=$domain1 and d2.name=$domain2  // 避免重复计算  // 避免重复计算
        WITH d1, d2,
             CASE
               WHEN d1.Company <>"None" and d1.Company <>"" AND d2.Company <>"" AND d2.Company <>"None" THEN apoc.text.levenshteinSimilarity(d1.Company, d2.Company) * 0.20
               ELSE 0
             END AS CompanySimilarity,
             CASE
               WHEN d1.Country <>"None" AND d1.Country <>"" AND d2.Country <>"" AND d2.Country <>"None" THEN apoc.text.levenshteinSimilarity(d1.Country, d2.Country) * 0.05
               ELSE 0
             END AS CountrySimilarity,
             CASE
               WHEN d1.Ip <>"None" AND d1.Ip <>"" AND d2.Ip <>"" AND d2.Ip <>"None" THEN apoc.text.levenshteinSimilarity(d1.Ip, d2.Ip) * 0.10
               ELSE 0
             END AS IpSimilarity,
             CASE
               WHEN d1.Port <>"None" AND d1.Port <>"" AND d2.Port <>"" AND d2.Port <>"None" THEN apoc.text.levenshteinSimilarity(d1.Port, d2.Port) * 0.05
               ELSE 0
             END AS portSimilarity,
             CASE
               WHEN d1.Website_title <>"None" AND d1.Website_title <>"" AND d2.Website_title <>"" AND d2.Website_title <>"None" THEN apoc.text.levenshteinSimilarity(d1.Website_title, d2.Website_title) * 0.15
               ELSE 0
             END AS titleSimilarity,
             CASE
               WHEN d1.Operator <>"None" AND d1.Operator <>"" AND d2.Operator <>"" AND d2.Operator <>"None" THEN apoc.text.levenshteinSimilarity(d1.Operator, d2.Operator) * 0.05
               ELSE 0
             END AS OperatorSimilarity,
             CASE
               WHEN d1.Province <>"None" AND d1.Province <>"" AND d2.Province <>"" AND d2.Province <>"None" THEN apoc.text.levenshteinSimilarity(d1.Province, d2.Province) * 0.05
               ELSE 0
             END AS ProvinceSimilarity,
             CASE
               WHEN d1.Urbanarea <>"None" AND d1.Urbanarea <>"" AND d2.Urbanarea <>"" AND d2.Urbanarea <>"None" THEN apoc.text.levenshteinSimilarity(d1.Urbanarea, d2.Urbanarea) * 0.05
               ELSE 0
             END AS UrbanareaSimilarity,
             CASE
               WHEN d1.license <>"None" AND d1.license <>"" AND d2.license <>"" AND d2.license <>"None" THEN apoc.text.levenshteinSimilarity(d1.license, d2.license) * 0.10
               ELSE 0
             END AS licenseSimilarity,
             CASE
               WHEN d1.name <>"None" AND d1.name <>"" AND d2.name <>"" AND d2.name <>"None" THEN apoc.text.levenshteinSimilarity(d1.name, d2.name) * 0.20
               ELSE 0
             END AS domainSimilarity
        WITH d1, d2,
             (CompanySimilarity + CountrySimilarity + IpSimilarity + portSimilarity + titleSimilarity + OperatorSimilarity + ProvinceSimilarity + UrbanareaSimilarity + licenseSimilarity + domainSimilarity) / 1 AS similarity
        return similarity
        """, domain1=domain1, domain2=domain2)

                for record in result:
                    similarity2 = (record.value())

                if ((similarity1 + similarity2) / 2 > 0.5):
                    similarity3 = (similarity1 + similarity2) / 2
                    query = """ MATCH (a:website {name: $domain1}), (b:website {name: $domain2}) MERGE (a)-[:SIMILAR_TO {similarity: $score}]->(b)"""
                    result = session.run(query, domain1=domain1, domain2=domain2, score=similarity3)



# domain="ww.w6455.szbaolongjx.com"
# sim(domain)

# driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "a109122392"))
#
# cnx = pymysql.connect(user='root', password='a109122392', host='127.0.0.1', database='pachong')
#
# cursor = cnx.cursor()
# cursor1 = cnx.cursor()
#
# # 执行查询操作获取数据
# query = ('SELECT `domain` FROM site_info WHERE home_page_html LIKE "%500 Internal Server Error%" AND id > 3500')
# cursor.execute(query)
# for row in cursor:
#     domain = row[0]
#     with driver.session() as session:
#         query = "match (n)-[r]-(w1:website) where n.name= $domain1  delete r"
#         result = session.run(query, domain1=domain)










