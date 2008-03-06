Ext.data.DjangoJsonReader = function(meta, recordType){
    Ext.data.DjangoJsonReader.superclass.constructor.call(this, meta, recordType);
};
Ext.extend(Ext.data.DjangoJsonReader, Ext.data.JsonReader, {
    readRecords : function(o){
        this.jsonData = o;
        var s = this.meta;
        var sid = s.id;
        var recordType = this.recordType, fields = recordType.prototype.fields;

        var totalRecords = 0;
        if(s.totalProperty){
            var v = parseInt(eval("o." + s.totalProperty), 10);
            if(!isNaN(v)){
                totalRecords = v;
            }
        }
        var records = [];
        var root = s.root ? eval("o." + s.root) : o;
        for(var i = 0; i < root.length; i++){
            var n = root[i];
            var values = {};
            var id = (n[sid] !== undefined && n[sid] !== "" ? n[sid] : n['pk']);
            for(var j = 0, jlen = fields.length; j < jlen; j++){
                var f = fields.items[j];
                var map = f.mapping || f.name;
                var v = n['fields'][map] !== undefined ? n['fields'][map] : f.defaultValue;
                v = f.convert(v);
                values[f.name] = v;
            }
            var record = new recordType(values, id);
            record.json = n;
            records[records.length] = record;
        }
        return {
            records : records,
            totalRecords : totalRecords || records.length
        };
    }
});