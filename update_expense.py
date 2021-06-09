#!/usr/bin/env python3

#	import os
import os

#	Build services
from googleapiclient.discovery import build

#	Acess provider
from GoogleAccessApiProvider import GoogleAccessApiProvider

# Spread sheet id for note
DailyIncomeExpense = '1_d1WlrW08qR6mE1to7fQgaP6KJC-_6U5WwOEkrD0l6Y'
MonthlyIncomeExpense = '1PWoP44ke6pM5rrNFgaJsnQkCNtbn0Q1uLuADFE3u33I'

#	Major dimanesion
MajorDimensionName = 'ROWS'

def main():

	#	Initial credential object
	creds = None
	
	#	Define token path
	tokenFilePath = 'tokens/token.pickle'

	#	Get token which store credential data
	if os.path.exists( tokenFilePath ):
	
		#	Load token file path
		creds = GoogleAccessApiProvider.loadCredentialFromTokenFile( tokenFilePath )
	
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not GoogleAccessApiProvider.validateToken( creds ) :
		
		#	Validate creds object and check expire and check able to refresh
		if creds and creds.expired and creds.refresh_token:
			GoogleAccessApiProvider.refreshToken( creds )
		else:
			creds = GoogleAccessApiProvider.createTokenAndSave( tokenFilePath )

	service = build( 'sheets', 'v4', credentials=creds )

	# Call the Sheets API
	sheet = service.spreadsheets()	

	print( sheet )

	# dailyIncomeDict = sheet.values().get( spreadsheetId=DailyIncomeExpense,
	# 							range='Sheet1!A2:B20',
	# 							majorDimension=MajorDimensionName ).execute()
	
	# valueIncomeList = dailyIncomeDict.get( 'values' )

	# #	Get monthly first
	# monthlyIncomeDict = sheet.values().get( spreadsheetId=MonthlyIncomeExpense,
	# 							range='Sheet1!A1:C160',
	# 							majorDimension=MajorDimensionName ).execute()

	# print( monthlyIncomeDict.get( 'values' ) )

	# modifyValueList = monthlyIncomeDict.get( 'values' )

if __name__ == '__main__':
	main()