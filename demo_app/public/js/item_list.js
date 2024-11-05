frappe.listview_settings["Item"] = {

    // onload: function(listview) {
    
    // listview.page.add_action_item(__("Send Email"), () => {
    
    // let selected_docs = listview.get_checked_items();
    
    // console.log('selected_docs',selected_docs)
    
    // let items_names = selected_docs.map(doc => doc.name);
    
    // console.log(items_names)
    
    // // frappe.msgprint("Action Clicked",items_names);
    // frappe.call({
    //     method:'demo_app.demo_app.api.fetch_email_data',
    //     args:{inames:items_names},
    //     callback:(r)=>{console.log(r)}
    // })
    
    // });
    
    // },

    onload: function(listview){

        
        listview.page.add_action_item(__("Send Email"), () => {
            let selected_docs = listview.get_checked_items();
    
            console.log('selected_docs',selected_docs)
            
            let items_names = selected_docs.map(doc => doc.name);
            
            console.log(items_names)
            console.log("triger------------------")
            frappe.call({
                method:'demo_app.demo_app.api.fetch_email_data',
                args:{inames:items_names},
                callback:function(r){
                    console.log(r)
                }
            })
        })
    }
    
    };