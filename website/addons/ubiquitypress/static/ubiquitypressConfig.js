'use strict';

var ko = require('knockout');
require('knockout.punches');
var Raven = require('raven-js');
var $ = require('jquery');
var koHelpers = require('js/koHelpers');
var $osf = require('js/osfHelpers');

ko.punches.enableAll();


/**
 * Knockout view model for the Ubiquitypress node settings widget.
 */
var ViewModel = function(url) {
	var self = this;
	self.upJournals = ko.observableArray([]);
	/**
     * Update the view model from data returned from the server.
     */
    self.updateFromData = function(data) {
        self.journalCode = data.journal_code;
    	self.upJournals(data.journals);
    };

	self.fetchFromServer = function() {
        $.ajax({
            type: 'GET',
            url: url,
            dataType: 'json'
        }).done(function(response) {
            self.updateFromData(response);
        });
    };
    self.fetchFromServer();
    console.log(self.upJournals);

};

function UbiquitypressConfig(selector, url) {
    var self = this;
    self.viewModel = new ViewModel(url);
    $osf.applyBindings(self.viewModel, selector);
}

module.exports = UbiquitypressConfig;
