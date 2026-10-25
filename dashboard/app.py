const ctx = document.getElementById('grafico').getContext('2d');

const chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [
            {
                label: 'Enviados (MB)',
                borderColor: '#22c55e',
                data: [],
            },
            {
                label: 'Recebidos (MB)',
                borderColor: '#38bdf8',
                data: [],
            }
        ]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: false
            }
        }
    }
});

function carregarDados() {
    fetch('/dados')
        .then(response => response.json())
        .then(data => {
            document.getElementById('hostname').textContent = data.hostname;
            document.getElementById('ip').textContent = data.ip;
            document.getElementById('sistema').textContent = data.sistema_operacional;
            document.getElementById('versao').textContent = data.versao;

            const hora = new Date().toLocaleTimeString();
            chart.data.labels.push(hora);
            chart.data.datasets[0].data.push(data.enviados);
            chart.data.datasets[1].data.push(data.recebidos);

            if (chart.data.labels.length > 12) {
                chart.data.labels.shift();
                chart.data.datasets[0].data.shift();
                chart.data.datasets[1].data.shift();
            }

            chart.update();
        })
        .catch(error => console.error('Erro ao buscar dados:', error));
}

setInterval(carregarDados, 3000);
carregarDados();
