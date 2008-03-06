/**
 * @author aaloy
 */

Ext.onReady(function() {
	
		var ds = new Ext.data.Store({
		    proxy: new Ext.data.HttpProxy({url: "/agenda/json/list/"}),
		    reader: new Ext.data.DjangoJsonReader({
		        root: 'rows',
		        totalProperty: 'total'
		    }, [
		        {name: 'first_name'},
		        {name: 'last_name'},
				{name: 'phone'},
				{name: 'age'},
				{name: 'comments'}
		    ])
		});  

        ds.load();		
        var grid = new Ext.grid.GridPanel({
                store: ds,				
                columns: [
                        {header: 'First Name', width: 120, sortable: true, dataIndex: 'first_name'},
                        {header: 'Last Name', width: 120, sortable: true, dataIndex: 'last_name'},
                ],                
                viewConfig: {
                        forceFit: true
                },
                renderTo: 'content',
                title: 'Agenda list',
                width: 500,
                frame: true
        });

        grid.getSelectionModel().selectFirstRow();
});