document.addEventListener('DOMContentLoaded', () => {
    loadSalesHistory();
});

async function loadSalesHistory() {
    const table = document.getElementById('SalesHistory');

    try {
        const response = await fetch('/history/sales/');
        
        if (response.status != 200) {
            throw new Error('Error loading sales history');
        }

        const data = await response.json();

        renderSalesHistory(data, table);

    } catch (error) {
        console.error(error);
        table.innerHTML = `
            <tr>
                <td colspan="5" class="text-center text-danger py-4">
                    Erro ao carregar histórico de vendas.
                </td>
            </tr>
        `;
    }
}

function renderSalesHistory(sales, container) {
    container.innerHTML = '';

    if (!sales.length) {
        container.innerHTML = `
            <tr>
                <td colspan="5" class="text-center text-muted py-4">
                    Nenhuma venda encontrada.
                </td>
            </tr>
        `;
        return;
    }

    sales.forEach(sale => {
        container.innerHTML += `
            <tr>
                <td>${sale.id}</td>
                <td>${sale.customer}</td>
                <td>${formatDate(sale.date)}</td>
                <td class="text-end">R$ ${Number(sale.total).toFixed(2)}</td>
                <td class="text-center">
                    <span class="badge ${sale.status === 'CONFIRMED' ? 'bg-success' : 'bg-warning text-dark'}">
                        Faturada
                    </span>
                </td>
            </tr>
        `;
    });
}

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('pt-BR') + ' ' +
           date.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });
}