<template>
  <h2>Child</h2>
  {{ counter.name }}
  <GrandChild />
</template>

<script setup>
import { useCounterStore } from "@/stores/counter.js"
import GrandChild from '@/components/GrandChild.vue'

const counter = useCounterStore()

counter.changeName("ssafy")

</script>

<style scoped>

</style>