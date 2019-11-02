# Copyright (c) 2013, halima and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def execute(filters=None):
    columns = get_column()
    data = get_data(filters)
    return columns, data


def get_column():
    return [
        _("Sales Order") + ":Link/Sales Order:100",
        _("Work Order") + ":Link/Work Order:100",
        _("Production Plan") + ":Link/Production Plan:100",
        _("Item Name") + ":Data/Item Name:300",
        _("Stock Entry Type") + ":Data/Stock Entry Type:100",
        _("Stock Item Group") + ":Data/Stock Item Group:100",
        _("Quantity") + ":Data/Quantity:100",
        _("UOM") + ":Data/UOM:100",
        _("Valuation Rate") + ":Data/Valuation Rate:100",
        _("Amount") + ":Data/Amount:100",
    ]


def get_data(filters):
    sale_order = filters.salesOrder
    production_plan = filters.productionPlan
    item_group = filters.itemGroup
    filterItemGroup = tuple(item_group)
    stock_entry_type = "Manufacture"

    # fetch report columns value
    if(filterItemGroup):
        response = frappe.db.sql(""" SELECT SOD.sales_order, WO.name, WO.production_plan, 
                SED.item_code, SE.stock_entry_type, SED.item_group, 
                SUM(ROUND(SED.qty, 3)), SED.uom, SED.basic_rate,
                (SED.qty * SED.basic_rate) as amount
            FROM `tabWork Order` as WO
                JOIN `tabStock Entry` as SE
                    ON SE.work_order = WO.name
                JOIN `tabStock Entry Detail` as SED
                    ON SED.parent = SE.name
                JOIN `tabProduction Plan` as PP
                    ON PP.name = WO.production_plan
                JOIN `tabProduction Plan Sales Order` as SOD
                    ON SOD.parent = WO.production_plan
            WHERE WO.production_plan = %s AND SOD.sales_order = %s AND SE.stock_entry_type = %s
                AND SED.item_group IN %s
            GROUP BY SOD.sales_order, WO.name, WO.production_plan, SED.item_code """, 
        (production_plan, sale_order, stock_entry_type, filterItemGroup), as_list=1)
    else:
        response = frappe.db.sql(""" SELECT SOD.sales_order, WO.name, WO.production_plan, 
                SED.item_code, SE.stock_entry_type, SED.item_group, 
                SUM(ROUND(SED.qty, 3)), SED.uom, SED.basic_rate,
                (SED.qty * SED.basic_rate) as amount
            FROM `tabWork Order` as WO
                JOIN `tabStock Entry` as SE
                    ON SE.work_order = WO.name
                JOIN `tabStock Entry Detail` as SED
                    ON SED.parent = SE.name
                JOIN `tabProduction Plan` as PP
                    ON PP.name = WO.production_plan
                JOIN `tabProduction Plan Sales Order` as SOD
                    ON SOD.parent = WO.production_plan
            WHERE WO.production_plan = %s AND SOD.sales_order = %s AND SE.stock_entry_type = %s
            GROUP BY SOD.sales_order, WO.name, WO.production_plan, SED.item_code """, 
        (production_plan, sale_order, stock_entry_type), as_list=1)
    
    # fetch production quontity and Item rate to display summary
    summary = frappe.db.sql(""" SELECT PP.total_produced_qty
        FROM `tabProduction Plan` as PP
        WHERE PP.name = %s """, (production_plan), as_list=1)

    totalQty = 0
    totalAmount = 0
    totalValuation = 0
    for sale in response:
        totalQty = totalQty + sale[6]
        totalAmount = totalAmount + sale[9]
        totalValuation = totalValuation+ sale[8]
    
    totalCostPerUOM = 0
    if (totalAmount != 0):
        totalCostPerUOM = float("{0:.3f}".format(totalAmount / summary[0][0]))
    
    totalAmount = float("{0:.3f}".format(totalAmount))
    totalQty = float("{0:.3f}".format(totalQty))
    totalValuation = float("{0:.3f}".format(totalValuation))

    # temporary quick solution
    response.append(['<b>Total</b>', '', '', '', '', '', totalQty, '', totalValuation, totalAmount])
    response.append(['<b>Manufacturing Cost per UOM</b>', '', '', '', '', '', '', '', '', totalCostPerUOM])
    return response


@frappe.whitelist()
def get_production_plan(sales_order):
    response = frappe.db.sql(""" SELECT PP.name as value
        FROM `tabProduction Plan Sales Order` as PPSO
        JOIN `tabProduction Plan` as PP
            ON PPSO.parent = PP.name
        WHERE PP.docstatus != 2 AND PPSO.sales_order = %s 
        GROUP BY PP.name """, (sales_order), as_dict=True)
    return response
