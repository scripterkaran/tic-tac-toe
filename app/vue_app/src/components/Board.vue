<template>
  <div class="board">
    <div>
      <table>
          <tr v-for='row in board'>
            <td v-for='slot in row'>
              <board-slot :move="{'row': row , 'position': slot}" @moveMarked="moveMarked"></board-slot>
            </td>
          </tr>
        </table>
    </div>
  </div>
</template>

<script>
  import BoardSlot from './BoardSlot.vue'

  export default {
    props: {},
    data(){
      return {
        user_selection: 'O',
        markedIndex: [],
        board: [[1,2,3],[4,5,6],[7,8,9]]
      }
    },
    mounted(){

    },
    components: {BoardSlot},
    methods: {
      moveMarked(args){
        //emit a http call
//        this.markedIndex.concat([args])
        let moved = this.moves[args - 1]
        moved.symbol = 'X'
        this.emitOtherPlayer()
      },
      emitOtherPlayer(){ // needs work ofcourse
        var randomItem = this.moves[Math.floor(Math.random() * this.moves.length)]
        randomItem.symbol = "O"
      }
    }
  }
</script>


<style>
  .board table {
    margin: 0 auto;
  }
</style>
