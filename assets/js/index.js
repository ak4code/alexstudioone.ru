import UIkit from 'uikit';
import Icons from 'uikit/dist/js/uikit-icons';
import '../scss/theme.scss';


UIkit.use(Icons);


const _feedForm = $('#feed-form');
const _feedModal = $('#feed-modal');


_feedForm.submit(function (evt) {
    evt.preventDefault();
    $.ajax({
        type: _feedForm[0].method,
        url: _feedForm[0].action,
        data: $(_feedForm).serialize(),
        beforeSend: function (xhr) {
            _feedModal.html(`
                    <div class="uk-card uk-card-default uk-card-body">
                    <p class="uk-text-center uk-text-lead">
                    <span uk-spinner="ratio: 4.5"></span>
                    </p>
                    <button class="uk-button uk-align-center uk-text-center uk-button-default uk-modal-close" type="button">Закрыть</button>
                    </div>
                `);
        }
    })
        .done(function (res) {
            _feedModal.html(`
                <div class="uk-card uk-card-default uk-card-body">
                <h2 class="uk-card-title uk-heading-divider uk-text-success uk-text-center">Ваша заявка отправлена! </h2>
                <p class="uk-text-center uk-text-lead">
                Мы свяжемся с вами в ближайшее время
                </p>
                <button class="uk-button uk-align-center uk-text-center uk-button-default uk-modal-close" type="button">Закрыть</button>
                </div>
            `);
        });
});