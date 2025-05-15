<template>
  <div>
    <h1>여기는 {{ num }}번 글의 상세 페이지 입니다.</h1>
    <RouterLink :to="{ name: 'over-thirty' }">30세 이상</RouterLink>
    <hr />
    <RouterLink :to="{ name: 'under-thirty' }">30세 미만</RouterLink>
  </div>
</template>

<script setup>
import { ref, watch } from "vue";
import { useRoute, onBeforeRouteUpdate } from "vue-router";

const route = useRoute();
const num = ref(route.params.id);

onBeforeRouteUpdate((to, from, next) => {
  num.value = to.params.id
  next()
})
</script>

<style scoped></style>
