jQuery(function ($) {
    'use strict';

    // Initialize django-file-form
    $('form').get().forEach(function (form) {
        // Prevent initilising it multiple times and run it for forms
        // that have a `form_id` field added by django-file-form.
        if (!form.initUploadFieldsDone && form.querySelector('[name=form_id]')) {
            init(form);
            form.initUploadFieldsDone = true;
        }
    });

    function init(form) {
        window.initUploadFields(form);

        // Hide wrapper elements for hidden inputs added by django-file-form
        $('input[type=hidden]').closest('.form__group').hide();
    }

});
