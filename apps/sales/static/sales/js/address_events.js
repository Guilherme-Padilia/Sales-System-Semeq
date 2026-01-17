document.addEventListener('DOMContentLoaded', () => {
    initAddressSearch();
});

function initAddressSearch() {
    const input = document.getElementById('SearchAddressCEP');

    input.addEventListener('input', async () => {
        const cep = input.value.trim();
        if (cep.length < 8) return;

        const response = await fetch(`/sales/search-addresses/?cep=${cep}`);
        const data = await response.json();
        
        if (data.erro != undefined) {
            alert("Não foi possível encontrar o endereço.: CEP inválido.");
            return;    
        }

        renderAddressResult(data)
    });
}

function renderAddressResult(address) {
    window.saleState.address = address;

    document.getElementById('AddressStreet').value        = address.logradouro;
    document.getElementById('AddressComplement').value    = address.complemento;
    document.getElementById('AddressNeighbordhood').value = address.bairro;
    document.getElementById('AddressCity').value          = address.localidade;
    document.getElementById('AddressState').value         = address.uf;
}