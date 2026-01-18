document.addEventListener('DOMContentLoaded', () => {
    initCustomerSearch();
});

function initCustomerSearch() {
    const input = document.getElementById('SearchCustomer');
    const results = document.getElementById('CustomerResults');

    input.addEventListener('input', async () => {
        const name = input.value.trim();
        if (name.length < 2) return;

        const response = await fetch(`/sales/search-customers/?name=${name}`);
        const customers = await response.json();

        renderCustomerResults(customers, results);
    });

    document.addEventListener('click', (e) => {
        if (!input.contains(e.target) && !results.contains(e.target)) {
            results.classList.add('d-none');
        }
    });

    input.addEventListener('click', async () => {
        const response = await fetch(`/sales/search-customers/`);
        const customers = await response.json();

        renderCustomerResults(customers, results);
    });
}

function selectCustomer(customer) {
    window.saleState.customer = customer

    document.getElementById('CustomerName').value = customer.name;
    document.getElementById('CustomerPhone').value = customer.phone;
    document.getElementById('SearchCustomer').value = customer.name;
}

function renderCustomerResults(customers, container) {
    container.innerHTML = '';

    if (!customers.length) {
        container.classList.add('d-none');
        return;
    }

    customers.forEach(customer => {
        const li = document.createElement('li');
        li.className = 'list-group-item list-group-item-action';

        li.innerHTML = `
            <strong>${customer.name}</strong><br>
            <small class="text-muted">${customer.phone}</small>
        `;

        li.addEventListener('click', () => {
            selectCustomer(customer);
            container.classList.add('d-none');
        });

        container.appendChild(li);
    });

    container.classList.remove('d-none');
}