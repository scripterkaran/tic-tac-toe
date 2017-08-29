<template>
  <div class="board">
    <div>
      <div v-for="move in moves">
        <board-slot :move="move" @moveMarked="moveMarked"></board-slot>
      </div>
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
        moves: []
      }
    },
    mounted(){
      while (this.moves.length < 9)
        this.moves.push({'position': this.moves.length + 1, 'symbol': ''});
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
