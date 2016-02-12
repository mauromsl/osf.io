<%inherit file="project/addon/widget.mako" />

<div id="forwardScope" class="scripted">

    <div id="ubiquitypressWidget" data-bind="visible: url() !== null">

        <div>
            This project contains a forward to
            <a data-bind="attr.href: url" target="_blank">grrr</a>.
        </div>

        <div class="spaced-buttons m-t-sm">
            <a class="btn btn-primary" data-bind="click: doRedirect">Redirect</a>
        </div>

    </div>

</div>