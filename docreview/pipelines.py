# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3



class DocreviewPipeline(object):

	def __init__(self):
		self.create_connection()
		self.create_table()

	def create_connection(self):
		self.conn = sqlite3.connect("reviews.db")
		self.cur = self.conn.cursor()

	def create_table(self):
		self.cur.execute("""DROP TABLE IF EXISTS reviews_tb""")
		self.cur.execute(""" CREATE TABLE reviews_tb(
							doctor text,
							patient_reviews text)""")
	def process_item(self, item, spider):
		self.store_db(item)
		return item

	def store_db(self, item):
		self.cur.execute(""" INSERT INTO reviews_tb VALUES(?,?)""",(
				item["doctor"],
				str(item['review'])))
		
		self.conn.commit()

   


