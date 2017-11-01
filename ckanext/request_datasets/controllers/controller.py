import ckan.plugins as plugins
import ckan.lib.base as base
import ckan.model as model
import ckan.lib.helpers as helper
from ckan.plugins import toolkit
from ckan.common import request, c, config


import logging
log = logging.getLogger(__name__)

class RequestDatasetsController(base.BaseController):
    def new(self):
        return plugins.toolkit.render('request_datasets/new.html')

    def save_new(self):
        if request.method == 'POST':
            context = {'model': model, 'session': model.Session,
                   'user': toolkit.c.user or toolkit.c.author, 'for_view': True,
                   'auth_user_obj': toolkit.c.userobj}
            new_title = request.POST.get('title')
            new_content = request.POST.get('notes')
	    new_email = request.POST.get('email')
	    data_dict = {'title': new_title, 'content': new_content, 'email': new_email}
	    try:
	        toolkit.get_action('ckanext_request_datasets_save_new')(context, data_dict)
                helper.flash_success('The request has been sent')
            except toolkit.ObjectNotFound:
		abort(404, 'The request cannot be sent')

	return plugins.toolkit.render('request_datasets/new.html')
