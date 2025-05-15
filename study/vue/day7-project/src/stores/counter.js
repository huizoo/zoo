import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const name = ref("minho")
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }
  function changeName(newName) {
    name.value = newName
  }

  return { count, name, doubleCount, increment, changeName }
})
