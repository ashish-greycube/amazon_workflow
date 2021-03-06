# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "amazon_workflow"
app_title = "Amazon Workflow"
app_publisher = "GreyCube Technologies"
app_description = "Workflow to assist post selling cycle"
app_icon = "octicon octicon-git-compare"
app_color = "brown"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/amazon_workflow/css/amazon_workflow.css"
# app_include_js = "/assets/amazon_workflow/js/amazon_workflow.js"

# include js, css files in header of web template
# web_include_css = "/assets/amazon_workflow/css/amazon_workflow.css"
# web_include_js = "/assets/amazon_workflow/js/amazon_workflow.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "amazon_workflow.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "amazon_workflow.install.before_install"
# after_install = "amazon_workflow.install.after_install"

# Fixtures
# ----------
fixtures = ['Workflow', 'Workflow State', 'Workflow Action Master']

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "amazon_workflow.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Issue": {
		"on_update": "amazon_workflow.api.update_issue_on_go_back_action",
		"on_update_after_submit": "amazon_workflow.api.update_issue_on_go_back_action",
		"on_change":"amazon_workflow.api.update_issue_on_go_back_action",
		"before_save":"amazon_workflow.api.update_issue_on_go_back_action",
		"validate":"amazon_workflow.api.update_issue_on_go_back_action"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"amazon_workflow.tasks.all"
# 	],
# 	"daily": [
# 		"amazon_workflow.tasks.daily"
# 	],
# 	"hourly": [
# 		"amazon_workflow.tasks.hourly"
# 	],
# 	"weekly": [
# 		"amazon_workflow.tasks.weekly"
# 	]
# 	"monthly": [
# 		"amazon_workflow.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "amazon_workflow.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "amazon_workflow.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "amazon_workflow.task.get_dashboard_data"
# }

