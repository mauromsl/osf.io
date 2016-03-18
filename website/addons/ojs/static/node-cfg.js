var OjsConfig = require('./ojsConfig.js');

var url = window.contextVars.node.urls.api + 'ojs/config/';


// #ubiquitypressScope will only be in the DOM if the addon is properly configured
if ($('#ojsScope')[0]) {
    new OjsConfig('#ojsScope', url);
}
