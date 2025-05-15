<template>
  <h3>GrandChild</h3>
  {{  counter.count  }}
</template>

<script setup>
import { useCounterStore } from "@/stores/counter"
const counter = useCounterStore()
counter.count++
</script>

<style scoped>

</style>