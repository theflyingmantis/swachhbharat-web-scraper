import scrapy
import sys
sys.path.append('..')

from items import stateItem


class stateScraper:
	"""Scrapes the states and UT data column wise and stores in stateItem"""
	def __init__(self, stateSelector):
		self.stateSelector = stateSelector

	def getData(self):
		columns = self.stateSelector.css('td');
		SNO = self.extractSNO(self.stateSelector)
		State = self.extractState(columns[1])
		ApplicationsReceived = self.extractApplicationsReceived(columns[2])
		ApplicationsNotVerified = self.extractApplicationsNotVerified(columns[3])
		ApplicationsVerified = self.extractApplicationsVerified(columns[4])
		ApplicationsApproved = self.extractApplicationsApproved(columns[5])
		ApplicationsApprovedWithAadhar = self.extractApplicationsApprovedWithAadhar(columns[6])
		ApplicationsRejected = self.extractApplicationsRejected(columns[7])
		ApplicationsPullback = self.extractApplicationsPullback(columns[8])
		ApplicationsClosed = self.extractApplicationsClosed(columns[9])
		ConstructedToiletsPhotos = self.extractConstructedToiletsPhotos(columns[10])
		CommencedToiletPhotos = self.extractCommencedToiletPhotos(columns[11])
		ConstructedToiletsPhotosSwachhalaya = self.extractConstructedToiletsPhotosSwachhalaya(columns[12])
		
		return stateItem(SNO = SNO, State=State, ApplicationsReceived=ApplicationsReceived, ApplicationsNotVerified=ApplicationsNotVerified, \
		 ApplicationsVerified = ApplicationsVerified, ApplicationsApproved=ApplicationsApproved, \
		 ApplicationsApprovedWithAadhar=ApplicationsApprovedWithAadhar, ApplicationsRejected=ApplicationsRejected, \
		 ApplicationsPullback=ApplicationsPullback, ApplicationsClosed = ApplicationsClosed, ConstructedToiletsPhotos=ConstructedToiletsPhotos, \
		 CommencedToiletPhotos=CommencedToiletPhotos, ConstructedToiletsPhotosSwachhalaya=ConstructedToiletsPhotosSwachhalaya)

	def extractSNO(self,selector):
		return selector.css('td::text').extract_first().strip().replace('\n','')

	def extractState(self,selector):
		return selector.css('a::text').extract_first()

	def extractApplicationsReceived(self,selector):
		return selector.css('span::text').extract_first()

	def extractApplicationsVerified(self,selector):
		return selector.css('span::text').extract_first()

	def extractApplicationsNotVerified(self,selector):
		return selector.css('span::text').extract_first()

	def extractApplicationsApproved(self,selector):
		return selector.css('span::text').extract_first()

	def extractApplicationsApprovedWithAadhar(self,selector):
		return selector.css('span::text').extract_first()

	def extractApplicationsRejected(self,selector):
		return selector.css('span::text').extract_first()

	def extractApplicationsPullback(self,selector):
		return selector.css('span::text').extract_first()

	def extractApplicationsClosed(self,selector):
		return selector.css('span::text').extract_first()

	def extractConstructedToiletsPhotos(self,selector):
		return selector.css('span::text').extract_first()

	def extractCommencedToiletPhotos(self,selector):
		return selector.css('span::text').extract_first()

	def extractConstructedToiletsPhotosSwachhalaya(self,selector):
		return selector.css('span::text').extract_first()