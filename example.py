import NSDQScrape

# Add all required symbols to a list
symbols = ["GOOG", "AAPL", "NVDA", "TSLA", "BABA", "DBX", "V", "EA"]

# Use the scraper to get the prices
# Results are returned as tuples containing the symbol name and the percentage change
results = NSDQScrape.getPremarketPrices(symbols)

#Nicely print the output
margin = max(len(results[t][0]) for t in xrange(0, len(results))) + 1

for r in results:
	if r[1] > 0:
		print str("$")+r[0].ljust(margin + 1), r[1]
	else:
		print str("$")+r[0].ljust(margin), r[1]