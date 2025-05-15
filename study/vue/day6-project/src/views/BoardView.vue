<template>
  <div>
    <h1>Board</h1>
  </div>
  
</template>

<script setup>
import { onBeforeRouteLeave } from 'vue-router'

onBeforeRouteLeave((to, from, next) => {
  console.log('onBeforeRouteLeave fired', to, from)
  const ask = window.confirm('정말 떠나실 건가요?')
  if (ask) {
    next()
  } else {
    next(false)
  }
})

</script>

<style scoped></style>
