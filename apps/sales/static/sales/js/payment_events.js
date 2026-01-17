document.addEventListener('DOMContentLoaded', () => {
    initPaymentEvents();
});

function initPaymentEvents() {
    const select = document.getElementById('PaymentType');

    if (!select) return;

    select.addEventListener('change', () => {
        const paymentType = select.value;

        if (!paymentType) {
            window.saleState.payment.type = null;
            return;
        }

        window.saleState.payment.type = paymentType;
        window.saleState.payment.total = window.saleState.totals.total;
    });
}
