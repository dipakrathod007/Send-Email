import frappe
import json
from frappe.utils.pdf import get_pdf

@frappe.whitelist()
def fetch_email_data(inames):
    inames = json.loads(inames)
    print("Fetching email data:---------", inames)
    
    recipients = ['drathod@dexciss.com']
    attachments = []

    for i in inames:
        sales_invoice_data = frappe.db.sql("""
            SELECT DISTINCT sii.parent, si.posting_date
            FROM `tabSales Invoice Item` sii
            JOIN `tabSales Invoice` si ON si.name = sii.parent
            WHERE sii.item_code = %s
            ORDER BY si.modified DESC
            LIMIT 5
        """, i, as_dict=True)

        for sales_data in sales_invoice_data:
            pdf_content = get_pdf(frappe.get_print("Sales Invoice", sales_data.parent, ""))
            attachments.append({
                "fname": f"{sales_data.parent}.pdf",
                "fcontent": pdf_content
            })

    frappe.sendmail(
        recipients=recipients,
        subject = "Sales Invoice Details",
        template='demo',
        args={
            "name": "Dipak Rathod",
            "sid": sales_invoice_data,
            "item_code":inames
        },
        header='Sales Invoice Item',
        attachments=attachments,
        now=True
    )