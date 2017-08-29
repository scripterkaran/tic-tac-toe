<template>
  <div class="slot-box" @click="markMove">
    {{move.position}}
    <span> {{move.symbol}}</span></div>
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
    border: 1px solid red;
    min-height: 40px;
    min-width: 40px;
  }

  .slot-box span {
    text-transform: uppercase;
    font-size: 18px;
    font-weight: 600;
    text-align: center;
    line-height: 40px;
  }
</style>
