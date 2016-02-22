'use strict';

var ko = require('knockout');
require('knockout.punches');
var Raven = require('raven-js');
var $ = require('jquery');
var koHelpers = require('js/koHelpers');
var $osf = require('js/osfHelpers');

ko.punches.enableAll();

ko.extebders


/**
 * Knockout view model for the Ubiquitypress node settings widget.
 */
var ViewModel = function(url) {

	var self = this;
	self.upJournals = ko.observableArray([{code:'',full_cover_image_path: null, name: ''}]);
	self.selectedJournal = ko.observable();

	self.selectedJournalCode = ko.computed(function() {
		return self.selectedJournal().code
	}, self, {deferEvaluation: true});

	self.coverImagePath = ko.computed(function(){
		return self.selectedJournal().full_cover_image_path; 
	}, self, {deferEvaluation: true});

	self.journalDescription = ko.computed(function(){
		return self.selectedJournal().short_description; 
	}, self, {deferEvaluation: true});


	/**
     * Update the view model from data returned from the server.
     */
    self.updateFromData = function(data) {
    	if (data.journal_code) {
        	self.selectedJournal(data.journal_code);
       	}
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

    /**
    *Generate cover url
    */


};



function UbiquitypressConfig(selector, url) {
    var self = this;
    self.viewModel = new ViewModel(url);
    $osf.applyBindings(self.viewModel, selector);
}

module.exports = UbiquitypressConfig;

