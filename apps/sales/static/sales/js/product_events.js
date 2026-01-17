document.addEventListener('DOMContentLoaded', () => {
    initProductSearch();
    initAddToCart();
});

function initProductSearch() {
    const input = document.getElementById('SearchProduct');
    const results = document.getElementById('ProductsResults');

    input.addEventListener('input', async () => {
        const name = input.value.trim();
        if (name.length < 2) return;

        const response = await fetch(`/products/search/?pname=${name}`);
        const data = await response.json();

        renderProductResult(data, results);
    });

    document.addEventListener('click', (e) => {
        if (!input.contains(e.target) && !results.contains(e.target)) {
            results.classList.add('d-none');
        }
    });
}

function renderProductResult(products, container) {
     container.innerHTML = '';

    if (!products.length) {
        container.classList.add('d-none');
        return;
    }

    products.forEach(product => {
        const li = document.createElement('li');
        li.className = 'list-group-item list-group-item-action';

        li.innerHTML = `
            <strong>${product.name}</strong><br>
            <small class="text-muted">${product.price}</small>
        `;

        li.addEventListener('click', () => {
            selectProduct(product);
            container.classList.add('d-none');
        });

        container.appendChild(li);
    });

    container.classList.remove('d-none');   
}

function selectProduct(product) {
    window.saleState.selectedProduct = product;
    document.getElementById('SearchProduct').value = product.name;
    document.getElementById('ProductPrice').value = product.price;
}

function initAddToCart() {
    const btn = document.getElementById('AddProductBtn');

    btn.addEventListener('click', () => {
        const product = window.saleState.selectedProduct;

        if (!product) {
            alert('Selecione um produto antes de adicionar ao carrinho');
            return;
        }

        addProductToCart(product);

        window.saleState.selectedProduct = null;
        document.getElementById('SearchProduct').value = '';
        document.getElementById('ProductPrice').value = '';
    });
}

function addProductToCart(product) {
    const existingItem = window.saleState.items.find(
        item => item.product_id === product.id
    );

    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        window.saleState.items.push({
            product_id: product.id,
            name: product.name,
            price: product.price,
            quantity: 1,
            supplier: product.supplier
        });
    }

    recalcTotals();
    renderCart();
}

function recalcTotals() {
    let subtotal = 0;

    window.saleState.items.forEach(item => {
        subtotal += item.price * item.quantity;
    });

    window.saleState.totals.subtotal = subtotal;
    window.saleState.totals.total = subtotal; 

    if (window.saleState.payment) {
        window.saleState.payment.total = subtotal;
    }
}

function renderCart() {
    const tbody = document.getElementById('CartItems');
    tbody.innerHTML = '';

    window.saleState.items.forEach((item, index) => {
        const subtotal = item.price * item.quantity;

        tbody.innerHTML += `
            <tr>
                <td><strong>${item.name}</strong></td>
                <td>${item.supplier ?? '-'}</td>

                <td class="text-center">
                    <input
                        type="number"
                        class="form-control form-control-sm text-center"
                        min="1"
                        value="${item.quantity}"
                        style="max-width: 70px; margin: 0 auto;"
                        onchange="updateItemQuantity(${index}, this.value)"
                    >
                </td>

                <td class="text-end">
                    R$ ${item.price}
                </td>

                <td class="text-end">
                    <strong class="text-success">
                        R$ ${subtotal}
                    </strong>
                </td>

                <td class="text-center">
                    <button
                        class="btn btn-sm btn-outline-danger"
                        onclick="removeItemFromCart(${index})"
                        title="Remover item"
                    >
                        <i class="bi bi-trash"></i>
                    </button>
                </td>
            </tr>
        `;
    });

    document.getElementById('SaleSubTotal').innerText = 'R$ ' + window.saleState.totals.subtotal;
    document.getElementById('SaleTotal').innerText = 'R$ ' + window.saleState.totals.total;
}

function updateItemQuantity(index, value) {
    const qty = parseInt(value);

    if (qty < 1 || isNaN(qty)) return;

    window.saleState.items[index].quantity = qty;
    recalcTotals();
    renderCart();
}

function removeItemFromCart(index) {
    window.saleState.items.splice(index, 1);
    
    recalcTotals();
    renderCart();
}