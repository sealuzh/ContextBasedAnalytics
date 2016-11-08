// require jquery
// require cytoscape/config.js

function CytoscapeInit(cy_id, service_name, data) {
    this.service_name = service_name;
    var _this = this;

    $('#' + cy_id).cytoscape({style: CytospaceConfig.style, elements: data, layout: CytospaceConfig.layout,
        ready: function() {
          var cy = this;
          cy.elements().unselectify();

          cy.on('tap', 'node', function(e){
            var node = e.cyTarget;
            var node_id = node['_private'].data.id;

            //deselect and remove all outgoing nodes
            if(ContextGraph.is_selected(node)) {
                ContextGraph.remove_child_nodes(cy, node, node_id);
                return;
            }

            //retrieve data
            ContextGraph.retrieve_data(cy, _this.service_name, node, node_id);


          });
        }
    });
}

// $('#{{cy_id}}').cytoscape

