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

    <div class="col-md-4">
        <img data-bind="attr:{src: coverImagePath}">
    </div>
    <div class="col-md-8">{journal_description}</div>
        <span data-bind:"text: journalDescription"></span>
    </div>

</div>

