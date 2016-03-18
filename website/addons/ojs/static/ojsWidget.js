'use strict';

var ko = require('knockout');
require('knockout.punches');
var $ = require('jquery');
var $osf = require('js/osfHelpers');

ko.punches.enableAll();

/**
 * Knockout view model for the Forward node settings widget.
 */
var ViewModel = function() {
    console.log('Ubiquity press addon loaded!! 2');
   }

function UbiquitypressWidget(selector) {
    var self = this;
    self.viewModel = new ViewModel();
    $osf.applyBindings(self.viewModel, selector);
}

module.exports = UbiquitypressWidget;
