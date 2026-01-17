document.addEventListener('DOMContentLoaded', () => {
    initFinishSale();
    initExitSale();
});

let cart = [];

function initFinishSale() {
    const btn = document.getElementById('FinishSaleBtn');

    btn.addEventListener('click', async () => {
        const state = window.saleState;

        if (!checkRequiredFields(state)) {
            return
        }
        
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        const response = await fetch('/sales/create/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(window.saleState)
        });

        if (response.status = 200) {
            alert('Venda concluida com sucesso!');
            location.reload();
        }
    });
}

function initExitSale(){
    const btn = document.getElementById('ExitSaleBtn');
    
    btn.addEventListener('click', () => {
        location.reload();
    });
}

function checkRequiredFields(state){
    if (!state.customer) {
        alert('Selecione um cliente.');
        return false;
    }

    if (!state.address) {
        alert('Selecione um endereço de entrega.');
        return false;
    }

    if (!state.items) {
        alert('Adicione ao menos um produto no carrinho.');
        return false;
    }

    if (!state.payment) {
        alert('Selecione a forma de pagamento.');
        return false;
    }

    if (!state.totals || state.totals.total <= 0) {
        alert('Total da venda inválido.');
        return false;
    }

    return true;  
}

function getCSRFToken() {
    return document.cookie.split('; ').find(row => row.startsWith('csrftoken='))?.split('=')[1];
}