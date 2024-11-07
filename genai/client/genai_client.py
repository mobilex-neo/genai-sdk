from ctypes import Array

from genai.models import Message


class GenAI():
	def __init__(self, api_key:str, api_secret:str):
		pass

	def contexts(self, app_id:str):
		pass

	def context(self, context_id:str):
		pass

	def ingest(self, context_id:str, path:str):
		pass

	def prompt(self, context, prompt:str, documents:Array[str] = [], path:str = "") -> Message:
		pass

	def __ask(self, context_id:str, question:str, documents:Array[str] = []) -> Message:
		pass

	def __chat(self, context_id:str, prompt:str, documents:Array[str] = []) -> Message:
		pass

	def __summarize(self, context_id:str, path:str) -> Message:
		pass

	def __data_understand(self, context_id:str, prompt:str) -> Message:
		pass

	def __code_analysis(self, context_id:str, prompt:str) -> Message:
		pass

