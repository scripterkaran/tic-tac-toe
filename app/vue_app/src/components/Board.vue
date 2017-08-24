<template>
  <div class="board">
    <div>
      <board-slot v-for="i in 9">

      </board-slot>
    </div>
  </div>
</template>

<script>
  import BoardSlot from './BoardSlot.vue'

  export default {
      props:{},
      components : {BoardSlot}
  }
</script>
