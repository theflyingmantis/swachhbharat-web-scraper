import scrapy
import sys
sys.path.append('..')
from scrapy.http import FormRequest

from scrapers.state_scraper import stateScraper
from scrapers.district_scraper import districtScraper
from data_dumpers import stateDataDumper,districtDataDumper
from config import URL,HEADERS,NO_OF_STATES


class stateSpider(scrapy.Spider):
    name = "state"
    start_urls = [
        URL
    ]
    def parse(self, response):
    	"""
    	Receives the response of the URL. Sends it to scrapeStateData() for scraping the desired fields

    	"""
       	self.scrapeStateData(response)

    def scrapeStateData(self,response):
    	"""
    	Scrapes the states and their data
    	"""
    	statesList = response.xpath('//table[@id="ContentPlaceHolder1_gvApplicationListState"]').css('tr.newRowStyleReport')
    	stateData = []
    	for state in statesList:
    		stateData.append(stateScraper(state).getData())
    	stateDataDumper().dump(stateData)


class districtSpider(scrapy.Spider):
	name = "district"
	start_urls = [
	    URL
	]
	def parse(self, response):
		"""
		Parses the districts of each state 
		in the given url for the data
		"""
		districtDataDumper().createHeading()
		print "\nCrawling Districts\n"
		for state in range(1,NO_OF_STATES+1):
			data = {}
			if state<9:
				state_string='0'+str(state+1)
			else: 
				state_string = str(state+1)
			#Sedning a post for request to open the links
			data['__EVENTTARGET'] = 'ctl00$ContentPlaceHolder1$gvApplicationListState$ctl'+state_string+'$lnkSTATE_NAME'
			data['__VIEWSTATE'] = response.xpath("//input[@id = '__VIEWSTATE']/@value").extract_first()
			data['ctl00$ScriptManager1'] = 'ctl00$ContentPlaceHolder1$uppnlApplication_id|ctl00$ContentPlaceHolder1$gvApplicationListState$ctl14$lnkSTATE_NAME'
			data['__VIEWSTATEGENERATOR'] = '94FEA955'
			data['__VIEWSTATEENCRYPTED'] = ''
			data['__ASYNCPOST'] = 'true'
			yield FormRequest(url=URL,method='POST',callback=self.scrapeDistrict,formdata=data,dont_filter=True,headers=HEADERS,meta={'index':state})

	def scrapeDistrict(self,response):
		"""
		Scrapes the districts for a particular state response it
		received after the post request sent in parse()
		""" 
		stateName=response.xpath('//*[(@id = "ContentPlaceHolder1_gvSTATECommon")]//td[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]').css('a::text').extract_first()
		districtList = response.xpath('//table[@id="ContentPlaceHolder1_gvApplicationListDistrict"]').css('tr.newRowStyleReport')
		stateWiseDistrictData = []
		for district in districtList:
			stateWiseDistrictData.append(districtScraper(district).getData(stateName))
		districtDataDumper().dump(stateWiseDistrictData)


	# We can extend this class to subDistricts too by making a subdistricts function which will be
	# called by scrapeDistrict function with a post request and desired params. These sub-districts 
	# can be then scraped by making a scraping class or extending it and then dumping it with the
	# dumping class. 
	