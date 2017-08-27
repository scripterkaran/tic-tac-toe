<template>
  <div class="board">
      <table>
        <tr v-for="i in 3">
            <td v-for="i in 3">
              <board-slot :user_selection="user_selection"></board-slot>
            </td>
        </tr>
      </table>
  </div>
</template>

<script>
  import BoardSlot from './BoardSlot.vue'

  export default {
      props:{},
      data(){
          return {
              user_selection: 'O'
          }
      },
      components : {BoardSlot}
  }
</script>


<style>
  .board table{
    margin: 0 auto;
  }
</style>
