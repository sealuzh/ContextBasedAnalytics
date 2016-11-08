var CytospaceConfig = {

    style : cytoscape.stylesheet()
                .selector('node')
                  .css({
                    'content': 'data(name)',
                    'text-valign': 'center',
                    'color': 'white',
                    'text-outline-width': 2,
                    'text-outline-color': '#888'
                  })
                .selector('edge')
                  .css({
                    'target-arrow-shape': 'triangle'
                  })
                .selector('.selected')
                  .css({
                    'background-color': 'darkblue'
                    /*'line-color': 'black',
                    #'target-arrow-color': 'black',
                    'source-arrow-color': 'black'*/
                  })
                .selector('.faded')
                  .css({
                    'opacity': 0.25,
                    'text-opacity': 0
                  }),


    layout:  {
                name: 'grid',
                padding: 10
              }

};