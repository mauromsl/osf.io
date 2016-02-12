

var url = window.contextVars.node.urls.api + 'ubiquitypress/config/';
// #forwardScope will only be in the DOM if the addon is properly configured
if ($('#forwardScope')[0]) {
    new UbiquitypressConfig('#ubiquitypressScope', url, window.contextVars.node.id);
}
