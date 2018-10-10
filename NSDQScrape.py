import urllib2
from bs4 import BeautifulSoup

def getPremarketPrices(symbols):

	results = []

	for sym in symbols:

		targetPage = "https://www.nasdaq.com/symbol/" + sym + "/premarket"

		# Get page HTML code and make soup
		pageCode = urllib2.urlopen(targetPage)
		soup = BeautifulSoup(pageCode, "html.parser")

		# Select the div which contains the percentage change
		changeLine = soup.select_one("div[id=qwidget_percent]")
		
		# Check for a non-result
		if changeLine is None:
			print "No data for", sym
		else:
			# Remove the percentage symbol from the price
			changeStr = changeLine.text.strip()[:-1]
			
			# Check for non-result
			if len(changeStr) > 0:
				change = float(changeStr)

				# Prices are displayed with green or red text rather than a 
				# positive or negative sign. If red we make the change negative
				if "qwidget-Red" in str(changeLine):
					change = -change

				results.append((sym, change))
			else:
				print "No data for", sym

	return results


