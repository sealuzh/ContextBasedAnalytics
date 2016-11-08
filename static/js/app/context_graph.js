//require jquery
//require app/renderer

var ContextGraph = {

    api_endpoint_url_template : "/contextgraph/expand/{service_name}/{node_id}/{start}/{end}",

    date_range : { start : 0, end : 0 },

    last_config : { cy: null, service_name: '', node: '', node_id: '' },

    set_last_config : function(cy, service_name, node, node_id) {
        ContextGraph.last_config.cy = cy;
        ContextGraph.last_config.service_name = service_name;
        ContextGraph.last_config.node = node;
        ContextGraph.last_config.node_id = node_id;
    },

    set_date_range : function(range) {
        ContextGraph.date_range.start = range.start.format('x');
        ContextGraph.date_range.end = range.end.format('x');

        //trigger active views to "reload"
        ContextGraph.reload_data();
    },

    reload_data : function() {
        if(ContextGraph.last_config.cy === null) { return; }

        ContextGraph.retrieve_data(
            ContextGraph.last_config.cy,
            ContextGraph.last_config.service_name,
            ContextGraph.last_config.node,
            ContextGraph.last_config.node_id
        );
    },

    // TODO: this is very tightly coupled to cytoscape.js, should be decoupled somehow
    expand_nodes : function(cy, node_id, expand_nodes) {
        var nodes = [];
        for(i=0; i < expand_nodes.length; i++) {
            var new_node_id = expand_nodes[i]['data']['id'];
            nodes.push({ group: "nodes", data: { id: new_node_id, name: expand_nodes[i]['data']['name'] } });
            nodes.push({ group: "edges", data: { source: node_id, target: new_node_id } })
        }

        cy.add(nodes);
        var layout = cy.makeLayout({ name: 'grid' });
        layout.run();
    },

    remove_child_nodes : function(cy, node, node_id) {
        var edges = cy.elements('edge[source="' + node_id + '"]');
        for(var i=0; i < edges.length; i++) {
            cy.remove(edges[i].target());
        }
        node.removeClass('selected');
        var layout = cy.makeLayout({ name: 'grid' });
        layout.run();
    },

    // TODO: this is also very tightly coupled to cytoscape
    is_selected : function(node) {
        return node['_private'].classes.selected == true;
    },

    render_data : function(service_name, node_id, data) {
        // TODO: too coupled to this particular context model, list should be retrieved from central renderer

        node_ = node_id.split(':');
        node_type = node_[0];
        if(node_.length > 1) {
            node_parameter = node_[1];
        }

        node_entity_renderer_map = {
            'cpu' : NodeEntityRenderer.timeseries_list,
            'jitter' : NodeEntityRenderer.timeseries_list,
            'code_fragment' : NodeEntityRenderer.code_fragment,
            'disk' : NodeEntityRenderer.keyvalue_list,
            'memory' : NodeEntityRenderer.timeseries_list
        };

        node_entity_renderer_map[node_type](service_name, node_id, data);
    },

    retrieve_data : function(cy, service_name, node, node_id) {
        ContextGraph.set_last_config(cy, service_name, node, node_id);

        var url = ContextGraph.parse_url(ContextGraph.api_endpoint_url_template,
                                        {'service_name' : service_name, 'node_id' : node_id,
                                         'start' : this.date_range.start, 'end' : this.date_range.end });

        $.getJSON(url, function(results) {
            var data = results['data'];
            var expand_nodes = results['expand_nodes'];

            ContextGraph.expand_nodes(cy, node_id, expand_nodes);
            ContextGraph.render_data(service_name, node_id, data);

            node.addClass('selected');
        });
    },

    //@staticmethod
    parse_url : function(url_template, value_map) {
        var url = url_template;
        for(var name in value_map) {
            url = url.replace("{" + name + "}", value_map[name]);
        }
        return url;
    }

};