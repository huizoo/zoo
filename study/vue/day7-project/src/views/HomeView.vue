<template>
 <h1>Home</h1>
 <div>count: {{ counter.count }}</div>
 <div>doubleCount: {{ counter.doubleCount }}</div>
 <HomeChild />
</template>

<script setup>
import { useCounterStore } from "@/stores/counter"
import HomeChild from '@/components/HomeChild.vue'

const counter = useCounterStore()

counter.count = 3
counter.increment()

</script>

<style scoped>

</style>