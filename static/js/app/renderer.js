var NodeEntityRenderer = {

    // TODO: extract common behaviour (setting html content) + introduce abstraction that is not tightly coupled to template engine
    // TODO: this method should only be data cleaning/prep.

    code_fragment : function(service_name, node_id, data) {

        var template_id = "code_fragment";
        var source = $("#" + template_id).html();
        var template = Handlebars.compile(source);
        var html = template({'code' : data});
        var fragment = $("#" + service_name + "-code-fragment-data");
        fragment.html(html);
        //Prism.highlightElement(document.getElementById(service_name + "-code-fragment-data"));
        Prism.highlightAll();
    },

    keyvalue_list : function(service_name, node_id, data) {
        var names = Object.keys(data);
        var template_data = [];
        for(i=0; i < names.length; i++) {
            var v = data[names[i]][0]['value']

            if(v != "0.0") {
                template_data.push({ key: names[i], value: v});
            }
        }

        var template_id = "keyvalue_list";
        var source = $("#" + template_id).html();
        var template = Handlebars.compile(source);
        var html = template(template_data);
        $("#" + service_name + "-" + node_id + "-data").html(html);
    },

    timeseries_list : function(service_name, node_id, data) {
        var names = Object.keys(data);
        var template_data = [];
        for(i=0; i < names.length; i++) {
            template_data.push({ name: names[i], service: service_name, node: node_id, number: i });
        }

        var template_id = "timeseries_list"

        var source = $("#" + template_id).html();
        var template = Handlebars.compile(source);
        var html = template(template_data);
        //TODO: create sub div for connections within right hand side data panel
        $("#" + service_name + "-" + node_id + "-data").html(html);

        // just created div's for charts in this format: connection_list_graph_[number], 0 < number < names.length
        for(i=0; i < names.length; i++) {
            detail_raw_data = data[names[i]];

            var x_axis = ['Time'];
            var detail_data = [node_id];

            for(var j=0; j < detail_raw_data.length; j++) {
                //x_axis.push(detail_raw_data[j]['timestamp'].split(',')[0]);
                x_axis.push(detail_raw_data[j]['timestamp'].split('.')[0]);

                // obviously bad, refactor this
                if(detail_raw_data[j]['response_time']) {
                    detail_data.push(detail_raw_data[j]['response_time']);
                } else {
                    detail_data.push(detail_raw_data[j]['volume']);
                }
            }

            var chart = c3.generate({
                bindto: '#' + service_name + '_' + node_id + '_list_graph_' + i,
                size: {
                    height: '250', width: '500'
                },
                data: {
                    x: 'Time',
                    // 2016-11-08T00:13:13.430000
                    //xFormat: '%Y-%m-%d %H:%M:%S',
                    xFormat: '%Y-%m-%dT%H:%M:%S',
                    columns: [
                        x_axis,
                        detail_data
                    ]
                },
                axis: {
                    x: {
                        type: 'timeseries',
                        tick: {
                            format: '%M:%S'
                        }
                    }
                }
            });
        }
    }
};
