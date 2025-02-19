let taxaRejeicaoChart, notaUsabilidadeChart, acoesChart, tempoSessaoChart; // Variáveis para armazenar as instâncias dos gráficos

// Função para buscar e exibir os dados do JSON Server
document.getElementById("periodo").addEventListener("change", updateDashboard);
document.getElementById("site").addEventListener("change", updateDashboard);

function updateDashboard() {
  const periodo = document.getElementById("periodo").value;
  const site = document.getElementById("site").value;

  fetch("http://localhost:3000/dados")
    .then((response) => response.json())
    .then((data) => {
      let container = document.getElementById("data-container");
      // Limpar os dados anteriores
      container.innerHTML = "";

      // Filtrar os dados conforme o período e o site selecionados
      const filteredData = data.filter((data) => {
        return (data.tipo === periodo || periodo === "todos") &&
               (data.site === site || site === "todos");
      });

      // Exibindo os dados
      filteredData.forEach((data) => {
        const card = document.createElement("div");
        card.classList.add("card", "mb-3");
        card.innerHTML = ` 
          <div class="card-body">
            <h5 class="card-title">${data.periodoInicial} a ${data.periodoFinal} (${data.tipo}) - ${data.site}</h5>
            <p><strong>Taxa de Rejeição:</strong> ${data.taxaRejeicao}%</p>
            <p><strong>Ações:</strong> ${data.acoes}</p>
            <p><strong>Tempo Médio de Sessão:</strong> ${data.tempoSessao} segundos</p>
            <p><strong>Nota Usabilidade:</strong> ${data.notaUsabilidade}</p>
          </div>
        `;
        container.appendChild(card);
      });

      // Preparando os dados para os gráficos
      const periodos = filteredData.map((data) => formatDate(data.periodoInicial)); // Formatar as datas
      const taxaRejeicao = filteredData.map((data) => data.taxaRejeicao);
      const notaUsabilidade = filteredData.map((data) => data.notaUsabilidade);
      const acoes = filteredData.map((data) => data.acoes);
      const tempoSessao = filteredData.map((data) => data.tempoSessao);

      // Verificando se os dados para os gráficos não estão vazios
      if (
        !taxaRejeicao.length ||
        !notaUsabilidade.length ||
        !acoes.length ||
        !tempoSessao.length
      ) {
        console.error("Dados para os gráficos estão vazios!" + data);
        return; // Impede a criação de gráficos se os dados não estiverem corretos
      }

      // Atualizando os gráficos com os dados filtrados
      updateCharts(periodos, taxaRejeicao, notaUsabilidade, acoes, tempoSessao);
    })
    .catch((error) => {
      console.error("Erro ao carregar os dados:", error);
    });
}

// Função para formatar a data
function formatDate(dateString) {
  const DateTime = luxon.DateTime;

  // Converte para um formato que o Luxon pode processar
  const formattedDate = DateTime.fromISO(dateString).toFormat("MMM dd, yyyy"); // Exemplo: Jan 01, 2024

  return formattedDate;
}

// Função para destruir gráficos anteriores, se existirem
function destroyChart(chartInstance) {
  if (chartInstance) {
    chartInstance.destroy();
  }
}

function updateCharts(
  periodos,
  taxaRejeicao,
  notaUsabilidade,
  acoes,
  tempoSessao
) {
  destroyChart(taxaRejeicaoChart);
  destroyChart(notaUsabilidadeChart);
  destroyChart(acoesChart);
  destroyChart(tempoSessaoChart);

  // Gráfico de Taxa de Rejeição
  const ctxTaxaRejeicao = document
    .getElementById("taxaRejeicaoChart")
    .getContext("2d");
  taxaRejeicaoChart = new Chart(ctxTaxaRejeicao, {
    type: "line",
    data: {
      labels: periodos,
      datasets: [
        {
          label: "Taxa de Rejeição (%)",
          data: taxaRejeicao,
          borderColor: "rgba(255, 99, 132, 1)",
          backgroundColor: "rgba(255, 99, 132, 0.2)",
          fill: true,
        },
      ],
    },
    options: {
      responsive: true,
      scales: {
        x: { title: { display: true, text: "Período" } },
        y: { title: { display: true, text: "Taxa de Rejeição (%)" } },
      },
    },
  });

  // Gráfico de Nota Usabilidade
  const ctxNotaUsabilidade = document
    .getElementById("notaUsabilidadeChart")
    .getContext("2d");
  notaUsabilidadeChart = new Chart(ctxNotaUsabilidade, {
    type: "bar",
    data: {
      labels: periodos,
      datasets: [
        {
          label: "Nota Usabilidade",
          data: notaUsabilidade,
          backgroundColor: "rgba(54, 162, 235, 0.2)",
          borderColor: "rgba(54, 162, 235, 1)",
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: true,
      scales: {
        x: { title: { display: true, text: "Período" } },
        y: { title: { display: true, text: "Nota Usabilidade" } },
      },
    },
  });

  // Gráfico de Ações Empilhadas
  const ctxAcoes = document.getElementById("acoesChart").getContext("2d");
  acoesChart = new Chart(ctxAcoes, {
    type: "bar",
    data: {
      labels: periodos,
      datasets: [
        {
          label: "Ações",
          data: acoes,
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(75, 192, 192, 0.2)",
          ],
          borderColor: [
            "rgba(255, 99, 132, 1)",
            "rgba(54, 162, 235, 1)",
            "rgba(75, 192, 192, 1)",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: true,
      scales: {
        x: { title: { display: true, text: "Período" } },
        y: { title: { display: true, text: "Ações" } },
      },
    },
  });

  // Gráfico de Tempo Médio de Sessão
  const ctxTempoSessao = document
    .getElementById("tempoSessao")
    .getContext("2d");
  tempoSessaoChart = new Chart(ctxTempoSessao, {
    type: "line",
    data: {
      labels: periodos,
      datasets: [
        {
          label: "Tempo Médio de Sessão (segundos)",
          data: tempoSessao,
          borderColor: "rgba(75, 192, 192, 1)",
          backgroundColor: "rgba(75, 192, 192, 0.2)",
          fill: true,
        },
      ],
    },
    options: {
      responsive: true,
      scales: {
        x: { title: { display: true, text: "Período" } },
        y: {
          title: { display: true, text: "Tempo Médio de Sessão (segundos)" },
        },
      },
    },
  });
}

// Função para carregar e preencher as opções de filtro dinamicamente
function loadFilters() {
  fetch("http://localhost:3000/dados")
    .then((response) => response.json())
    .then((data) => {
      const uniqueSites = [...new Set(data.map((item) => item.site))];
      const siteSelect = document.getElementById("site");

      uniqueSites.forEach((site) => {
        const option = document.createElement("option");
        option.value = site;
        option.textContent = site;
        siteSelect.appendChild(option);
      });
    });
}

// Carregar os filtros assim que a página for carregada
window.onload = loadFilters;
