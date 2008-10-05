/**
 * @author aaloy
 */

Ext.namespace('agendaSpace');

agendaSpace.app = function() {
	 // private variables
	 	
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
		
		function getGrid(){
			return new Ext.grid.GridPanel({
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
					width: 160,
					sortable: true,
					dataIndex: 'comments'
				}, ],
				viewConfig: {
					forceFit: true
				},
				renderTo: 'content',
				title: 'Agenda list',
				width: 800,
				frame: true,
				loadMask: true,
				sm: new Ext.grid.RowSelectionModel({
					singleSelect: true
				}),
			});
		}
		
	// private functions
	function datos_cargados(){
		  var grid = getGrid();
		  grid.show();
		  grid.getSelectionModel().selectFirstRow();
	}
	// public space
	return {
		init: function () {
			ds.load({callback:datos_cargados});
		}
	}
}


Ext.onReady(function() {
    new agendaSpace.app().init();
});