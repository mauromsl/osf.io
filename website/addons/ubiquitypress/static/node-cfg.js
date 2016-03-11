var UbiquitypressConfig = require('./ubiquitypressConfig.js');

var url = window.contextVars.node.urls.api + 'ubiquitypress/config/';


// #ubiquitypressScope will only be in the DOM if the addon is properly configured
if ($('#ubiquitypressScope')[0]) {
    new UbiquitypressConfig('#ubiquitypressScope', url);
}
