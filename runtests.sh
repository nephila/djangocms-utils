cd tests/
virtualenv djangocms_utils_env
djangocms_utils_env/bin/pip install -r requirements.txt
djangocms_utils_env/bin/python testapp/manage.py test djangocms_utils