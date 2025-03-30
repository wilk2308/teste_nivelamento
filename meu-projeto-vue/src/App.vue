<template>
  <div id="app" class="container">
    <h1 class="title">Busca de Operadoras de Saúde</h1>
    <p class="description">Digite o nome da operadora para buscar informações detalhadas sobre ela.</p>
    
    <div class="search-box">
      <input
        v-model="searchTerm"
        placeholder="Buscar operadora"
        class="search-input"
        @keyup.enter="buscarOperadoras"
      />
      <button @click="buscarOperadoras" class="search-button">Buscar</button>
      <button @click="limparBusca" class="clear-button">Limpar</button>
    </div>
    
    <div v-if="loading" class="loading-message">
      Carregando resultados...
    </div>
    
    <ul v-if="operadoras.length > 0" class="operadoras-list">
      <li 
        v-for="operadora in operadoras" 
        :key="operadora.Registro_ANS" 
        class="operadora-item"
        @click="mostrarDetalhes(operadora)"
      >
        {{ operadora.Razao_Social }}
      </li>
    </ul>

    <!-- Exibir detalhes da operadora -->
    <div v-if="detalhesOperadora" class="detalhes-operadora">
      <h3>{{ detalhesOperadora.Razao_Social }}</h3>
      <p><strong>CNPJ:</strong> {{ detalhesOperadora.CNPJ }}</p>
      <p><strong>Nome Fantasia:</strong> {{ detalhesOperadora.Nome_Fantasia }}</p>
      <p><strong>Modalidade:</strong> {{ detalhesOperadora.Modalidade }}</p>
      <p><strong>Endereço:</strong> {{ detalhesOperadora.Logradouro }}, {{ detalhesOperadora.Numero }} {{ detalhesOperadora.Complemento }}, {{ detalhesOperadora.Bairro }}, {{ detalhesOperadora.Cidade }} - {{ detalhesOperadora.UF }} {{ detalhesOperadora.CEP }}</p>
      <p><strong>Telefone:</strong> {{ detalhesOperadora.DDD }} {{ detalhesOperadora.Telefone }}</p>
      <p><strong>Email:</strong> {{ detalhesOperadora.Endereco_eletronico }}</p>
      <p><strong>Representante:</strong> {{ detalhesOperadora.Representante }} ({{ detalhesOperadora.Cargo_Representante }})</p>
      <p><strong>Data de Registro ANS:</strong> {{ detalhesOperadora.Data_Registro_ANS }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      operadoras: [],
      searchTerm: '',
      loading: false,
      detalhesOperadora: null,
      apiBaseUrl: process.env.NODE_ENV === 'production' 
        ? 'https://teste-nivelamento.onrender.com' 
        : 'http://localhost:8000'
    };
  },
  methods: {
    buscarOperadoras() {
      if (this.searchTerm) {
        this.loading = true;
        axios.get(`${this.apiBaseUrl}/buscar?q=${this.searchTerm}`)
          .then((response) => {
            this.operadoras = response.data;
          })
          .catch((error) => {
            console.error("Erro ao buscar operadoras:", error);
          })
          .finally(() => {
            this.loading = false;
          });
      }
    },
    mostrarDetalhes(operadora) {
      this.detalhesOperadora = operadora;
    },
    limparBusca() {
      this.searchTerm = '';
      this.operadoras = [];
      this.detalhesOperadora = null;
    }
  }
};
</script>

<style scoped>
.container {
  width: 80%;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Arial', sans-serif;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.title {
  text-align: center;
  font-size: 24px;
  margin-bottom: 10px;
}

.description {
  text-align: center;
  font-size: 16px;
  margin-bottom: 20px;
}

.search-box {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.search-input {
  width: 100%;
  max-width: 400px;
  padding: 12px;
  font-size: 16px;
  border: 2px solid #ddd;
  border-radius: 8px;
  outline: none;
  transition: border-color 0.3s ease;
}

.search-input:focus {
  border-color: #4CAF50;
}

.search-button, .clear-button {
  padding: 12px 20px;
  font-size: 16px;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  margin-left: 10px;
  transition: background-color 0.3s ease;
}

.search-button {
  background-color: #4CAF50;
}
.search-button:hover {
  background-color: #45a049;
}
.search-button:active {
  background-color: #388e3c;
}

.clear-button {
  background-color: #d9534f;
}
.clear-button:hover {
  background-color: #c9302c;
}
.clear-button:active {
  background-color: #ac2925;
}

.loading-message {
  text-align: center;
  font-size: 16px;
  color: #4CAF50;
  margin-top: 10px;
}

.operadoras-list {
  list-style-type: none;
  padding: 0;
}

.operadora-item {
  background-color: #ffffff;
  margin: 10px 0;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  font-size: 18px;
  transition: background-color 0.3s ease;
  cursor: pointer;
}

.operadora-item:hover {
  background-color: #f1f1f1;
}

.detalhes-operadora {
  margin-top: 20px;
  padding: 15px;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.detalhes-operadora p {
  font-size: 16px;
  margin: 5px 0;
}

.detalhes-operadora h3 {
  font-size: 24px;
  margin-bottom: 10px;
}
</style>
