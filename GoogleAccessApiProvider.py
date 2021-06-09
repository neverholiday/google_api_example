#!/usr/bin/env python3

#	pickle
import pickle

#   Google authen
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


#   Global variable
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

#	Default credential file
DefaultCredentialFile = 'data/credentials.json'

class GoogleAccessApiProvider( object ):
	'''	Class for provider access to google api
	'''

	@staticmethod
	def createTokenAndSave( tokenPath, credentialFilePath=DefaultCredentialFile ):
		'''	function to create token from token path
		'''
		#	Create flow from api
		flow = InstalledAppFlow.from_client_secrets_file( credentialFilePath, SCOPES )
		
		#	Create credential token
		creds = flow.run_local_server(port=0)

		#	Open file and save to pickle file
		with open( tokenPath, 'wb' ) as tokenFile:
			pickle.dump( creds, tokenFile )

		return creds

	@staticmethod
	def loadCredentialFromTokenFile( tokenPath ):
		'''	function to load credential object from token file
		'''
		
		#	Open token and load cred file
		with open( tokenPath, 'rb' ) as tokenFile:
			creds = pickle.load( tokenFile )

		return creds

	@staticmethod
	def refreshToken( credentialObject ):
		'''	function to refresh credential object
		'''
		
		#	Refresh token
		credentialObject.refresh( Request() )

	@staticmethod
	def validateToken( credentialObject ):
		'''	function to validate token
		'''
		return credentialObject.valid