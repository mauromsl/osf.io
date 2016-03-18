<div id="ojsScope" class="scripted" style="display: block">

    <h4 class="addon-title">
        <img class="addon-icon" src="/static/addons/ojs/comicon.png">
        OJS - Open Journal Systems
    </h4>

    <!-- Settings Pane -->
    <div class="ojs-settings">

        <form class="form" data-bind="submit: submitSettings">
            <div>
                <div class="form-group">
                    <label for="ojsJournalUrl">Enter the journal url</label>
                    <input
                            id="ojsJournalUrl"
                            type="required"
                            class="form-control"
                            data-bind="value: selectedJournal,"
                            placeholder="required"
                            required>
                    </select>
                </div>
            </div>
            <div class="row">
                <div class="col-md-12"><hr></div>
                <div class="col-md-10 overflow">
                    <p data-bind="html: message, attr.class: messageClass"></p>
                </div>
                <div class="col-md-2">
                    <input type="submit"
                           class="btn btn-success pull-right"
                           value="Save"
                           data-bind="disable: !validators.isValid()"
                    />
                </div>
            </div>
        </form>
    </div>
</div>

