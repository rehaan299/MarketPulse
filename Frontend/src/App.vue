<template>
  <main class="max-w-4xl mx-auto p-8">
    <header class="mb-8">
      <h1 class="text-4xl font-bold tracking-tight">MarketPulse</h1>
      <p class="text-slate-600 mt-2">
        Real-time market sentiment dashboard for TD stock
      </p>
    </header>

    <section class="flex items-center gap-6 mb-6">
      <div class="text-2xl font-semibold">
        ${{ price }}
      </div>

      <span :class="sentimentClass">
        {{ sentimentLabel }}
      </span>
    </section>

    <section class="bg-white rounded-xl shadow p-6">
      <Line :data="chartData" :options="chartOptions" />
    </section>
  </main>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  LineElement,
  PointElement,
  LinearScale,
  CategoryScale,
  Tooltip,
  Legend
} from 'chart.js'

ChartJS.register(
  LineElement,
  PointElement,
  LinearScale,
  CategoryScale,
  Tooltip,
  Legend
)

const price = ref(0)
const sentiment = ref(0)

const chartData = ref({
  labels: [],
  datasets: [{
    label: 'TD Stock Price',
    data: [],
    borderColor: '#2563eb',
    borderWidth: 2,
    tension: 0.3
  }]
})

const chartOptions = {
  responsive: true,
  animation: false,
  plugins: {
    legend: { display: false }
  }
}

const sentimentLabel = computed(() =>
  sentiment.value >= 0 ? 'Positive Sentiment' : 'Negative Sentiment'
)

const sentimentClass = computed(() =>
  sentiment.value >= 0
    ? 'bg-emerald-100 text-emerald-700 px-4 py-1 rounded-full text-sm font-semibold'
    : 'bg-rose-100 text-rose-700 px-4 py-1 rounded-full text-sm font-semibold'
)

onMounted(() => {
  const ws = new WebSocket('ws://localhost:8000/ws/TD')

  ws.onmessage = (event) => {
    const data = JSON.parse(event.data)

    price.value = data.price
    sentiment.value = data.sentiment_score

    chartData.value.labels.push(
      new Date(data.timestamp).toLocaleTimeString()
    )
    chartData.value.datasets[0].data.push(data.price)

    if (chartData.value.labels.length > 25) {
      chartData.value.labels.shift()
      chartData.value.datasets[0].data.shift()
    }
  }
})
</script>
