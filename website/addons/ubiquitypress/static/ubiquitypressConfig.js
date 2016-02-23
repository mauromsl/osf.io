'use strict';

var ko = require('knockout');
require('knockout.punches');
var Raven = require('raven-js');
var $ = require('jquery');
var koHelpers = require('js/koHelpers');
var $osf = require('js/osfHelpers');

ko.punches.enableAll();

var MESSAGE_TIMEOUT = 5000;



/**
 * Knockout view model for the Ubiquity Press node settings widget.
 */
var ViewModel = function(url) {

	var self = this;
	self.upJournals = ko.observableArray([{code:'',full_cover_image_path: null, name: ''}]);
	self.selectedJournal = ko.observable().extend({
        required: true
    });

	self.selectedJournalCode = ko.computed(function() {
		return self.selectedJournal().code
	}, self, {deferEvaluation: true});

	self.coverImagePath = ko.computed(function(){
		return self.selectedJournal().full_cover_image_path; 
	}, self, {deferEvaluation: true});

	self.journalDescription = ko.computed(function(){
		return self.selectedJournal().short_description; 
	}, self, {deferEvaluation: true});

	// Flashed messages
    self.message = ko.observable('');
    self.messageClass = ko.observable('text-info');

    self.validators = ko.validatedObservable({
        url: self.url,
    });


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

    function onSubmitSuccess() {
        self.changeMessage(
            'Journal selection saved:' + self.selectedJournal().name,
            'text-success',
            MESSAGE_TIMEOUT
        );
    }

    function onSubmitError(xhr, status) {
        self.changeMessage(
            'Could not change settings. Please try again later.',
            'text-danger'
        );
    }

    /**
     * Submit new settings.
     */
    self.submitSettings = function() {
        $osf.putJSON(
            url,
            {journal_code: self.selectedJournal().code}
        ).done(
            onSubmitSuccess
        ).fail(
            onSubmitError
        );
    };

    /** Change the flashed message. */
    self.changeMessage = function(text, css, timeout) {
        self.message(text);
        var cssClass = css || 'text-info';
        self.messageClass(cssClass);
        if (timeout) {
            // Reset message after timeout period
            setTimeout(function() {
                self.message('');
                self.messageClass('text-info');
            }, timeout);
        }
    };



};



function UbiquitypressConfig(selector, url) {
    var self = this;
    self.viewModel = new ViewModel(url);
    $osf.applyBindings(self.viewModel, selector);
}

module.exports = UbiquitypressConfig;

