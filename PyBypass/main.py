import re
import requests
from PyBypass.Shortners import *
from PyBypass.Filehoster import *
from PyBypass.Constants import *
from PyBypass.GdriveSharer import *
from PyBypass.VideoServers import *



class BypasserNotFoundError(Exception):
	"""
	Raise when there is no bypasser of the giver url.
	"""
		

class UrlConnectionError(Exception):
	"""
	Raise when response code of given url is not equal to 200
	"""
	
	
class RequiredValueNotFoundError(Exception):
	"""
	Raise when user didn't provided required parameters.
	( Example: gdot_crypt, appdrive_email etc )
	"""

class UnableToBypassError(Exception):
	"""
	Raise when script is unable to bypass the given url. 
	( possible reason can be wrong link, wrong parameters or script is patched)
	"""

		
def _requiredvaluechecker(function):
	
	"""
	a decorator to check if required parameters is/are present or not  to bypass 
	the given links
	"""
	
	def wrapper_function(*args, **kwargs):
		
		func_name = args[-1]
		if func_name == "gdtot_bypass":	
			if ("gdtot_crypt" in kwargs) == False:
				raise RequiredValueNotFoundError(" Missing required parameter 'gdtot_crypt'. please enter yout GDOT crypt value")
			
				
		if func_name =="appdrive_bypass":	
			if all([("appdrive_email" in kwargs ), ("appdrive_password" in kwargs)])== False:	
				raise RequiredValueNotFoundError("Missing required parameter 'appdrive_email' and 'appdrive_password. please enter yout appdrive credential value to bypass the given link.")
				
				
		if func_name =="hubdrive_bypass":			
			if ("hubdrive_crypt" in kwargs) == False:
				raise RequiredValueNotFoundError(" Missing required parameter 'hubdrive_crypt'. please enter your hubdrive crypt value")
		
				
		if func_name =="sharerpw_bypass":			
			if all([("sharerpw_xsrf_token" in kwargs ), ("sharerpw_larvel_session" in kwargs)])== False:	
				raise RequiredValueNotFoundError("Missing required parameter 'sharerpw_xsrf_token' and 'sharerpw_larvel_session. please enter yout sharer.pw credential value to bypass the given link.")	
		
		value = function(*args, **kwargs)
		return value	
		
	return wrapper_function


		
class PyBypass:
		
	def _init__(self):
		pass

	@_requiredvaluechecker
	def redirect_function(self, url, bypasser_function, **kwargs):
		
		parameter = ""
		for (key,values) in kwargs.items():
			parameter += f" ,{key}='{values}' "
		parameter = parameter.strip()
	

		try:
			bypassed_value = eval(bypasser_function + f"('{url}'{parameter})")
		except Exception as e:
			print(e)
			raise UnableToBypassError("Can not bypass the given url. possible reason can be wrong link, wrong parameters or script is patched")
	
		
		if bypassed_value == None:
		    raise UnableToBypassError("Can not bypass the given url. possible reason can be wrong link, wrong parameters or script is patched")
		return bypassed_value
		 
		 
									
	def bypass(self, url, name=None, **kwargs):			
		
		try:
			response = requests.get(url)
		except Exception as e:
			raise UrlConnectionError("Can not establish a successful connection with the given url.")
			
		if response.status_code != 200:
				raise UrlConnectionError("Can not establish a successful connection with the given url.")
	
	
		bypasser_function = None
		if name:
		    for (key,value) in MAIN_REGEX.items():
		    	if name.lower() == value[0]:
		    		bypasser_function = value[1] ; break
		    	else:
		    		raise BypasserNotFoundError("Can not find any bypasser script for the given url")
		    		
		else:
			for (key,value) in MAIN_REGEX.items():		
				if bool(re.search(FR"{key}", url)):
					bypasser_function = value[1]						
		
		if bypasser_function is not None:
			return self.redirect_function(url, bypasser_function, **kwargs)
		else:
			raise BypasserNotFoundError("Can not find any bypasser script for the given url")


def bypass(url, name=None, **kwargs):
	bypasser = PyBypass()
	return bypasser.bypass(url , name=name, **kwargs)
	
											
