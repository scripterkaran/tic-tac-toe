<template>
  <div class="board">
      <table>
        <tr v-for="i in 3">
            <td v-for="i in 3"> x </td>
        </tr>
      </table>
  </div>
</template>

<script>
  import BoardSlot from './BoardSlot.vue'

  export default {
      props:{},
      components : {BoardSlot}
  }
</script>


<style>
  .board table{
    margin: 0 auto;
  }
</style>
