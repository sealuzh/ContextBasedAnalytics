var DateRange = {

    _observers : [],

    // fn: function with parameters start and end
    register : function(fn) {
        this._observers.push(fn);
    },

    notify : function(start, end) {
        for(var i=0; i < this._observers.length; i++) {
            if(typeof this._observers[i] === "function") {
                this._observers[i]({'start': start, 'end' : end});
            }
        }
    },

    init : function() {
	    var start = moment().subtract(29, 'days');
        var end = moment();
        var _this = this;

        function cb(start, end) {
            $('#daterange span').html(start.format('D.M, hh:mm') + ' - ' + end.format('D.M, hh:mm'));
            _this.notify(start, end);
        }

        $('#daterange').daterangepicker({
    		timePicker: true,
            timePickerIncrement: 30,
            startDate: start,
            endDate: end,
            ranges: {
                'Last 10 minutes': [moment().subtract(10, 'minutes'), moment()],
                'Last 30 minutes': [moment().subtract(30, 'minutes'), moment()],
                'Today': [moment().subtract(24, 'hours'), moment()],
                'Yesterday': [moment().subtract(2, 'days'), moment().subtract(1, 'days')],
                'Last 7 Days': [moment().subtract(6, 'days'), moment()],
                'Last 30 Days': [moment().subtract(29, 'days'), moment()],
                'This Month': [moment().startOf('month'), moment().endOf('month')],
                'Last Month': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
            }
        }, cb);

        cb(start, end);
    }

};