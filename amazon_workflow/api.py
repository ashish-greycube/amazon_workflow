from __future__ import unicode_literals
import frappe, erpnext
import frappe.defaults
from frappe import msgprint, _


def update_issue_on_go_back_action(self,method):
	print('---===============')
	print('method',method)
	print('workflow_state',self.workflow_state,'status',self.status,'docstatus',self.docstatus,'issue_type',self.issue_type)
	workflow_action=frappe.db.get_list('Workflow Action',
    filters={
        'reference_name': self.name,
		'reference_doctype':'Issue'
    },
    fields=['status', 'user','workflow_state'],
    as_list=True
)
	print(workflow_action,len(workflow_action))
	print('----------------------------------------------------')

	if (len(workflow_action)==1):
		workflow_action_status=workflow_action[0][0]
		workflow_action_workflow_state=workflow_action[0][2]
		if (self.workflow_state=='Open' and self.status=='Closed' and self.docstatus==0 and self.issue_type==None and workflow_action_status=='Open' and workflow_action_workflow_state=='Open' ):
			self.db_set('status', workflow_action_status, update_modified = True)
			print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++finally in')
			print(workflow_action_status,workflow_action_workflow_state)