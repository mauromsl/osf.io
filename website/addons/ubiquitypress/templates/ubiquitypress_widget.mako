<%inherit file="project/addon/widget.mako"/>

<div id="ubiquitypressScope" class="scripted">

    <div id="forwardWidget" data-bind="visible: url() !== null">

        <div>
            This project contains a forward to
            <a data-bind="attr.href: url" target="_blank">{{ linkDisplay }}</a>.
        </div>

        <div class="spaced-buttons m-t-sm">
            <a class="btn btn-primary" data-bind="click: doRedirect">Redirect</a>
        </div>

    </div>

</div>


{{ test }}

testing how this works
