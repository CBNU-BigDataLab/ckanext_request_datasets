import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import logging
#import ckanext.request_datasets.logic.auth
import ckanext.request_datasets.logic.action.create
#import ckanext.theme.logic.action.delete
#import ckanext.theme.logic.action.update
#import ckanext.theme.logic.action.get
#import ckanext.request_datasets.logic.helpers as request_datasets_helpers

import urllib2
import json

log = logging.getLogger(__name__)

class Request_DatasetsPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer),
    plugins.implements(plugins.IRoutes, inherit=True),
    plugins.implements(plugins.ITemplateHelpers),
    plugins.implements(plugins.IAuthFunctions),
    plugins.implements(plugins.IActions)  # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'request_datasets')
    
    def before_map(self, m):
	m.connect('ckanext_request_datasets_new',
		'/request_datasets/new',
		controller='ckanext.request_datasets.controllers.controller:RequestDatasetsController',
		action='new')
        m.connect('ckanext_request_datasets_save_new_request_datasets',
		'/request_datasets/save-new',
		controller='ckanext.request_datasets.controllers.controller:RequestDatasetsController',
		action='save_new')
	return m

    # ITemplateHelper
    def get_helpers(self):
        return {
        
        }

    # IAuthFunctions
    def get_auth_functions(self):
        return { 
        }

    # IActions
    def get_actions(self):
	return {
	    'ckanext_request_datasets_save_new': ckanext.request_datasets.logic.action.create.request_datasets_create
        }
