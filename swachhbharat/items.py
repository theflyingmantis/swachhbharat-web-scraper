import scrapy
#Data Models for Swachhbharat namely for states and districts

class stateItem(scrapy.Item):
    SNO = scrapy.Field()
    State = scrapy.Field()
    ApplicationsReceived = scrapy.Field()
    ApplicationsNotVerified = scrapy.Field()
    ApplicationsVerified = scrapy.Field()
    ApplicationsApproved = scrapy.Field()
    ApplicationsApprovedWithAadhar = scrapy.Field()
    ApplicationsRejected = scrapy.Field()
    ApplicationsPullback = scrapy.Field()
    ApplicationsClosed = scrapy.Field()
    ConstructedToiletsPhotos = scrapy.Field()
    CommencedToiletPhotos = scrapy.Field()
    ConstructedToiletsPhotosSwachhalaya = scrapy.Field()
    pass

class districtItem(scrapy.Item):
    SNO = scrapy.Field()
    District = scrapy.Field()
    State = scrapy.Field()
    ApplicationsReceived = scrapy.Field()
    ApplicationsNotVerified = scrapy.Field()
    ApplicationsVerified = scrapy.Field()
    ApplicationsApproved = scrapy.Field()
    ApplicationsApprovedWithAadhar = scrapy.Field()
    ApplicationsRejected = scrapy.Field()
    ApplicationsPullback = scrapy.Field()
    ApplicationsClosed = scrapy.Field()
    ConstructedToiletsPhotos = scrapy.Field()
    CommencedToiletPhotos = scrapy.Field()
    ConstructedToiletsPhotosSwachhalaya = scrapy.Field()
    pass
