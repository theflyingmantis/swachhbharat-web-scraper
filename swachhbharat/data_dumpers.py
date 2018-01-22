import csv

class stateDataDumper:
	"""Dumps the data for states in csv file in data folder"""
	def dump(self,states):
		# HeaderName
		fieldNames = ['S.No', 'State', 'No. Of Applications Received', 'No. Of Applications not Verified', \
		'No. Of Applications Verified', 'No. of Applications Approved','No. of Applications Approved having Aadhar No.', \
		'No. of Applications Rejected','No. of Applications Pullback','No. of Applications Closed','No. of Constructed Toilet Photo', \
		'No. of Commenced Toilet Photo','No. of Constructed Toilet Photo through Swachhalaya'] 
		
		with open('data/states_data.csv', 'w') as stateFile:
			csvWriter = csv.writer(stateFile)
			csvWriter.writerow(fieldNames)
			for state in states:
				csvWriter.writerow([state['SNO'],state['State'],state['ApplicationsReceived'], \
					state['ApplicationsNotVerified'],state['ApplicationsVerified'],state['ApplicationsApproved'], \
					state['ApplicationsApprovedWithAadhar'],state['ApplicationsRejected'],state['ApplicationsPullback'], \
					state['ApplicationsClosed'],state['ConstructedToiletsPhotos'],state['CommencedToiletPhotos'], \
					state['ConstructedToiletsPhotosSwachhalaya']])
		stateFile.close()
		print '\n\nState File saved\n\n'


class districtDataDumper:
	"""Dumps the data for districts in csv file in data folder"""	
	def createHeading(self):
		fieldNames = ['District' ,'State', 'No. Of Applications Received', 'No. Of Applications not Verified', \
		'No. Of Applications Verified', 'No. of Applications Approved','No. of Applications Approved having Aadhar No.', \
		'No. of Applications Rejected','No. of Applications Pullback','No. of Applications Closed','No. of Constructed Toilet Photo', \
		'No. of Commenced Toilet Photo','No. of Constructed Toilet Photo through Swachhalaya']
		with open('data/district_data.csv', 'w') as districtFile:
			csvWriter = csv.writer(districtFile)
			csvWriter.writerow(fieldNames)
		districtFile.close()

	def dump(self,districts):		
		with open('data/district_data.csv', 'a') as districtFile:
			csvWriter = csv.writer(districtFile)
			for district in districts:
				csvWriter.writerow([district['District'], district['State'], district['ApplicationsReceived'], \
					district['ApplicationsNotVerified'], district['ApplicationsVerified'], district['ApplicationsApproved'], \
					district['ApplicationsApprovedWithAadhar'], district['ApplicationsRejected'], district['ApplicationsPullback'], \
					district['ApplicationsClosed'], district['ConstructedToiletsPhotos'], district['CommencedToiletPhotos'], \
					district['ConstructedToiletsPhotosSwachhalaya']])
		districtFile.close()