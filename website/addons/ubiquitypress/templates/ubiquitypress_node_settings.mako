<div id="ubiquitypressScope" class="scripted">

    <h4 class="addon-title">
        <img class="addon-icon" src="/static/addons/ubiquitypress/comicon.png">
        Ubiquitypress
    </h4>

    <!-- Settings Pane -->
    <div class="ubiquitypress-settings">

        <form class="form" data-bind="submit: submitSettings">
            <div>
                <div class="form-group">
                    <label for="forwardUrl">Select a journal</label>
                    <select
                            id="ubiquitypressJournalCode"
                            class="form-control"
                            data-bind="value: url"
                            placeholder="Required"
                            required>

                        <option value="cg"> The Comics Grid</option>
                    </select>
                </div>
            </div>

    <div class="col-md-4">
    { journal_cover }
    </div>
    <div class="col-md-8">{journal_description}</div>

    </div>

</div>

