<div id="ubiquitypressScope" class="scripted" style="display: block">

    <h4 class="addon-title">
        <img class="addon-icon" src="/static/addons/ubiquitypress/comicon.png">
        Ubiquitypress
    </h4>

    <!-- Settings Pane -->
    <div class="ubiquitypress-settings">

        <form class="form" data-bind="submit: submitSettings">
            <div>
                <div class="form-group">
                    <label for="ubiquitypressJournalCode">Select a journal</label>
                    <select
                            id="ubiquitypressJournalCode"
                            class="form-control"
                            data-bind="options: upJournals,
                                optionsText: 'name',
                                value: selectedJournal,"
                            placeholder="required"
                            required>
                    </select>
                </div>
            </div>

            <div class="col-md-3">
                <img data-bind="attr:{src: coverImagePath}">
            </div>
            <div class="col-md-8">
                <span data-bind="html: journalDescription"></span>
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

