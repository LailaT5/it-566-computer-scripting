"""Implements application business logic."""
from persistence_wrapper_interface import PersistenceWrapperInterface
from mysql_persistence_wrapper import MySQLPersistenceWrapper
import json

class BusinessLogic(object):

	def __init__(self):
		self._persistence_wrapper = MySQLPersistenceWrapper()
	

	def get_all_inventories(self):
		query_results = None
		#inventory_list = []
		try:
			query_results = self._persistence_wrapper.get_all_inventories()
		except Exception as e:
			print(f'Exception in business logic: {e}')

		return query_results

	def get_all_inventories_with_format(self, format: str):
		query_results = None
		#inventory_list = []
		try:
			query_results = self._persistence_wrapper.get_all_inventories()
		except Exception as e:
			print(f'Exception in business logic: {e}')

		return_results = None
		match format:
			case 'json': return_results = json.dumps(query_results)

		return return_results


	def create_new_inventory(self, name: str, description: str, date: str):
		inventory_id = 0
		try:
			inventory_id = self._persistence_wrapper.create_inventory(name, description, date)

		except Exception as e:
			print(f'Exception in business logic: {e}')
		
		return inventory_id

	def get_items_for_inventory_id(self, id):
		query_results = None
		try:
			query_results = self._persistence_wrapper.get_items_for_inventory(id)
		except Exception as e:
			print(f'Exception in business logic: {e}')

		return query_results


	