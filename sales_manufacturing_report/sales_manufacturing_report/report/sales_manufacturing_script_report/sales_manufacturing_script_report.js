frappe.query_reports["Sales Manufacturing Script Report"] = {
	"filters": [
		{
			"fieldname": "salesOrder",
			"label": __("Sales Order"),
            "fieldtype": "Link",
            "options": "Sales Order",
            "reqd": 1,
            "on_change": function(query_report) {
                var salesOrder = query_report.get_values().salesOrder;
                if (!salesOrder) {
                    return;
                }                
				loadFeaturesToView(query_report, salesOrder);
            }
        },
        {
			"fieldname": "productionPlan",
			"label": __("Production Plan"),
            "fieldtype": "Link",
			"options": "Production Plan",
			"reqd": 1,
			"on_change": function(query_report) {
				console.log("event triggered....")
				console.log(query_report)
			}
        },
        // {
		// 	"fieldname": "stockEntryType",
		// 	"label": __("Stock Entry Type"),
        //     "fieldtype": "MultiSelectList",
        //     "default": "Manufacture",
		// 	get_data: function(txt) {
		// 		return frappe.db.get_link_options('Stock Entry Type', txt);
		// 	}
        // },
	]
}

var loadFeaturesToView = function (query_report, salesOrder) {
	console.log(frappe)
	console.log("frappe")
	if (salesOrder) {
		frappe.call({
			method: "sales_manufacturing_report.sales_manufacturing_report.report.sales_manufacturing_script_report.sales_manufacturing_script_report.get_production_plan",
			args: {
				sales_order: salesOrder
			}
		})
			.fail(fail => console.log("fail to fetch record", fail))
			.done(success => {
				console.log(success)
				// frappe.query_report_filters_by_name.salesOrder.get_value();
				// frm.set_df_property('project_feature', 'options', success.message);
				// frm.refresh_field('project_feature');
			})
	}
}
