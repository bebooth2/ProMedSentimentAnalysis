import scrapy
from ..items import DocreviewItem

class ReviewSpider(scrapy.Spider):
	"""this creates the spider for my 
	healthgrades website"""

	items = DocreviewItem()
	name= "reviews"
	url = "https://www.healthgrades.com"
	start_urls =  [
	"https://www.healthgrades.com/find-a-doctor/indiana/best-general-surgeons-in-south-bend"
	    # "https://www.healthgrades.com/find-a-doctor/indiana/best-general-surgeons-in-south-bend",
	    ]
	def parse(self, response):
		doctors = response.css(".provider-details a::text").extract()
		page = response.css(" .provider-details a::attr(href)").extract()
		for count, doc in enumerate(doctors):
			yield scrapy.Request(url = ReviewSpider.url+page[count], callback= self.parse2)
		
	def parse2(self, response):

		patient_reviews = response.css(".c-single-comment__comment::text , .c-single-comment__comment span::text").extract()
		# patient_re = response.css("div.c-comment-list__show-more > div.c-single-comment__comment> span::text").extract()
		# print(patient_re)
		doctor= response.css("h1._12gWC::text").extract()
		ReviewSpider.items["doctor"]= str(doctor)
		ReviewSpider.items["review"]= patient_reviews
		yield ReviewSpider.items
			



	
		
