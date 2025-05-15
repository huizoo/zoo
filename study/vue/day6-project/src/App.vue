<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'home'}">Home</RouterLink> | 
      <RouterLink :to="{ name: 'about'}">About</RouterLink> |
      <RouterLink :to="{ name: 'board'}">Board</RouterLink> |
      <RouterLink :to="{ name: 'detail', params: { id: '1' }}">1번 페이지</RouterLink> |
      <RouterLink :to="{ name: 'detail', params: { id: '2' }}">2번 페이지</RouterLink> |
      <RouterLink :to="{ name: 'login'}">Login</RouterLink>
    </nav>
  </header>
  <RouterView/>
</template>

<script setup>
  import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>

</style>



