document.addEventListener('DOMContentLoaded', () => {
    initLogin();
});

function initLogin() {
    const btn = document.getElementById('BtnLogin');
    const password = document.getElementById('password');
    const email = document.getElementById('email');

    btn.addEventListener('click', async () => {
        btn.disabled = true; 
        btn.innerText = 'Carregando...';

        if (!password.value) {
            alert('Necessário preencher a senha para realizar o login!');
            return;
        }

        if (!email.value) {
            alert('Necessário preencher o email para realizar o login!')
            return;
        }

        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        const response = await fetch('/signin/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                email: email.value,
                password: password.value
            })
        });

        if (response.status != 200) {
            alert('Erro ao realizar login ' + response.status);
            location.reload();
            return;
        } else {
            alert('Login realizado com sucesso!');
            window.location.href = '/modules/';
        }
    })
}