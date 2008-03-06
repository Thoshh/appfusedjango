/**
 * @author aaloy
 */

Ext.onReady(function() {

	   var AgendaRecord = Ext.data.Record.create([        
                {name: 'first_name', mapping: 'fields.first_name'},
                {name: 'last_name', mapping: 'fields.last_name'},
                {name: 'phone',mapping: 'fields.phone'},
                {name: 'age',mapping: 'fields.age'},
                {name: 'comments',mapping: 'fields.comments'}
        ]);
	
		var ds = new Ext.data.Store({
		    proxy: new Ext.data.HttpProxy({url: "/agenda/json/list/"}),
		    reader: new Ext.data.JsonReader({
		        root: 'rows',
		        totalProperty: 'total',
				id: 'pk'
		    }, [        
                {name: 'first_name', mapping: 'fields.first_name'},
                {name: 'last_name', mapping: 'fields.last_name'},
                {name: 'phone',mapping: 'fields.phone'},
                {name: 'age',mapping: 'fields.age'},
                {name: 'comments',mapping: 'fields.comments'}
                ]
			)
		});  

        function datos_cargados(){		
			var grid = new Ext.grid.GridPanel({
				store: ds,
				columns: [{
					header: 'First Name',
					width: 120,
					sortable: true,
					dataIndex: 'first_name'
				}, {
					header: 'Last Name',
					width: 120,
					sortable: true,
					dataIndex: 'last_name'
				}, {
					header: 'Phone',
					width: 60,
					sortable: true,
					dataIndex: 'phone'
				}, {
					header: 'Age',
					width: 60,
					sortable: true,
					dataIndex: 'age'
				}, {
					header: 'Comments',
					width: 60,
					sortable: true,
					dataIndex: 'comments'
				}, ],
				viewConfig: {
					forceFit: true
				},
				renderTo: 'content',
				title: 'Agenda list',
				width: 500,
				frame: true,
				loadMask: true,
				sm: new Ext.grid.RowSelectionModel({singleSelect:true}),
			});
			grid.show();
			grid.getSelectionModel().selectFirstRow();
		}
        ds.load({callback:datos_cargados});
});