# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "sales_manufacturing_report"
app_title = "Sales Manufacturing Report"
app_publisher = "Atri Developers"
app_description = "Sales Manufacturing Report"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "developers@atritechnocrat.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sales_manufacturing_report/css/sales_manufacturing_report.css"
# app_include_js = "/assets/sales_manufacturing_report/js/sales_manufacturing_report.js"

# include js, css files in header of web template
# web_include_css = "/assets/sales_manufacturing_report/css/sales_manufacturing_report.css"
# web_include_js = "/assets/sales_manufacturing_report/js/sales_manufacturing_report.js"

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
# get_website_user_home_page = "sales_manufacturing_report.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sales_manufacturing_report.install.before_install"
# after_install = "sales_manufacturing_report.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sales_manufacturing_report.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sales_manufacturing_report.tasks.all"
# 	],
# 	"daily": [
# 		"sales_manufacturing_report.tasks.daily"
# 	],
# 	"hourly": [
# 		"sales_manufacturing_report.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sales_manufacturing_report.tasks.weekly"
# 	]
# 	"monthly": [
# 		"sales_manufacturing_report.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "sales_manufacturing_report.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sales_manufacturing_report.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sales_manufacturing_report.task.get_dashboard_data"
# }

