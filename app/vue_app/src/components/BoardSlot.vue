<template>
  <div class="slot-box" @click="markMove">
    <span class="meta"> {{move.position}} - {{move.row }}</span></div>
</template>

<script>
  export default {
    props: ['index', 'move'],
    methods: {
      markMove(){
        this.$emit('moveMarked', this.move.position)
      },
    }
  }
</script>

<style scoped>
  .slot-box {
    width: 15vw;
    height: 15vw;
    background: #6C7A89;
    cursor: pointer;
    font-size: 15vw;
    line-height: 15vw;
    text-align: center;
    color: white;
  }
  .meta{
      font-size: 10px;
       position: absolute;
   }
</style>
