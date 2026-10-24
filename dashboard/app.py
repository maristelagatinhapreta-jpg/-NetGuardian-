<hr>

<h3>📊 Tráfego de Rede em Tempo Real</h3>

<canvas id="grafico" width="700" height="300"></canvas>

https://cdn.jsdelivr.net/npm/chart.jsscript>

<script>

const ctx = document.getElementById('grafico').getContext('2d');

const grafico = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [
            {
                label: 'Enviados (MB)',
                borderColor: '#22c55e',
                data: []
            },
            {
                label: 'Recebidos (MB)',
                borderColor: '#38bdf8',
                data: []
            }
        ]
    },
    options: {
        responsive: true
    }
});

function atualizarGrafico() {

    fetch('/dados')

    .then(response => response.json())

    .then(data => {

        const hora = new Date().toLocaleTimeString();

        grafico.data.labels.push(hora);

        grafico.data.datasets[0].data.push(data.enviados);

        grafico.data.datasets[1].data.push(data.recebidos);

        if (grafico.data.labels.length > 10) {

            grafico.data.labels.shift();

            grafico.data.datasets[0].data.shift();

            grafico.data.datasets[1].data.shift();

        }

        grafico.update();

    });

}

setInterval(atualizarGrafico, 3000);

atualizarGrafico();

</script>