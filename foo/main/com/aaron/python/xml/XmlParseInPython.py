"""
Python中的Xml数据解析
"""

import xml
import xml.sax


class QueryOrderHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.data = ""
        self.OrgID = ""
        self.UserName = ""
        self.AuthKey = ""
        self.Version = ""

    def endElement(self, name):
        super().endElement(name)

    def startDocument(self):
        super().startDocument()

    def characters(self, content):
        super().characters(content)


xmlString = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<AvailabilityRequest SessionId="{{sessionId}}">
    <Authentication>
        <OrgID>{{OrgID}}</OrgID>
        <UserName>{{HaoQiaoUserName}}</UserName>
        <AuthKey>{{AuthKey}}</AuthKey>
        <Version>{{Version}}</Version>
    </Authentication>
    <HotelRequest>
        <ReqType>query</ReqType>
        <Booking>
            <BookingID>11709016087227</BookingID>
            <PartnerBookingID>5000007516</PartnerBookingID>
        </Booking>
    </HotelRequest>
</AvailabilityRequest>"""

xml.sax.parseString(xmlString, QueryOrderHandler)