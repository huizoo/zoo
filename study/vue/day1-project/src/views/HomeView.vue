<template>
  <h1>Home</h1>
  <div>message: {{ message }}</div>
</template>

<script setup>
import { ref } from 'vue'

const message = ref('Hello Vue')

</script>

<style scoped>

</style>